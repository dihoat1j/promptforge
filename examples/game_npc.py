from promptforge import PromptForge
from promptforge.agent import AgentPersona

def main():
    forge = PromptForge(storage_path="example_prompts")
    
    # Define an NPC Persona
    blacksmith = AgentPersona(
        name="Thrain",
        traits=["stern", "honest", "skilled"],
        goals=["sell weapons", "protect the town"]
    )
    
    # Create template
    forge.create_template(
        "conversation", 
        "Name: {name}\nTraits: {traits}\nGoal: {goals}\nPlayer says: {message}"
    )
    
    # Render for game use
    prompt = forge.get_prompt(
        "conversation",
        {**blacksmith.to_context_dict(), "message": "Give me a discount!"}
    )
    
    print("--- Generated Prompt ---")
    print(prompt)

if __name__ == "__main__":
    main()
