from typing import Literal
from ..utils.gemini import gemini_api
from .math_agent import math_agent
from .physics_agent import physics_agent

class TutorAgent:
    def __init__(self):
        self.gemini = gemini_api
        self.math_agent = math_agent
        self.physics_agent = physics_agent
    
    async def classify_subject(self, question: str) -> Literal["math", "physics"]:
        """
        Determine whether the question is related to math or physics
        
        Args:
            question (str): The question to classify
        
        Returns:
            Literal["math", "physics"]: The classified subject
        """
        try:
            return await self.gemini.classify_subject(question)
        except Exception as e:
            print(f"Classification error in TutorAgent: {str(e)}")
            # Default to math if classification fails
            return "math"
    
    async def process_question(self, question: str) -> str:
        """
        Process a question by routing it to the appropriate subject agent
        
        Args:
            question (str): The question to process
        
        Returns:
            str: The answer from the appropriate agent
        """
        try:
            # First, classify the subject
            subject = await self.classify_subject(question)
            
            # Route to appropriate agent
            if subject == "math":
                return await self.math_agent.process_question(question)
            elif subject == "physics":
                return await self.physics_agent.process_question(question)
            else:
                # This should never happen due to the Literal type, but just in case
                print(f"Unexpected subject classification: {subject}")
                return await self.math_agent.process_question(question)
                
        except Exception as e:
            error_msg = str(e)
            print(f"Error processing question: {error_msg}")
            return f"I apologize, but I encountered an error while processing your question. Please try rephrasing it or ask another question. Error: {error_msg}"

# Create a singleton instance
tutor_agent = TutorAgent() 