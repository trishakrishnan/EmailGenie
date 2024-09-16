# EmailGenie
[![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/-OpenAI-412991?logo=OpenAI&logoColor=white)](https://openai.com/)
[![Langchain](https://img.shields.io/badge/-Langchain-gray)](https://langchain.com/)
[![LLama](https://img.shields.io/badge/-LLama-7932a8?logo=LLama&logoColor=white)](https://llama.ai/)
[![Perplexity AI](https://img.shields.io/badge/-Perplexity%20AI-232f3e?logo=Perplexity&logoColor=white)](https://www.perplexity.ai/)
[![LinkedIn Scraper](https://img.shields.io/badge/-LinkedIn%20Scraper-0077B5?logo=LinkedIn&logoColor=white)](https://linkedin.com/)


EmailGenie is an AI-powered tool designed to generate personalized cold outreach emails. The tool leverages a Large Language Model (LLM) to assist users in drafting professional emails tailored to specific use cases such as sales pitches, networking, job inquiries, and event invitations. The goal is to simplify the process of writing outreach emails by guiding the user through key details and crafting an email based on the given inputs.

You can explore this tool in deployment [here](https://emailgenie.onrender.com/)

## Features
- **Personalized Email Creation**: Choose from different types of emails and answer relevant questions to personalize your outreach email.
   ![image](https://github.com/user-attachments/assets/99909340-8898-4d32-a3c7-e62e9b2db471)
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








