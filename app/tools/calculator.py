from typing import Union, Optional

class Calculator:
    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> float:
        return float(a + b)
    
    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> float:
        return float(a - b)
    
    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> float:
        return float(a * b)
    
    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
        try:
            if b == 0:
                raise ValueError("Division by zero is not allowed")
            return float(a / b)
        except ValueError as e:
            print(f"Error: {str(e)}")
            return None
    
    @staticmethod
    def evaluate(expression: str) -> Optional[float]:
        """
        Safely evaluate a simple arithmetic expression
        
        Args:
            expression (str): A simple arithmetic expression (e.g., "2 + 3 * 4")
        
        Returns:
            Optional[float]: Result of the evaluation, or None if invalid
        """
        try:
            # Only allow basic arithmetic operations and numbers
            allowed_chars = set("0123456789.+-*/() ")
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Invalid characters in expression")
            
            # Use eval() safely with only arithmetic operations
            result = eval(expression, {"__builtins__": {}})
            return float(result)
        except Exception as e:
            print(f"Error evaluating expression: {str(e)}")
            return None

# Create a singleton instance
calculator = Calculator() 