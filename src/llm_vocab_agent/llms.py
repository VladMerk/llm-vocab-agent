import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY", "")

llm = ChatOpenAI(api_key=SecretStr(openai_key), model="gpt-4o-mini")
