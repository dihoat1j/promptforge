import json

class HistoryManager:
    """Tracks prompt execution history for auditing game sessions."""
    
    def __init__(self, log_path: str = "logs/history.jsonl"):
        self.log_path = log_path

    def log_interaction(self, prompt_id: str, inputs: dict, response: str):
        entry = {
            "prompt_id": prompt_id,
            "inputs": inputs,
            "response": response
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
