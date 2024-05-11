import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("CHAT_GPT_API_KEY"))
