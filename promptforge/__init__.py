from .store import PromptStore
from .engine import PromptEngine
from .evaluator import Evaluator

class PromptForge:
    def __init__(self, storage_path: str = "prompts"):
        self.store = PromptStore(storage_path)
        self.engine = PromptEngine()
        self.eval = Evaluator()

    def create_template(self, name: str, template: str, metadata: dict = None):
        return self.store.save(name, template, metadata)

    def get_prompt(self, name: str, vars: dict, version: str = "latest"):
        data = self.store.load(name, version)
        return self.engine.render(data["template"], vars)
