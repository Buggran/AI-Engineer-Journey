import json
from llm_client import generate


def build_theme_prompt(comments):

    comment_text = "\n".join(comments)

    prompt = f"""
You are a Customer Experience Analyst.

Analyze the survey comments below.

Identify the top customer experience themes.

Return JSON in this format:

{{
    "themes": []
}}

Survey Comments:
{comment_text}
"""

    return prompt


def extract_themes(comments):

    try:

        prompt = build_theme_prompt(comments)

        print("\nPROMPT SENT TO AI:")
        print(prompt)

        # Send prompt to LLM
        ai_response = generate(prompt)

        # Convert JSON string into Python dictionary
        data = json.loads(ai_response)

        # Return structured result
        return data

    except Exception as e:

        print(f"Theme extraction failed: {e}")

        return {
            "themes": []
        }