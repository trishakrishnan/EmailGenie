from custom_groq_llm import GroqLLM  # Use OpenAI or relevant LLM connector
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import email_prompt_template
from util_functions import  extract_email_content
# Initialize the LLM 
llm = GroqLLM()  



# Function to handle API processing
def generate_email(name, industry, role, email_type,answers, additional_inputs):
    """
    This function takes user inputs and calls the Groq API using Langchain to generate email drafts.
    :param name: User's name
    :param industry: Industry information
    :param role: User's role
    :param email_type: The type of email to generate
    :param answers: Specific answers related to the email type
    :param additional_inputs: Additional instructions or modifications input by the user
    :return: One email as a list
    """
    # Set up prompt template and Langchain chain
    prompt = PromptTemplate(
        input_variables=["name", "industry", "role", "email_type", "answers","additional_inputs"],
        template=email_prompt_template,
    )

    # Langchain chain for generating emails
    email_chain = LLMChain(llm=llm, prompt=prompt)

    # Call the chain with user inputs
    response = email_chain.run({
        "name": name,
        "industry": industry,
        "role": role,
        "email_type": email_type,
        "answers": answers,
        "additional_inputs": additional_inputs
    })

    email = extract_email_content(response)

    return email