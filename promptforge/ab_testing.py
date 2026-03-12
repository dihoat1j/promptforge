from typing import List, Dict
import random

class ABTester:
    """Runs A/B tests between different prompt versions."""
    
    def __init__(self, forge_instance):
        self.forge = forge_instance

    def compare(self, template_name: str, variants: List[str], input_data: Dict):
        results = {}
        for version in variants:
            prompt = self.forge.get_prompt(template_name, input_data, version=version)
            # In a real scenario, you'd call an LLM here
            # For this mock, we simulate results
            results[version] = {
                "prompt": prompt,
                "token_estimate": len(prompt) // 4
            }
        return results
