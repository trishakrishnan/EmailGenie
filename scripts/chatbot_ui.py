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
    st.write("EmailGenie is an AI-powered email generator designed to craft personalized cold outreach emails. Type in some basic information below and EmailGenie will generate a personalised outreach email for you. Continue chatting with EmailGenie to refine the email as per your needs.")
    st.subheader("Basic Inputs to get started")
    email_type = st.radio(
        "What kind of outreach email do you want to generate?",
        ('Sales pitch', 'Networking Introduction', 'Job Inquiry', 'Event Invitation', 'Content Promotion',
         'Testimonial Request', 'Connect on social media'),
        index=0,
        horizontal=False
    )
    
    purpose_questions = {
        'Sales pitch': 'What are the key benefits of the product',
        'Networking Introduction': 'Key things about you that you want to mention',
        'Job Inquiry': 'Tell me more about the job and your experience relevant to the job',
        'Event Invitation': 'What is the event about?',
        'Content Promotion': 'What are the key highlights about your content',
        'Testimonial Request': 'Tell me more about the product/service you want a testimonial for',
        'Connect on social media': 'Tell me more about you'
    }

    # Set the default value of the text area based on the selected email type
    product_content = st.text_area(purpose_questions[email_type])
    recipient_content = st.text_area("Tell me more about the recipient")
    tone = st.radio("What should be the tone of the email?", ("Formal", "Casual", "Professional"), index=0, horizontal=True)


# Initialize chat history
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
        # Get the response from the LLM API
        response = chat_response(email_type, purpose_questions, product_content, recipient_content, tone,st.session_state.prompt, st.session_state.chat_history)

        # Update the chat history
        st.session_state.chat_history += f"\nAI: {response}"

        st.session_state.response = [response, "Add in any additional comments or feedback to tailor this email to your needs"]

# Main content with the heading
st.markdown("<h1 style='font-size: 3em; color: #FF6F00;'>EmailGenie</h1>", unsafe_allow_html=True)
st.subheader("Talk your way through data")

if st.session_state.response:
    st.markdown(f"""
        <div style='display: flex; align-items: center; margin-top: 20px;'>
            <div style='background-color: #6C757D; padding: 10px 15px; border-radius: 10px; color: white; max-width: 60%;'>
                {st.session_state.response[0]} 
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style='display: flex; align-items: center; margin-top: 20px;'>
            <div style='background-color: #6C757D; padding: 10px 15px; border-radius: 10px; color: white; max-width: 60%;'>
                {st.session_state.response[1]} 
            </div>
        </div>
        """, unsafe_allow_html=True)


# Display chat messages
for chat_user, chat_ai in zip(st.session_state.chat_history_user.split("\nUser:"), st.session_state.chat_history_ai.split("\nAI:")):
    if chat_user.strip():
        st.markdown(chat_user.strip())
    if chat_ai.strip():
        st.markdown(chat_ai.strip())


# Chat input
prompt = st.chat_input("Type your message here...")

if prompt:
    # Get the response from the LLM API
    response = chat_response(email_type, purpose_questions, product_content, recipient_content, tone, prompt, st.session_state.chat_history)

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
