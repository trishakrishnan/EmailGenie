from config import email_type_description, email_type_questions
import streamlit as st
from emails import generate_email
import json
from util_functions import (add_user_to_gsheet,
                             update_user_on_gsheet, 
                             send_email_via_mailjet, 
                             extract_subject_line_email_body)


if 'page' not in st.session_state:
    st.session_state.page = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "generated_email" not in st.session_state:
    st.session_state.generated_email = ""

if "template_send" not in st.session_state:
    st.session_state.template_send = 0

if "template_save" not in st.session_state:
    st.session_state.template_save = 0


with st.sidebar:
    st.markdown("<h1 style='color: #FF6F00;'>EmailGenie</h1>", unsafe_allow_html=True)


    page_name  = { 0: 'Registration',1: 'Personalise your Email',2: 'Generate Email',3: 'Send Email'}
    page_instructions = {
    0: "Fill in your name, industry, role, and the type of email you wish to generate to get started",
    1: "\n\n Answer these questions to personalise the email to your specific usecase. \n \n  The more details you mention the more personalised the email can be",
    2: "Review the generated email draft, provide any further instructions, or regenerate the email.",
    3: "Preview, edit, and send the final email to your audience\n\n"
}
    num_pages =4
    

     # Custom CSS for unified text and radio styling
    st.markdown("""
        <style>
        .sidebar-text {
            font-size: 16px;
            padding: 10px;
            color: #000000;
            border-radius: 5px;
        }
        .sidebar-text:hover {
            background-color: #e0e0e0;
            cursor: pointer;
        }
        .sidebar-text.active {
            background-color: #d6d6d6;
            font-weight: bold;
            color: #000000;
        }
        .sidebar-title {
            font-size: 18px;
            font-weight: bold;
            color: #FF6F00; /* Orange color for header */
            margin-bottom: 15px;
        }
        .sidebar-text.inactive {
            color: #8a8a8a;
        }
        </style>
    """, unsafe_allow_html=True)

    # Display all page names in the radio button but disable future pages
    options = [page_name[i] for i in range(num_pages)]
    st.markdown(f"<div class='sidebar-title'>Navigation Guide</div>", unsafe_allow_html=True)

    for i in range(num_pages):
        # Set active class if the page is the current one
        if i == st.session_state.page:
            st.markdown(f"<div class='sidebar-text active'>{page_name[i]}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='sidebar-text inactive'>{page_name[i]}</div>", unsafe_allow_html=True)


    # Display instructions for the current page
    st.markdown(f"<div class='sidebar-title'>Instructions</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='sidebar-description'>{page_instructions[st.session_state.page]}</div>", unsafe_allow_html=True)

    st.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True) 

    st.markdown("\n\nYou can find your user profile data and saved templates [here](https://docs.google.com/spreadsheets/d/1eb9SiWTXspLVlpGtoYj0ChNUtLreRyzTs6UScDH2yxE/edit?usp=sharing)")


st.markdown("<h1 style='font-size: 3em; color: #FF6F00;'>EmailGenie</h1>", unsafe_allow_html=True)
st.write("EmailGenie is an AI-powered email generator designed to craft personalized cold outreach emails.") 

# Step 1: Create form for basic user inputs

if st.session_state.page == 0:

    # Collect initial inputs
    with st.form("initial_form"):
        name = st.text_input("Your Name")
        industry = st.text_input("Your Industry")
        role = st.text_input("Your Role")
        email_type = st.radio("Select the type of email", list(email_type_description.keys()))

        submit = st.form_submit_button("Register and Next")

    if submit:
        st.session_state.name = name
        st.session_state.industry = industry
        st.session_state.role = role
        st.session_state.email_type = email_type
        st.session_state.page = 1
        if name and industry and role and email_type:
            add_user_to_gsheet(name, industry, role, email_type)
            st.session_state['submitted'] = True  # Mark the form as submitted

        else:
            st.error("Please fill in all the fields.")

        st.rerun()



# Step 2: Display specific questions for the chosen email type
if st.session_state.page == 1:
    st.markdown(f'<div class="subheader-text">Follow-up Questions for {st.session_state.email_type}.</div>', unsafe_allow_html=True)

    # Show relevant questions
    questions = email_type_questions[st.session_state.email_type].split("\n")
    with st.form("email_questions"):
        answers = {}
        for question in questions:
            if question.strip():
                answers[question.strip()] = st.text_area(question.strip())

        submit_answers = st.form_submit_button("Generate Drafts")

    if submit_answers:
        st.session_state.answers = answers
        st.session_state.page = 2

        if st.session_state.answers:
            try:
                update_user_on_gsheet(st.session_state.name,  st.session_state.industry, st.session_state.role, st.session_state.email_type, 'EmailTypeData', json.dumps(st.session_state.answers, ensure_ascii=False))
                st.success("Email drafts have been saved successfully.")
            except:
                st.error("Email drafts has NOT been saved successfully.")
                
        else:
            st.error("Please fill in all the fields.")
        st.rerun()




# Step 3: Show generated drafts and additional inputs
if st.session_state.page == 2:

    # Custom CSS for aesthetics
    st.markdown("""
        <style>
            .subheader-text {
                font-size: 24px;

                color: #ff6f00; /* You can adjust the color */
            }
            .email-box {
                border: 2px solid black;
                border-radius: 10px;
                padding: 15px;
                background-color: #333333;
                margin-bottom: 20px;
            }
            .button-style {
                background-color: #ff6f00; /* Button background color */
                color: white;
                font-weight: bold;
                font-size: 16px;
                border-radius: 8px;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
            }
            .button-style:hover {
                background-color: #e65100; /* Hover effect */
            }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<div class="subheader-text">Following is the email draft generated using the provided inputs.</div>', unsafe_allow_html=True)

    # Call the separate function for email generation
    
    generated_email = generate_email(
        st.session_state.email_type,
        st.session_state.answers,
        st.session_state.feedback
    )
    st.session_state.generated_email = generated_email


    st.markdown(f'<div class="email-box">{st.session_state.generated_email.strip()}</div>', unsafe_allow_html=True)


    # Allow user to provide further instructions
    additional_instructions = st.text_area("Add any further instructions or modifications to the drafts")

    regenerate_col, send_col, go_back = st.columns(3)
    
    with regenerate_col:
        if st.button("Regenerate Email", key="regen_button"):

            # Collect feedback and regenerate emails
            st.session_state.feedback= additional_instructions 
            st.session_state.reset_instructions = True
            st.rerun()
 
    with send_col:
        if st.button("Preview and Send Email", key="send_button"):
            st.session_state.page = 3
            st.rerun()
    
    with go_back:
        if st.button("Go Back"):
            st.session_state.page = 1
            st.rerun()




# Step 4: Preview, edit, and send the email
if st.session_state.page == 3:


    st.session_state.template_save = 0

    st.subheader("Review and Edit Your Email")
    
    # Allow the user to modify the email
    edited_email = st.text_area("Edit the email content", st.session_state.generated_email, height=300)
    st.session_state.generated_email = edited_email

    # Input the 'to' and 'from' email addresses
    recipient_name = st.text_input("Recipient Name")
    to_email = st.text_input("Recipient Email Address (To)")


    subject, email_content = extract_subject_line_email_body(st.session_state.generated_email)

    send_email,save_col, go_back = st.columns(3)

    email_success_code = ""

    # Button to send email
    with send_email:
        if st.button("Confirm and Send Email"):
            if to_email and edited_email:
                # Call the send_email_via_sendgrid function
                email_success_code = send_email_via_mailjet(
                    recipient_name = recipient_name,
                    recipient_email=to_email,
                    subject=subject,
                    body=email_content
                )
                
                # Display success or error message based on the function's return value
                if email_success_code==200:
                    st.session_state.template_send = 1
                    st.rerun()
                elif email_success_code :
                    st.session_state.template_send = -1
                    st.rerun()

            else:
                st.error("Please provide 'to' email addresses.")

        

    with save_col:
        if st.button("Save Email Template", key="save_button"):
            if edited_email:
                update_user_on_gsheet(st.session_state.name,  st.session_state.industry, st.session_state.role, st.session_state.email_type, 'Template', edited_email)
                st.session_state.template_save = 1
            else:
                st.error("Please fill in all the fields.")
        
    with go_back:
        if st.button("Go Back"):
            st.session_state.page = 2
            st.rerun()


    if st.session_state.template_save ==1:
        st.success("Email template has been saved successfully.")

    if st.session_state.template_send ==1:
        st.success("Email successfully sent")
    elif st.session_state.template_send ==-1:
        st.error("Error in sending email")


