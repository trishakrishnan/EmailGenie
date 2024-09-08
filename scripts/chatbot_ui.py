import streamlit as st
from chat import chat_response

# Set page configuration
st.set_page_config(
    page_title="EmailGenie",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar content
with st.sidebar:
    st.markdown("<h1 style='color: #FF6F00;'>EmailGenie</h1>", unsafe_allow_html=True)
    st.subheader("Basic Inputs to get started")

    email_type = st.radio(
        "What kind of outreach email do you want to generate?",
        ('Sales pitch', 'Networking Introduction', 'Job Inquiry', 'Event Invitation'),
        index=0,
        horizontal=False
    )

    st.subheader("Recipient Details")
    recipient_name = st.text_area("Recipient's Details - Name, company, role")

    st.subheader("Sender Details")
    sender_name = st.text_area("Sender's Details - Name, company, role")


    tone = st.radio("What should be the tone of the email?", ("Formal", "Casual", "Professional"), index=0, horizontal=True)
    cta = st.text_area("What is the Call to Action")



# Initialize chat history
    if "chat_enabled" not in st.session_state:
        st.session_state.chat_enabled = False
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = ""

    if "chat_history_user" not in st.session_state:
        st.session_state.chat_history_user = ""
    
    if "chat_history_ai" not in st.session_state:
        st.session_state.chat_history_ai = ""

    if "response" not in st.session_state:
            st.session_state.response = ""

    if "prompt" not in st.session_state:
        st.session_state.prompt = ""


 
    # Display submit button and handle the chat initiation
    if st.button("Submit"):
        # Clear previous chat history for a fresh start
        st.session_state.chat_history = ""
        st.session_state.chat_history_user = ""
        st.session_state.chat_history_ai = ""
        # Get the response from the LLM API
        response = chat_response(email_type, recipient_name,
                                 sender_name, tone, cta,st.session_state.prompt, st.session_state.chat_history)

        
        # Update the chat history
        st.session_state.chat_history += f"\nAI: {response}"

        st.session_state.response = response

        # Enable the chat after submit
        st.session_state.chat_enabled = True


# Main content with the heading
st.markdown("<h1 style='font-size: 3em; color: #FF6F00;'>EmailGenie</h1>", unsafe_allow_html=True)
st.write("EmailGenie is an AI-powered email generator designed to craft personalized cold outreach emails. ")
st.write("Step 1: Fill out the form in the left panel and hit submit")
st.write("Step 2: EmailGenie will generate a personalised outreach email for you below. Continue chatting with EmailGenie to refine the email as per your needs.")

if st.session_state.response:
    st.markdown(f"""
        <div style='display: flex; align-items: center; margin-top: 20px;'>
            <div style='background-color: #6C757D; padding: 10px 15px; border-radius: 10px; color: white; max-width: 60%;'>
                {st.session_state.response} 
            </div>
        </div>
        """, unsafe_allow_html=True)


# Display chat messages
for chat_user, chat_ai in zip(st.session_state.chat_history_user.split("\nUser:"), st.session_state.chat_history_ai.split("\nAI:")):
    if chat_user.strip():
        st.markdown(f"""
    <div style='display: flex; align-items: center; justify-content: flex-end; margin-top: 10px;'>
        <div style='background-color: #007BFF; padding: 10px 15px; border-radius: 10px; color: white; max-width: 60%;'>
            {chat_user.strip()}
        </div>
    </div>
""", unsafe_allow_html=True)
    if chat_ai.strip():
        st.markdown(f"""
            <div style='display: flex; align-items: center; margin-top: 20px;'>
                <div style='background-color: #6C757D; padding: 10px 15px; border-radius: 10px; color: white; max-width: 60%;'>
                    {chat_ai.strip()}
                </div>
            </div>
        """, unsafe_allow_html=True)


if st.session_state.chat_enabled:
    prompt = st.chat_input("Type your message here...")

    if prompt:
        # Get the response from the LLM API
        response = chat_response(email_type, recipient_name,
                                 sender_name, tone, cta, prompt, st.session_state.chat_history)

        # Update the chat history
                # Update the chat history
        st.session_state.chat_history += f"\nUser: {prompt}\nAI: {response}"

        st.session_state.chat_history_user += f"\nUser: {prompt}"
        st.session_state.chat_history_ai += f"\nAI: {response}"



        # Display user message
        st.markdown(f"""
            <div style='display: flex; align-items: center; justify-content: flex-end; margin-top: 10px;'>
                <div style='background-color: #007BFF; padding: 10px 15px; border-radius: 10px; color: white; max-width: 60%;'>
                    {prompt}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Display AI response
        st.markdown(f"""
            <div style='display: flex; align-items: center; margin-top: 20px;'>
                <div style='background-color: #6C757D; padding: 10px 15px; border-radius: 10px; color: white; max-width: 60%;'>
                    {response} 
                </div>
            </div>
            """, unsafe_allow_html=True)
