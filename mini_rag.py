from knowledge_base import knowledge_base

question = "Tell me about advisor"


for chunk in knowledge_base:

    if chunk["topic"] in question.lower():

        print("Retrieved Context:")
        print(chunk["content"])