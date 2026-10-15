from langchain_core.prompts import PromptTemplate
from langchain_ollama.chat_models import ChatOllama
from .MyOutputParser import TextInfoParser
from langchain_core.output_parsers import PydanticOutputParser 
from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv

load_dotenv()

parser = PydanticOutputParser(pydantic_object=TextInfoParser)

prompt = PromptTemplate(
    template="""
        Based on the input given '{user_input}' provide the following details
        1. Count the number of vowels.
        2. Count thr number of consonants.

        Make sure of the following things
        1. The search should be case in-sensitive
        2. List all the vowels and consonants in the end

        {formatting_instructions}
    """,
    input_variables=["user_input"],
    partial_variables={"formatting_instructions": parser.get_format_instructions()}
)   

llm = ChatOllama(model="qwen3:1.7b", reasoning=True, temperature=0)

chain = prompt | llm | parser

def main():
    response = chain.invoke({"user_input": "Kalyan"})
    print(response)