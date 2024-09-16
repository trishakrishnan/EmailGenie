# Define email type descriptions and questions
email_type_description = {
    "Sales Pitch": "A sales pitch email is designed to introduce your product or service to a potential client, highlighting its value and encouraging them to take action, such as scheduling a meeting or making a purchase.",
    "Networking Introduction": "A networking introduction email is used to establish a professional connection with someone in your industry or related field, with no immediate agenda other than to connect.",
    "Job Enquiry": "A job inquiry email is sent to express interest in working with a company, for a specific role or in general. Many times this involves asking for a referral for a specific job opening.",
    "Event Invitation": "An event invitation email is used to invite someone to a specific event, whether it's a webinar, conference, workshop, or networking event. The focus is on providing key event details and emphasizing the value of attending."
}

email_type_questions = {
    'Sales Pitch': """
    1. What product or service are you pitching?
    2. Who is your target recipient (company or individual) and what specific problem does your product/service solve for this recipient?
    3. What's your value proposition (e.g., save time, reduce costs, increase revenue)?
    4. What is the desired action you want the recipient to take (e.g., schedule a call, demo, etc.)?
    Optional: Include any personalization factors (e.g., have you met the recipient before, how did you come across their company?).
    """,

    'Networking Introduction': """
    1. What is your reason for reaching out (e.g. Are you looking for advice, collaboration, mentorship, or something else?)?
    2. Who is the recipient, and what is their role or profession?
    3. Is there a mutual connection you would like to mention? Do you have any shared interests, events, or groups that can be used to build rapport?
    4. What's the desired outcome of this email (e.g., a meeting, call, or introduction to someone else)?
    Optional: Mention any specific accomplishments or recent achievements of the recipient that caught your attention.
    """,

    'Job Enquiry': """
    1. Are you applying for a specific job position, or is this a general inquiry?
    2. What's the name of the company, and what about this company or job opportunity appeals to you?
    3. Can you describe your relevant experience and skills that make you a good fit for the company/position?
    4. Are there specific projects or accomplishments that you want to highlight?
    5. What are you hoping to achieve with this email (e.g., an interview, information about openings, advice)?
    """,

    'Event Invitation': """
    1. What is the name of the event? When and where is the event happening (date, time, location)?
    2. What's the purpose of the event (e.g., networking, product launch, conference)?
    3. Who is the target audience for this event?
    4. Can you highlight any special guests, speakers, or activities?
    5. What's the desired action (e.g., RSVP, register, share with their network)?
    """
}



# Create a prompt template for generating emails
email_prompt_template = """
You are a professional email generator. Given the following details, generate 1 versions of a cold email:
- Email Type: {email_type}
- Email Recipient, Purpose and other Answers: {answers}
- Additional Inputs: {additional_inputs}

Please generate 1 email, around 100-150 words. 
The output should only have the email and no other text.
Keep placeholders for names of the recipient

Output Structure:

Subject: 

Hi <name>,
<Email body>

<Salutation>, 
"""
