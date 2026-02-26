import os
from dotenv import load_dotenv

print("Before load:", os.getenv("ANTHROPIC_API_KEY"))
load_dotenv(dotenv_path=".env")
print("After load:", os.getenv("ANTHROPIC_API_KEY"))