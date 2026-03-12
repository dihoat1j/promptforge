from typing import List, Dict, Callable
import numpy as np

class Evaluator:
    """Provides tools to score LLM outputs against game-specific metrics."""
    
    @staticmethod
    def length_score(output: str, target_range: tuple) -> float:
        """Scores based on output length (min, max)."""
        length = len(output.split())
        if target_range[0] <= length <= target_range[1]:
            return 1.0
        return 0.5

    @staticmethod
    def keyword_relevance(output: str, keywords: List[str]) -> float:
        """Scores based on presence of key lore or game terms."""
        if not keywords: return 1.0
        count = sum(1 for word in keywords if word.lower() in output.lower())
        return count / len(keywords)

    def run_suite(self, output: str, config: Dict[str, Any]) -> Dict[str, float]:
        results = {}
        if "keywords" in config:
            results["relevance"] = self.keyword_relevance(output, config["keywords"])
        if "length" in config:
            results["length_efficiency"] = self.length_score(output, config["length"])
        return results
