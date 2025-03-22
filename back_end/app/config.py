import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.GENAI_API_KEY = os.getenv("GENAI_API_KEY")
        if not self.GENAI_API_KEY:
            raise ValueError(
                "GENNAI_API_KEY is not set in the environment variables. "
                "Please set it in your .env file or system environment."
            )
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        if not self.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY is not set in the environment variables. "
                "Please set it in your .env file or system environment."
            )

# Instantiate config to validate the key at runtime
try:
    config = Config()
except ValueError as e:
    print(f"Configuration Error: {e}")
