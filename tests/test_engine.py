import pytest
from promptforge.engine import PromptEngine

def test_render_valid_vars():
    engine = PromptEngine()
    template = "Hello {name}, welcome to {place}."
    vars = {"name": "Hero", "place": "Aria"}
    assert engine.render(template, vars) == "Hello Hero, welcome to Aria."

def test_render_missing_vars():
    engine = PromptEngine()
    template = "Hello {name}"
    with pytest.raises(KeyError):
        engine.render(template, {})
