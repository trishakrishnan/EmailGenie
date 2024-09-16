# EmailGenie
[![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Langchain](https://img.shields.io/badge/-Langchain-gray)](https://langchain.com/)
[![LLama](https://img.shields.io/badge/-LLama-7932a8?logo=LLama&logoColor=white)](https://llama.ai/)
[![Render](https://img.shields.io/badge/-Render-46E3B7?logo=Render&logoColor=white)](https://render.com/)
[![gROQ](https://img.shields.io/badge/-gROQ-black)](https://groq.com/)
[![Google Sheets API](https://img.shields.io/badge/-Google_Sheets_API-34A853?logo=Google-Sheets&logoColor=white)](https://developers.google.com/sheets/api)
[![Resend](https://img.shields.io/badge/-Resend-FF6F00?logo=mail.ru&logoColor=white)](https://resend.com/)



EmailGenie is an AI-powered tool designed to generate personalized cold outreach emails. The tool leverages a Large Language Model (LLM) to assist users in drafting professional emails tailored to specific use cases such as sales pitches, networking, job inquiries, and event invitations. The goal is to simplify the process of writing outreach emails by guiding the user through key details and crafting an email based on the given inputs.

You can explore this tool in deployment [here]([https://emailgenie.onrender.com/](https://emailgenie-4smc.onrender.com/))


![image](https://github.com/user-attachments/assets/96109bb9-a17c-423f-af54-1435f2cb9e66)  
![image](https://github.com/user-attachments/assets/3dc7a16e-9e99-461e-ba5e-54a05221533b)
![image](https://github.com/user-attachments/assets/0db2fb34-c265-4d80-99ae-81be987e1066)
![image](https://github.com/user-attachments/assets/94955826-982c-4d1e-ac28-f0216182c76c)



## Features
- **Personalized Email Creation**: Choose from different types of emails and answer relevant questions to personalize your outreach email.
- **Review and Edit**: View a draft of the generated email and make any edits or adjustments before sending.
- **Save Templates**: Save the generated email templates for future use.
- **Direct Email Sending**: Send the email directly from the app to your recipient(s).
- **User Profile Data**: Save user information, email types, and templates to Google Sheets for easy access and management.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/trishakrishnan/EmailGenie.git
   ```

2. Navigate to the project directory:
   ```bash
   cd EmailGenie
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

### Step-by-Step Guide
1. **Registration:** Enter your details including name, industry, role, and select the type of email you want to generate.

2. **Personalize Your Email:** Based on the selected email type, answer a set of questions that will be used to personalize your email. The more details you provide, the more tailored the email will be.

3. **Generate Email:** The app will generate a draft of the email. You can review the draft, add further instructions, and regenerate the email if needed.

4. **Send Email:** Preview the email, make final edits, and input the recipient's email address. Then, click "Send" to dispatch the email or save the template for future use.

### Sidebar Navigation

The app uses a sidebar for navigation and instructions. The sidebar contains the following sections:

- **Page Navigation:** Displays the current step of the process (Registration, Personalization, Email Generation, Send Email).
- **Instructions:** Provides a description of the task to be completed at each step.
- **User Profile:** A link to a Google Sheet where user profile data and saved templates are stored.

### Sending and Saving Emails
- **Send Email:** You can send the email directly from the app by providing the recipient's email address.
- **Save Template:** The generated or edited email can be saved to your profile for future use.

## Code Structure

- **`app.py`**: Main application file that manages the Streamlit UI flow and email generation.
- **`emails.py`**: Contains the logic for generating emails based on user inputs.
- **`util_functions.py`**: Includes utility functions for saving user data to Google Sheets, sending emails, and extracting subject lines from email drafts.
- **`config.py`**: Configuration file that stores descriptions and questions for each type of email.
  
## Dependencies

- **Streamlit**: Web application framework used for building the interactive UI.
- **Google Sheets API**: Used for saving user profile data and email templates.
- **Resend API**: Integrated for sending emails directly through the app.
- **JSON**: For handling data serialization.
- **LangChain**: A framework for building applications powered by language models. It handles the interaction between the user inputs and the large language model.
- **Llama3-8b-8192**: A large language model (LLM) with 8 billion parameters, providing sophisticated natural language understanding and generation capabilities.
- **gROQ**: A high-performance inference engine that optimizes the Llama model for efficient and fast processing, ensuring the emails are generated in a timely and resource-efficient manner.
- **Render**: A fully managed cloud platform that automates the deployment and scaling of web applications. The EmailGenie app is hosted on Render to ensure reliable, scalable, and efficient access for users.
- **Resend**: Resend provides a reliable and efficient platform to send emails directly from the application. It's integrated into EmailGenie to handle the dispatch of personalized outreach emails to the recipient(s).









