import re
from typing import Dict, Any

class PromptEngine:
    """Handles logic for injecting variables into templates."""
    
    def __init__(self):
        pass

    def render(self, template: str, variables: Dict[str, Any]) -> str:
        """Simple string interpolation with validation."""
        required_vars = re.findall(r"\{(.*?)\}", template)
        
        for var in required_vars:
            if var not in variables:
                raise KeyError(f"Missing required variable: {var}")
        
        return template.format(**variables)

    def validate_action_space(self, output: str, allowed_actions: list) -> bool:
        """Ensures the LLM output contains valid game actions."""
        # Example: [MOVE: NORTH], [ATTACK: ORC]
        matches = re.findall(r"\[(.*?):(.*?)\]", output)
        if not matches:
            return False
            
        return all(action.strip() in allowed_actions for action, val in matches)
