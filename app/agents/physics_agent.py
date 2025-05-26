from typing import Optional, Dict, Any
from ..utils.gemini import gemini_api
from ..tools.constants import constants

class PhysicsAgent:
    def __init__(self):
        self.gemini = gemini_api
        self.constants = constants
    
    def find_relevant_constants(self, text: str) -> Optional[Dict[str, Dict[str, Any]]]:
        """
        Find physics constants that might be relevant to the question
        
        Args:
            text (str): The physics question text
        
        Returns:
            Optional[Dict[str, Dict[str, Any]]]: Dictionary of relevant constants or None
        """
        text = text.lower()
        relevant_constants = {}
        
        # Search through all constants
        for symbol, data in self.constants.list_constants().items():
            if data["name"].lower() in text or symbol.lower() in text:
                relevant_constants[symbol] = data
        
        return relevant_constants if relevant_constants else None
    
    async def process_question(self, question: str) -> str:
        """
        Process a physics question using Gemini API and constants when needed
        
        Args:
            question (str): The physics question to process
        
        Returns:
            str: The answer to the question
        """
        # First, check for relevant constants
        relevant_constants = self.find_relevant_constants(question)
        
        context = """
        You are a helpful physics tutor. Please provide a clear and detailed explanation
        for the following physics question. Include relevant formulas and calculations
        where appropriate.
        """
        
        if relevant_constants:
            # Add constants information to the context
            constants_info = "\nRelevant physical constants:\n"
            for symbol, data in relevant_constants.items():
                constants_info += f"- {data['name']} ({symbol}): {data['value']} {data['unit']}\n"
            context += constants_info
        
        response = await self.gemini.generate_response(question, context)
        
        # If constants were found, append them to the response
        if relevant_constants:
            response += "\n\nRelevant Constants Used:\n"
            for symbol, data in relevant_constants.items():
                response += f"- {data['name']} ({symbol}): {data['value']} {data['unit']}\n"
        
        return response

# Create a singleton instance
physics_agent = PhysicsAgent() 