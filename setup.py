from setuptools import setup, find_packages

setup(
    name="promptforge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
    ],
    author="PromptForge Maintainers",
    description="Prompt engineering toolkit for game agents",
    python_requires=">=3.8",
)
