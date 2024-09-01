import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def chat_response(email_type, purpose_questions, product_content, recipient_content, tone,prompt, history):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an email assistant that generates an email using the inputs including type of outreach email, specific information about the product/ service or individual relevant to the email"
                    "information about the recipient and tone of the email to personalise the email for the user needs"
                    "If the user does not provide the necessary inputs, ask them to fill in the form in the panel to the left and give a clean description of each of the inputs"
                    "##### Inputs #####"
                    f"Email Type to define the structure of email: {email_type}\n"
                    f"{purpose_questions}: {product_content}\n"
                    f"About the email recipient: {recipient_content}\n"
                    f"Tone of Email: {tone}\n"
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
