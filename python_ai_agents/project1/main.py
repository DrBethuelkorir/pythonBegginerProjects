from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm1 = ChatOpenAI(model_name="gpt-4", temperature=0.9)