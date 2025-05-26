import re
from typing import Optional, Tuple
from ..utils.gemini import gemini_api
from ..tools.calculator import calculator

class MathAgent:
    def __init__(self):
        self.gemini = gemini_api
    
    def extract_calculation(self, text: str) -> Optional[Tuple[str, str]]:
        """
        Extract arithmetic expressions from text
        
        Args:
            text (str): Text containing potential arithmetic expressions
        
        Returns:
            Optional[Tuple[str, str]]: Tuple of (expression, original_text) or None
        """
        # Look for arithmetic expressions like "2 + 2" or "5 * (3 + 2)"
        pattern = r'\b\d+(\s*[\+\-\*\/]\s*\d+\s*[\+\-\*\/\(\)]*\d*)+\b'
        match = re.search(pattern, text)
        if match:
            return match.group(0), text
        return None
    
    async def process_question(self, question: str) -> str:
        """
        Process a math question using Gemini API and calculator when needed
        
        Args:
            question (str): The math question to process
        
        Returns:
            str: The answer to the question
        """
        # First, try to extract any arithmetic calculations
        calc_result = self.extract_calculation(question)
        
        if calc_result:
            expression, _ = calc_result
            result = calculator.evaluate(expression)
            if result is not None:
                # Get explanation from Gemini
                context = f"""
                The arithmetic calculation {expression} = {result}.
                Please explain this calculation step by step.
                """
                explanation = await self.gemini.generate_response(question, context)
                return f"Result: {result}\n\nExplanation: {explanation}"
        
        # If no calculation needed or extraction failed, use Gemini API directly
        context = """
        You are a helpful math tutor. Please provide a clear and detailed explanation
        for the following math question. If the question involves calculations,
        show the steps clearly.
        """
        response = await self.gemini.generate_response(question, context)
        return response

# Create a singleton instance
math_agent = MathAgent() 