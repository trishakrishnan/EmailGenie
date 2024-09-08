import requests
import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def linked_in_scraper(linkedin_url:str)-> str:

    url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"
    
    querystring = {"linkedin_url":linkedin_url,
                   "include_skills":"false",
                   "include_certifications":"false",
                   "include_publications":"false",
                   "include_honors":"false",
                   "include_volunteers":"false",
                   "include_projects":"false",
                   "include_patents":"false",
                   "include_courses":"false",
                   "include_organizations":"true",
                   "include_company_public_url":"false"}

    
    payload = {"link": linkedin_url}
    headers = {
	"x-rapidapi-key": os.getenv("RAPID_API_KEY"),
	"x-rapidapi-host": "fresh-linkedin-profile-data.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)

    response_summary = linkedin_summary(response.json())

    return response_summary

## get the about, headline, work experience

def linkedin_summary(json_file:json):

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": ( "You are a useful assistant that summarises the contents of the Linkedin profile data passed on by the user as input\n"
                            "Make sure to include components from the About section and headline of the Linkedin profile among other things while creating the summary"
                            "Don't output anything else apart from the summary of the profile\n"
                            "Highlight the following in the linkedIn profile\n"
                            "1. Current work experience and important projects/ skills used\n"
                            "2. Past experience that is relevant to the current role/ headline description of the person\n"
                            "3. Key highlights about the current company which is relevant to it's industry\n"
                            "4. Any other experience that is relevant to the person and their current role/headline description\n" 
                            )
            },
            {
                "role": "user",
                "content": (
                    f"Summarise this LinkedIn profile data {json_file}"
                )
            }
        ],
        model="llama3-8b-8192",
    )
    
    return chat_completion.choices[0].message.content


    # Use profile_data as input for your LLM summarization




# Function to call Perplexity API
def call_perplexity_api(query):
    # Replace with the actual API URL and your Perplexity API key

    url = "https://api.perplexity.ai/chat/completions"

    api_key = os.getenv("PERPLEXITY_API_KEY")

    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": f"{query}"
            }
        ],
        "temperature": 0.2,
        "top_p": 0.9,
        "search_domain_filter": ["perplexity.ai"],
        "search_recency_filter": "month",
        "top_k": 0,
        "presence_penalty": 0,
        "frequency_penalty": 1
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


    response = requests.request("POST", url, json=payload, headers=headers)

    response_json = json.loads(response.text)
    return response_json['choices'][0]['message']['content']




def sender_recipient_summary(
                                   recipient_linkedin, 
                                   sender_linkedin, 
) -> str : 


    recipient_summary = linked_in_scraper(recipient_linkedin)
    sender_summary = linked_in_scraper(sender_linkedin)


    return recipient_summary, sender_summary


def job_description_summary(job_role, 
                                   job_description_link,
                                   job_company,
                                   sender_name,
                                   sender_summary,
) -> str : 


    job_query = f"""{job_role},{job_company},{job_description_link},Applicant: {sender_name},{sender_summary}
    Based on job details and link page above, give the following details about the role\n
    1. What are the key roles and responsibilities and how are these relevant to the applicants experience\n
    2. What are the skills required for this role and which of these are \n
    3. What experience of the applicant will make them a good fit for this role\n
    """

    job_summary = call_perplexity_api(job_query)


    return job_summary


def product_summary(product_name, 
                                   product_website,
                                   recipient_summary
) -> str : 


    product_query = f""" {product_name},{product_website}, {recipient_summary}
    Based on their details and link page above, give the following details about {product_name}\n
    1. What are the key features of the product\n
    2. What is the intended audience for this feature\n
    3. What pain points of the user does this product solve\n
    4. What are the key benefits of this product\n
    """

    product_summary = call_perplexity_api(product_query)

    return product_summary


def event_summary(event_name, event_link,recipient_summary) -> str : 

    event_query = f""" {event_name},{event_link},Invitee details: {recipient_summary},
    Based on the event page details and link page above, give the following summary\n
    1. Name, place, date, timing of the event \n\
    2. What is the event about and who else would be attending the event
    3. Key agenda items of the event like speakers, workshops, activities etc.\n
    4. Top reasons why the person invited (invitee) would be interested to attend the event \n
    """
    event_summary = call_perplexity_api(event_query)

    return event_summary



js = {'data': {'about': "Passionate about everything machine learning and AI with experience in orchestrating data science based solutions for companies like Deliveroo and United Airlines.\n\nI love helping professionals globally, especially in transitioning from analytics to data science and navigating career shifts across borders (having made the leap from India to the UK myself!) I also extend mentorship in interview preparation, CV reviews, and general career advice—here to guide you every step of the way 😊.\n\nAs a committed advocate for diversity in tech, I'm always open to discussing my experiences as a woman in the industry. If you're curious or seeking insights, let's have a chat!\n\nAlways looking for impactful and thought provoking problems to solve. Inquisitive and eager to learn something new each day!\n\nLink to book video chat in the bio\nFor any further queries you can reach me on  - trisha.krishnan97@gmail.com", 'certifications': [], 'city': '', 'company': 'Trainline', 'company_domain': 'trainline.com', 'company_employee_range': '1001-5000', 'company_industry': 'Software Development', 'company_linkedin_url': 'https://www.linkedin.com/company/trainline', 'company_logo_url': 'https://media.licdn.com/dms/image/v2/D4E0BAQHKxehu-kchgw/company-logo_400_400/company-logo_400_400/0/1720797638016/trainline_logo?e=1733961600&v=beta&t=Mr7Avx7utoyvEuyrDwnUXiLCwK2aLUHmmhDNPE8wbJQ', 'company_website': 'https://www.trainline.com/?utm_source=linkedin&utm_medium=social&utm_campaign=profilepage', 'company_year_founded': 1997, 'connection_count': 867, 'country': 'United Kingdom', 'current_company_join_month': 1, 'current_company_join_year': 2024, 'educations': [{'activities': '', 'date_range': '2020 - 2021', 'degree': 'Post Graduate Program', 'end_month': '', 'end_year': 2021, 'field_of_study': 'Artificial Intelligence and Machine Learning', 'school': 'Great Learning', 'school_id': '9282020', 'school_linkedin_url': 'https://www.linkedin.com/company/9282020/', 'school_logo_url': 'https://media.licdn.com/dms/image/v2/C560BAQF40lFj20_wxA/company-logo_200_200/company-logo_200_200/0/1630649587188/great_learning_logo?e=1733961600&v=beta&t=OVTqI18q2TZiEpfGg-QBANzqHRE0yTkExiPpzyhoJ4s', 'start_month': '', 'start_year': 2020}, {'activities': 'Activities and societies: General Secretary of Department of Statistics(2016-2017), LSR Western Music Society, National Sports Organisation, Tarang 2016 Informals team, Tarang 2016, Moments 2016 Publicity Team, Moments 2016 Informals Team', 'date_range': '2015 - 2018', 'degree': "Bachelor's degree", 'end_month': '', 'end_year': 2018, 'field_of_study': 'Statistics', 'school': 'Lady Shri Ram College For Women', 'school_id': '5427901', 'school_linkedin_url': 'https://www.linkedin.com/company/5427901/', 'school_logo_url': 'https://media.licdn.com/dms/image/v2/C4D0BAQEd-hGKsa4aSA/company-logo_200_200/company-logo_200_200/0/1631352402194?e=1733961600&v=beta&t=wAbpa2Q6o4qGjjd_mV7PPbwctAPHvwnhFZRbSC1uSVc', 'start_month': '', 'start_year': 2015}, {'activities': '', 'date_range': '2011 - 2015', 'degree': 'High School', 'end_month': '', 'end_year': 2015, 'field_of_study': '', 'school': 'The Shri Ram School, Aravali', 'school_id': '', 'school_linkedin_url': '', 'school_logo_url': '', 'start_month': '', 'start_year': 2011}, {'activities': '', 'date_range': '2004 - 2011', 'degree': '', 'end_month': '', 'end_year': 2011, 'field_of_study': '', 'school': 'The Heritage School, Gurgaon', 'school_id': '', 'school_linkedin_url': '', 'school_logo_url': '', 'start_month': '', 'start_year': 2004}], 'email': 'trisha.krishnan97@gmail.com', 'experiences': [{'company': 'Trainline', 'company_id': '96955', 'company_linkedin_url': 'https://www.linkedin.com/company/96955', 'company_logo_url': 'https://media.licdn.com/dms/image/v2/D4E0BAQHKxehu-kchgw/company-logo_200_200/company-logo_200_200/0/1720797638016/trainline_logo?e=1733961600&v=beta&t=iOvhpL6x3yfwFrOunyBu1GCIPLkRTUMDY0PkHmfoRrg', 'date_range': 'Jan 2024 - Present', 'description': '', 'duration': '9 mos', 'end_month': '', 'end_year': '', 'is_current': True, 'job_type': '', 'location': 'London, England, United Kingdom', 'skills': '', 'start_month': 1, 'start_year': 2024, 'title': 'Senior Machine Learning Engineer'}, {'company': 'Deliveroo', 'company_id': '2837535', 'company_linkedin_url': 'https://www.linkedin.com/company/2837535', 'company_logo_url': 'https://media.licdn.com/dms/image/v2/C4E0BAQHIgRVMCL9wqA/company-logo_200_200/company-logo_200_200/0/1663666898712/deliveroo_logo?e=1733961600&v=beta&t=yBHN1sdNDP7-YDf3KJj1VzVeGU1JoxKeIUqqZD_riYA', 'date_range': 'Mar 2022 - Jan 2024', 'description': '- Developed an ML solution to predict lifetime value for customers, improving accuracy of existing solution and deployed an end-to-end production pipeline to optimise spend \n- Developed a framework to measure the long-term financial value for B2B marketing leads which was used to set spend targets for future campaigns', 'duration': '1 yr 11 mos', 'end_month': 1, 'end_year': 2024, 'is_current': False, 'job_type': 'Full-time', 'location': 'London, England, United Kingdom', 'skills': 'Argo · Exploratory Data Analysis · Continuous Integration and Continuous Delivery (CI/CD) · Looker (Software) · Python (Programming Language) · Hypothesis Testing · Machine Learning · Amazon Web Services (AWS) · Experimental Design · Communication', 'start_month': 3, 'start_year': 2022, 'title': 'Data Scientist'}, {'company': 'United Airlines', 'company_id': '2380', 'company_linkedin_url': 'https://www.linkedin.com/company/2380', 'company_logo_url': 'https://media.licdn.com/dms/image/v2/C560BAQE2FQDbKOgfJQ/company-logo_200_200/company-logo_200_200/0/1652708216669/united_airlines_logo?e=1733961600&v=beta&t=qvM8582z_ECLcubvxAU4rf1GyrGanUuGdflRhjNpy6w', 'date_range': 'Apr 2021 - Feb 2022', 'description': "- Building an ML based solution to recommend the 'next best message' to show to customers and deploying it on web and app platforms to improve customer experience throughout the travel journey Analyst Data Scientist", 'duration': '11 mos', 'end_month': 2, 'end_year': 2022, 'is_current': False, 'job_type': '', 'location': 'Gurugram, Haryana, India', 'skills': 'Cross-functional Collaborations · Exploratory Data Analysis · SQL · Recommender Systems · Python (Programming Language) · Predictive Modeling · Amazon Web Services (AWS) · Communication', 'start_month': 4, 'start_year': 2021, 'title': 'Analyst Data Scientist'}, {'company': 'United Airlines', 'company_id': '2380', 'company_linkedin_url': 'https://www.linkedin.com/company/2380', 'company_logo_url': 'https://media.licdn.com/dms/image/v2/C560BAQE2FQDbKOgfJQ/company-logo_200_200/company-logo_200_200/0/1652708216669/united_airlines_logo?e=1733961600&v=beta&t=qvM8582z_ECLcubvxAU4rf1GyrGanUuGdflRhjNpy6w', 'date_range': 'Jan 2020 - Apr 2021', 'description': "- Awarded Analyst of the Quarter (Q2'20) for the contribution to the loyalty program initiatives\n- Developed a suite of customer propensity models for United loyalty program credit cards, used to target audience for marketing campaigns\n-  Developed an internal A/B testing product using control matching technique (k-NN), to simplify and streamline campaign performance measurement across the company Associate Data Scientist Jan 2020 - Apr 2021 · 1 yr 4 mos", 'duration': '1 yr 4 mos', 'end_month': 4, 'end_year': 2021, 'is_current': False, 'job_type': '', 'location': 'Gurgaon, India', 'skills': 'Exploratory Data Analysis · JavaScript · SQL · Machine Learning · Data Robot · Propensity Modelling · PySpark', 'start_month': 1, 'start_year': 2020, 'title': 'Associate Data Scientist'}, {'company': 'United Airlines', 'company_id': '2380', 'company_linkedin_url': 'https://www.linkedin.com/company/2380', 'company_logo_url': 'https://media.licdn.com/dms/image/v2/C560BAQE2FQDbKOgfJQ/company-logo_200_200/company-logo_200_200/0/1652708216669/united_airlines_logo?e=1733961600&v=beta&t=qvM8582z_ECLcubvxAU4rf1GyrGanUuGdflRhjNpy6w', 'date_range': 'Jun 2018 - Jan 2020', 'description': '- Engineered large dimensionality datasets and developed a model to predict competitor airline fares and support demand forecasting decisions\n- Performed complex analysis on competitor airlines to augment pricing strategies\n- Developed an automated email report and dashboard to monitor data quality from a 3rd party vendor which saved the company vendor cost and reduced complaint response time Associate Analyst- Enterprise Analytics Jun 2018 - Jan 2020 · 1 yr 8 mos', 'duration': '1 yr 8 mos', 'end_month': 1, 'end_year': 2020, 'is_current': False, 'job_type': '', 'location': 'Gurgaon, India', 'skills': 'SQL · Spotfire · Data Visualization · Python (Programming Language) · Data Analytics · Data Analysis · Amazon Web Services (AWS) · Predictive Analytics', 'start_month': 6, 'start_year': 2018, 'title': 'Associate Analyst- Enterprise Analytics'}, {'company': 'JSW', 'company_id': '32884', 'company_linkedin_url': 'https://www.linkedin.com/company/32884', 'company_logo_url': 'https://media.licdn.com/dms/image/v2/C510BAQG497L93uhyQA/company-logo_200_200/company-logo_200_200/0/1630614041519/jswgroup_logo?e=1733961600&v=beta&t=HMPRxYkrNuDi-FQTdhobOtifzOBOhPAQAysNgQqBusE', 'date_range': 'May 2017 - Jul 2017', 'description': '', 'duration': '3 mos', 'end_month': 7, 'end_year': 2017, 'is_current': False, 'job_type': 'Internship', 'location': '', 'skills': '', 'start_month': 5, 'start_year': 2017, 'title': 'Summer Intern'}, {'company': 'Deloitte India', 'company_id': '1038', 'company_linkedin_url': 'https://www.linkedin.com/company/1038', 'company_logo_url': 'https://media.licdn.com/dms/image/v2/C560BAQGNtpblgQpJoQ/company-logo_200_200/company-logo_200_200/0/1662120928214/deloitte_logo?e=1733961600&v=beta&t=sc1za0u1W2LXacJW1wJ_ukHRlVwqvpR79GTv8CWbHgw', 'date_range': 'May 2016 - Jun 2016', 'description': '', 'duration': '2 mos', 'end_month': 6, 'end_year': 2016, 'is_current': False, 'job_type': '', 'location': '', 'skills': '', 'start_month': 5, 'start_year': 2016, 'title': 'Summer Intern'}, {'company': 'Wadi.com', 'company_id': '9340977', 'company_linkedin_url': 'https://www.linkedin.com/company/9340977', 'company_logo_url': 'https://media.licdn.com/dms/image/v2/C4D0BAQEDSWaSHXJDJg/company-logo_200_200/company-logo_200_200/0/1631312547707?e=1733961600&v=beta&t=6osJ_sfIRhJ0RTW-CUsu6y_riJy98A-Oi4iD5bIMi5c', 'date_range': 'Dec 2015 - Jan 2016', 'description': '', 'duration': '2 mos', 'end_month': 1, 'end_year': 2016, 'is_current': False, 'job_type': '', 'location': '', 'skills': '', 'start_month': 12, 'start_year': 2015, 'title': 'Customer Relationship Management Intern'}, {'company': 'JOSH Talks', 'company_id': '6555271', 'company_linkedin_url': 'https://www.linkedin.com/company/6555271', 'company_logo_url': 'https://media.licdn.com/dms/image/v2/C4D0BAQEhXz8cBVn4Vw/company-logo_200_200/company-logo_200_200/0/1672770926771/joshtalks_logo?e=1733961600&v=beta&t=_k0UaC53BBFCqDTHKUHFsiMhxTMwGtJwrw3K3fwQmyo', 'date_range': 'Sep 2015 - Nov 2015', 'description': '', 'duration': '3 mos', 'end_month': 11, 'end_year': 2015, 'is_current': False, 'job_type': '', 'location': '', 'skills': '', 'start_month': 9, 'start_year': 2015, 'title': 'Core Team Member'}], 'first_name': 'Trisha', 'follower_count': 1482, 'full_name': 'Trisha Krishnan', 'headline': 'Senior Machine Learning Engineer @ Trainline | AI enthusiast | Mentorship | Women in Tech', 'hq_city': 'London', 'hq_country': 'GB', 'hq_region': '', 'job_title': 'Senior Machine Learning Engineer', 'languages': 'English, French, Hindi, Spanish', 'last_name': 'Krishnan', 'linkedin_url': 'https://www.linkedin.com/in/trishakrishnan/', 'location': 'United Kingdom', 'organizations': [], 'phone': '', 'profile_id': '498710972', 'profile_image_url': 'https://media.licdn.com/dms/image/v2/C5103AQGTpPWyICnAEQ/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1516849740181?e=1730937600&v=beta&t=rF8tn5ztMLTItpaoZYRqPu9Yu2k0SpUmnnhnnAAVTEc', 'public_id': 'trishakrishnan', 'school': 'Great Learning', 'state': '', 'urn': 'ACoAAB25ubwBsSxrtpPf0_fRQ4v1eNPviBbKyMI'}, 'message': 'ok'}


print(linkedin_summary(js))