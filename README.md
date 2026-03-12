# PromptForge

PromptForge is a production-grade prompt engineering toolkit specifically designed for AI-driven game engines and complex multi-agent systems. It bridges the gap between raw LLM completions and structured game logic by providing versioned templates, automated A/B testing, and behavioral evaluation metrics.

## Key Features

*   **Prompt Versioning**: Treat prompts as code with git-like hashing and named aliases.
*   **Agent Personas**: Define and swap behavioral profiles for NPCs and game systems.
*   **A/B Testing**: Run multiple prompt versions through evaluators to determine the most effective narrative or logic path.
*   **Evaluation Metrics**: Build-in support for Sentiment, Coherence, and Goal-Achievement scoring.
*   **Game Engine Integration**: Hooks for state injection and action-space mapping.

## Installation

```bash
pip install promptforge
```

## Quick Start

```python
from promptforge import PromptManager, Evaluator

# Initialize manager
pm = PromptManager(storage_path="./prompts")

# Register a template
pm.create_template(
    name="merchant_dialogue",
    template="You are a {trait} merchant. The player offers you {item}. Respond in character.",
    input_variables=["trait", "item"]
)

# Run an A/B test
results = pm.run_ab_test(
    template_name="merchant_dialogue",
    variants=[{"trait": "grumpy"}, {"trait": "jovial"}],
    inputs={"item": "a rusty sword"},
    iterations=5
)

print(results.summary())
```

## Architecture

PromptForge follows a decoupled architecture where the Prompt Store is isolated from the Execution Engine. This allows you to swap LLM providers or evaluation logic without modifying your game's core NPC systems.

*   **Store**: Handles file-based or DB-based persistence of prompt versions.
*   **Engine**: Manages variable injection and safety filtering.
*   **Judge**: A specialized agent class that scores outputs against defined metrics.

## Contributing

Please see CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
