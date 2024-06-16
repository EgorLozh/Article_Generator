import os
from dotenv import load_dotenv

load_dotenv()
LLAMA_API_TOKEN = os.getenv("LLAMA_API_TOKEN")
