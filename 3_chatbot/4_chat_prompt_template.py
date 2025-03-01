from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, What is {topic}')
])

prompt = chat_template.invoke({'domain': 'Cricket', 'topic':'Dusra'})

print(prompt)