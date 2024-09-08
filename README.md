# EmailGenie
[![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/-OpenAI-412991?logo=OpenAI&logoColor=white)](https://openai.com/)
[![Langchain](https://img.shields.io/badge/-Langchain-gray)](https://langchain.com/)


EmailGenie is an AI-powered tool designed to generate personalized cold outreach emails. The tool leverages a Large Language Model (LLM) to assist users in drafting professional emails tailored to specific use cases such as sales pitches, networking, job inquiries, and event invitations. The goal is to simplify the process of writing outreach emails by guiding the user through key details and crafting an email based on the given inputs.

![image](https://github.com/user-attachments/assets/99909340-8898-4d32-a3c7-e62e9b2db471)

## Core Features

**1. User-Friendly Interface:**

The interface is built using Streamlit, providing an easy-to-use web application.
Users can input all relevant information through simple fields in the sidebar, including email type, recipient details, sender details, email tone, and the call to action (CTA).

**2. Email Type Options:**

Sales Pitch: Focused on introducing a product or service, showcasing its value to a potential client, and prompting action.
Networking Introduction: A professional connection with no immediate agenda, designed to create long-term connections.
Job Inquiry: Interest in a job role or company, usually requesting a referral or an opportunity to interview.
Event Invitation: Invitations for webinars, conferences, workshops, or networking events.

**3. Interactive User Input:**

Based on the selected email type, the LLM may prompt users for more specific information through a chatbot-like interaction.
EmailGenie asks relevant follow-up questions to ensure a fully personalized email draft.

**4. Customizable Tone & Call to Action:**

Users can select the desired tone of the email: Formal, Casual, or Professional.
The CTA (Call to Action) is entirely customizable, allowing users to dictate what action they want the recipient to take (e.g., scheduling a meeting, signing up for an event, or responding to the email).

**5. Real-Time Chat Feature:**

EmailGenie includes a chat component where users can interact with the tool to refine their email drafts in real time.
The chat feature allows users to submit prompts and receive responses iteratively, refining the email’s content and structure.

**6. Session Management:**

The tool maintains session history so that users can continuously modify their email drafts and view prior interactions, making it easier to track progress.


**7. LLM-Powered Email Generation:**

The backend is powered by a Large Language Model (Groq using Llama 3-8b), which generates personalized email drafts.



## Sample Email

![image](https://github.com/user-attachments/assets/e0c51aa2-886e-4192-a302-1d4a6394e9f3)




