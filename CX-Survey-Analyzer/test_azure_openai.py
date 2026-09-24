import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")


print("KEY:", "present" if api_key else "missing")
print("ENDPOINT:", "present" if endpoint else "missing")
print("DEPLOYMENT:", deployment_name)


if not api_key:
    raise ValueError(
        "AZURE_OPENAI_API_KEY is missing from the .env file."
    )

if not endpoint:
    raise ValueError(
        "AZURE_OPENAI_ENDPOINT is missing from the .env file."
    )

if not deployment_name:
    raise ValueError(
        "AZURE_OPENAI_DEPLOYMENT is missing from the .env file."
    )


client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)


response = client.responses.create(
    model=deployment_name,
    input="Say hello to Jasman and confirm that Azure OpenAI is connected."
)


print("\nMODEL RESPONSE:")
print(response.output_text)