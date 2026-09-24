import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)


def generate(prompt):

    response = client.responses.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        input=prompt
    )

    print("\nPROMPT SENT TO AI:")
    print(prompt)

    response_text = response.output[0].content[0].text

    print("\nAI RESPONSE:")
    print(response_text)

    return response_text
