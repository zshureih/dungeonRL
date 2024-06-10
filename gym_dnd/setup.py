from setuptools import setup, find_packages

setup(
    name="gym_dnd",  # Replace with your project name
    version="0.1",  # Replace with your project version
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
        # You can find them in your requirements.txt file
    ],
    entry_points={
        "console_scripts": [
            "gym_dnd = gym_dnd.src.main:main",  # Replace with your script name and entry point
        ],
    },
    author="Zeyad Shureih",  # Replace with your name
    author_email="zeyad@me.com",  # Replace with your email
    description="Description of your project",  # Replace with your project description
    url="https://github.com/zshureih/dungeonRL",  # Replace with your project URL
)
