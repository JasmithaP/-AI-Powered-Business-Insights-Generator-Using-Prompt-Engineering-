import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

def generate_insights(prompt):
    chat = ChatOpenAI(temperature=0.5, model_name="gpt-4", openai_api_key=os.getenv("OPENAI_API_KEY"))
    messages = [HumanMessage(content=prompt)]
    response = chat(messages)
    return response.content
