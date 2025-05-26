from typing import Optional, Dict, Any

class PhysicsConstants:
    def __init__(self):
        self.constants: Dict[str, Dict[str, Any]] = {
            "c": {
                "name": "Speed of light in vacuum",
                "value": 299792458,
                "unit": "m/s"
            },
            "G": {
                "name": "Gravitational constant",
                "value": 6.67430e-11,
                "unit": "m³/(kg·s²)"
            },
            "h": {
                "name": "Planck constant",
                "value": 6.62607015e-34,
                "unit": "J·s"
            },
            "e": {
                "name": "Elementary charge",
                "value": 1.602176634e-19,
                "unit": "C"
            },
            "me": {
                "name": "Electron mass",
                "value": 9.1093837015e-31,
                "unit": "kg"
            },
            "mp": {
                "name": "Proton mass",
                "value": 1.67262192369e-27,
                "unit": "kg"
            },
            "k": {
                "name": "Boltzmann constant",
                "value": 1.380649e-23,
                "unit": "J/K"
            },
            "ε0": {
                "name": "Vacuum permittivity",
                "value": 8.8541878128e-12,
                "unit": "F/m"
            }
        }
    
    def get_constant(self, symbol: str) -> Optional[Dict[str, Any]]:
        """
        Get information about a physical constant by its symbol
        
        Args:
            symbol (str): The symbol of the constant (e.g., 'c' for speed of light)
        
        Returns:
            Optional[Dict[str, Any]]: Dictionary containing constant information or None if not found
        """
        return self.constants.get(symbol)
    
    def search_constant(self, query: str) -> Optional[Dict[str, Any]]:
        """
        Search for a constant by name or description
        
        Args:
            query (str): Search query (e.g., "speed of light" or "gravitational")
        
        Returns:
            Optional[Dict[str, Any]]: First matching constant or None if not found
        """
        query = query.lower()
        for symbol, data in self.constants.items():
            if query in data["name"].lower():
                return {symbol: data}
        return None
    
    def list_constants(self) -> Dict[str, Dict[str, Any]]:
        """
        Get all available constants
        
        Returns:
            Dict[str, Dict[str, Any]]: Dictionary of all constants
        """
        return self.constants

# Create a singleton instance
constants = PhysicsConstants() 