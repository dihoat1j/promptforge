from typing import List, Dict

class AgentPersona:
    """Represents a game agent's personality traits and behavioral constraints."""
    
    def __init__(self, name: str, traits: List[str], goals: List[str]):
        self.name = name
        self.traits = traits
        self.goals = goals

    def to_context_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "traits": ", ".join(self.traits),
            "goals": "; ".join(self.goals)
        }
