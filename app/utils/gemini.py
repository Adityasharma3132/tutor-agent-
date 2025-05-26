import os
from typing import Optional, Literal
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiAPI:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')

    async def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """
        Generate a response using the Gemini API
        
        Args:
            prompt (str): The main question or prompt
            context (str, optional): Additional context or instructions
        
        Returns:
            str: Generated response
        """
        try:
            full_prompt = f"{context}\n\n{prompt}" if context else prompt
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"

    async def classify_subject(self, question: str) -> Literal["math", "physics"]:
        """
        Classify whether a question is related to Math or Physics
        
        Args:
            question (str): The question to classify
        
        Returns:
            Literal["math", "physics"]: The classified subject
        """
        prompt = f"""
        You are a subject classifier. Your task is to determine if the following question is related to mathematics or physics.
        
        Rules:
        1. Only respond with either 'math' or 'physics' (lowercase)
        2. If the question contains mathematical calculations or concepts, classify as 'math'
        3. If the question involves physical phenomena, forces, energy, or physical constants, classify as 'physics'
        4. If unclear, default to 'math'
        
        Question: {question}
        
        Classification:
        """
        
        try:
            response = self.model.generate_content(prompt)
            result = response.text.strip().lower()
            
            # Ensure we only return valid responses
            if result in ["math", "physics"]:
                return result
            return "math"  # Default to math if response is invalid
        except Exception as e:
            print(f"Classification error: {str(e)}")
            return "math"  # Default to math on error

# Create a singleton instance
gemini_api = GeminiAPI() 