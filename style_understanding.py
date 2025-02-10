from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from config import OPENAI_API_KEY

llm = OpenAI(api_key=OPENAI_API_KEY)

def analyze_style(style_description):
    prompt = PromptTemplate(
        input_variables=["style"],
        template="Describe the key characteristics of {style} fashion style."
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(style=style_description)
