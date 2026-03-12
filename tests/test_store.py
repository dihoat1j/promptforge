import pytest
import os
import shutil
from promptforge.store import PromptStore

def test_save_and_load():
    store = PromptStore("test_prompts")
    template = "You are a {role}."
    v_id = store.save("npc_base", template)
    
    loaded = store.load("npc_base", v_id)
    assert loaded["template"] == template
    assert loaded["version"] == v_id
    
    shutil.rmtree("test_prompts")
