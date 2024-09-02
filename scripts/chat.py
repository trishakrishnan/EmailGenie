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
                    "information about the recipient and tone of the email to personalise the email for the user needs\n"
                    "##### Inputs #####\n"
                    f"Email Type to define the structure of email: {email_type}\n"
                    f"{purpose_questions}: {product_content}\n"
                    f"About the email recipient: {recipient_content}\n"
                    f"Tone of Email: {tone}\n"
                    "### Key things to keep in mind while drafting the email\n"
                    "1. Don't assume a name or gender for the recipient or sender unless stated in the imputs - use placeholders instead\n"
                    "2. Have a strong Introduction: A strong statement or question that addresses the prospect's pain point is a good way to start a cold email.\n"
                    "3. Have a value proposition: A benefit-oriented value proposition that highlights the benefits of your product or service.\n"
                    "4. Have a call to action: A soft call to action is a component of a cold email.\n"
                    "5. The email should be between 50-125 words long, or about 5-15 lines of text.\n"
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
