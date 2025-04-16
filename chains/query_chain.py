# chains/query_chain.py
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

query_prompt_template = """
You are a data analyst. Based on the business goal: "{goal}", generate a list of 4 specific sub-questions 
that should be answered using SQL queries to support this goal. 

Use the metadata below for context.

Metadata:
{metadata}

ONLY return a JSON array. 
Do not include any markdown formatting (Ex: ```json) or text outside the array (```json, ```). 
Use the below format:

[
  {{
    "question": "string - the sub question",
    "purpose": "string - why this question matters"
  }},
  ...
]

"""

prompt = PromptTemplate(
    input_variables=["goal", "metadata"],
    template=query_prompt_template
)

llm = ChatOpenAI(model="gpt-4o")

# ✅ RunnableSequence replaces LLMChain
query_chain = prompt | llm
