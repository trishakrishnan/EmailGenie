from langchain.llms.base import LLM
from typing import Optional, List
import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()



# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class GroqLLM(LLM):
    """Custom LLM class to use Groq API within Langchain."""

    def _call(self, prompt: str, stop: Optional[List[str]] = None, system_message: str = None, history: List[dict] = None) -> str:
        """Method to send the prompt, system message, and conversation history to the Groq API and return the response."""
        
        # Prepare the conversation message array
        messages = []
        
        # Include the system message if provided
        if system_message:
            messages.append({"role": "system", "content": system_message})
        
        # Include the conversation history if provided
        if history:
            messages.extend(history)
        
        # Add the user's current prompt
        messages.append({"role": "user", "content": prompt})
        
        try:
            # Call Groq API with the prompt, system message, and history
            chat_completion = client.chat.completions.create(
                messages=messages,
                model="llama3-8b-8192"  # Specify the correct Groq model here
            )
            
            # Extract the response from Groq's API output
            response = chat_completion.choices[0].message.content
            return response
        
        except Exception as e:
            return f"Error in Groq API call: {str(e)}"

    @property
    def _identifying_params(self) -> dict:
        """Return any identifying parameters to identify this LLM."""
        return {}

    @property
    def _llm_type(self) -> str:
        return "groq"
