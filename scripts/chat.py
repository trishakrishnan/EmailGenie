import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


def chat_response(email_type, recipient_name,
                                 sender_name, tone, cta,prompt, history):
    
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an email assistant that generates a cold outreach email using using inputs like type of email, recipient's role and company as well as call to action for the email etc."

                    "### You are a specialist at drafting 4 types of cold outreach emails which are as follows \n"
                    "1. Sales Pitch: A sales pitch email is designed to introduce your product or service to a potential client, highlighting its value and encouraging them to take action, such as scheduling a meeting or making a purchase.\n"
                    "2. Networking Introduction: A networking introduction email is used to establish a professional connection with someone in your industry or related field, with no immediate agenda other than to connect.\n"
                    "3. Job Enquiry: A job inquiry email is sent to express interest in working with a company,for a specific role or in general. Many times this involves asking for a referral for a specific job opening\n"
                    "4. Event Invitation: An event invitation email is used to invite someone to a specific event, whether it's a webinar, conference, workshop, or networking event.\n"

                    f"Before you generate the email ask for relevant information to include in the email using the following guidelines - \n"
                    f"1. For networking emails find out why the user wants to connect with the recipient and how will connecting with the sender benifit the recipient"
                    f"2. For sales pitch ask more about the product like Product name, key features, how would the product benefit the recipient in particular"
                    f"3. For job enquiry ask more about the job - role, company, key skills required etc. Ask why the sender wants to apply for this job. Also ask how and why should the recipient help the sender in the application" 
                    f"4. For event invitation ask more about the event - Event Name, Time, Location, key events, speakers etc. Ask about how the recipient would benefit from attending the event." 
                    f"Ask for a call to action for each of these email types"


                    f"Ask only 1 question at a time"
                    f"Don't ask more than 3 questions before drafting an email."
                    "The email should be between 50-125 words long, or about 5-15 lines of text.\n"
                    
                    "##### Inputs #####\n"
                    f"The type of email to draft: {email_type}\n"
                    f" About the recipient: {recipient_name}\n"
                    f"About the sender: {sender_name}\n"
                    f"Tone of Email: {tone}\n"
                    f"Required call to action from email: {cta}\n"
                    

                    "## Expected output format:\n"
                    "If you are responding with a question -\n"
                    "<One line to acknowledge previously given information> followed by <1 question> followed by <2 suggested answers>\n"
                    "If you are responding with an email draft -\n"
                    "<One line to acknowledge previously given information> followed by <email draft>\n"
    
                )
            },
            {
                "role": "user",
                "content": (
                    f"{history}\n"
                    f"{prompt}"
                )
            }
        ],
        model="llama3-8b-8192",
    )
    
    return chat_completion.choices[0].message.content
