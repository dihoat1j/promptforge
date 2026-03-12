import json
import os
import hashlib
from datetime import datetime
from typing import Dict, List, Optional

class PromptStore:
    """Manages persistence and versioning of prompt templates."""
    
    def __init__(self, base_dir: str = "prompts"):
        self.base_dir = base_dir
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

    def save(self, name: str, template: str, metadata: Dict = None) -> str:
        version_id = hashlib.md5(template.encode()).hexdigest()[:8]
        file_path = os.path.join(self.base_dir, f"{name}_{version_id}.json")
        
        data = {
            "name": name,
            "version": version_id,
            "template": template,
            "metadata": metadata or {},
            "created_at": datetime.now().isoformat()
        }
        
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        
        return version_id

    def load(self, name: str, version: str = "latest") -> Dict:
        files = [f for f in os.listdir(self.base_dir) if f.startswith(name)]
        if not files:
            raise FileNotFoundError(f"No templates found for: {name}")
        
        if version == "latest":
            files.sort(key=lambda x: os.path.getmtime(os.path.join(self.base_dir, x)))
            target = files[-1]
        else:
            target = next((f for f in files if version in f), None)
            if not target:
                raise ValueError(f"Version {version} not found for {name}")

        with open(os.path.join(self.base_dir, target), "r") as f:
            return json.load(f)
