import json


def generate(prompt):

    print("\nLLM RECEIVED PROMPT")

    simulated_response = """
    {
        "themes": [
            "Advisor Experience",
            "Website Experience",
            "Mobile Experience"
        ]
    }
    """

    return json.loads(simulated_response)