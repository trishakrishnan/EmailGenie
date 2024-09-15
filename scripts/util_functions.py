import gspread
from google.oauth2.service_account import Credentials
import re
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import os
import resend


load_dotenv()


# Google Sheets Integration
def add_user_to_gsheet(name, industry, role, email_type):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = Credentials.from_service_account_file('credentials.json', scopes=scope)
    client = gspread.authorize(creds)
    sheet = client.open('EmailGenie_users_records').sheet1  # The name of your Google Sheet
    sheet.append_row([name, industry, role, email_type])



def update_user_on_gsheet(name, industry, role, email_type, column_name, new_value):
    # Define the scope for accessing Google Sheets and Google Drive
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    
    # Load credentials from the credentials file
    creds = Credentials.from_service_account_file('credentials.json', scopes=scope)
    
    # Authorize the client using the credentials
    client = gspread.authorize(creds)
    
    # Open the Google Sheet by name and select the first sheet (sheet1)
    sheet = client.open('EmailGenie_users_records').sheet1
    
    try:
        # Get all the data in the sheet (excluding headers)
        all_data = sheet.get_all_records()
        
        # Get the header row to map column names to indices
        header_row = sheet.row_values(1)
        
        # Check if the target column exists
        if column_name not in header_row:
            print(f"Column '{column_name}' not found in the sheet.")
            return
        
        # Get column indices for 'name', 'industry', 'role', 'email_type', and the target column

        target_col_index = header_row.index(column_name)
        
        # Loop through the data and find rows that match 'name', 'industry', 'role', and 'email_type'
        rows_to_update = []
        for idx, row_data in enumerate(all_data, start=2):  # Start at row 2 (data row)
            if (row_data['Name'] == name and
                row_data['Industry'] == industry and
                row_data['Role'] == role and
                row_data['EmailType'] == email_type):
                rows_to_update.append(idx)
        
        if not rows_to_update:
            print(f"No matching rows found for the specified criteria.")
            return
        
        # Update the target column for each matching row
        for row_number in rows_to_update:
            sheet.update_cell(row_number, target_col_index + 1, new_value)  # +1 for 1-based indexing
            print(f"Updated {column_name} for {name} in row {row_number} successfully.")
    
    except gspread.exceptions.GSpreadException as e:
        print(f"An error occurred: {e}")



def extract_email_content(text):
    # Define a pattern for the start of the email (from 'Subject:')
    subject_pattern = r"Subject:.*"  # Start capturing from 'Subject:'
    
    # Find the portion starting from 'Subject'
    subject_match = re.search(subject_pattern, text, re.DOTALL)
    
    # If the 'Subject:' line is found, extract the portion of the text from there onward
    if subject_match:
        start_idx = subject_match.start()
        return text[start_idx:].strip()  # Extract the email from 'Subject' and strip any excess whitespace
    else:
        return "Subject line not found in the text"


def extract_subject_line_email_body(text):
    # Define a pattern to capture the subject line after 'Subject:'
    subject_pattern = r"Subject:\s*(.*)"  # Captures everything after 'Subject:'
    
    # Search for the subject line in the text
    subject_match = re.search(subject_pattern, text)
    
    # If the 'Subject:' line is found, return the subject content
    if subject_match:
        body_start_idx = subject_match.end()
        email_body = text[body_start_idx:].strip()
        subject = subject_match.group(1).strip()
        return subject, email_body  # Return the subject without leading/trailing spaces
    else:
        return "No subject line found, could not extract email body."




def send_email_via_resend(sender_email, recipient_email, subject, body):
    
    resend.api_key = os.environ["RESEND_API_KEY"]

    params: resend.Emails.SendParams = {
    "from": sender_email,
    "to": [recipient_email],
    "subject": subject,
    "text": body,
}

    email = resend.Emails.send(params)
    return  email