# -*- coding: utf-8 -*-
"""LLMs with RAG

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rwzto4plt-E6awJ7Cnq6KZILc710aKdm
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install -q langchain langchain-nvidia-ai-endpoints gradio
from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os
os.environ["NVIDIA_API_KEY"] = '__insert_api_key___'


ChatNVIDIA.get_available_models()

from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from functools import partial

identity = RunnableLambda(lambda x:x)

def print_and_return(x, preface=""):
    print(f"{preface}{x}")
    return x

rprint0 = RunnableLambda((print_and_return))

rprint1 = RunnableLambda(partial(print_and_return, preface="1: "))

def RPrint(preface=""):
    return RunnableLambda(partial(print_and_return, preface=preface))

chain1 = identity | rprint0
chain1.invoke("Hello World!")
print()

output = (
    chain1           ## Prints "Welcome Home!" & passes "Welcome Home!" onward
    | rprint1        ## Prints "1: Welcome Home!" & passes "Welcome Home!" onward
    | RPrint("2: ")  ## Prints "2: Welcome Home!" & passes "Welcome Home!" onward
).invoke("Welcome Home!")

## output is "Welcome Home!"
print("\nOutput:", output)

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

chat_llm = ChatNVIDIA(model="meta/llama3-8b-instruct", api_key = 'NVIDIA_API_KEY')

prompt = ChatPromptTemplate.from_messages([
    ("system", "Only respond in rhymes"),
    ("user", "{input}")
])

rhyme_chain = prompt | chat_llm | StrOutputParser()

print(rhyme_chain.invoke({"input" : "Tell me about birds!"}))

import requests

headers = {
    "Authorization": f"Bearer {os.environ['NVIDIA_API_KEY']}"
}

response = requests.get("https://api.ngc.nvidia.com/v2/models", headers=headers)  # Replace with the correct endpoint
print(response.status_code, response.text)