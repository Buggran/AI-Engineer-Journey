import json


def build_theme_prompt(comments):

    comment_text = "\n".join(comments)

    prompt = f"""
You are a Customer Experience Analyst.

Analyze the survey comments below.

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

        ai_response = """
        {
            "themes": [
                "Advisor Experience",
                "Website Experience",
                "Mobile Experience"
            ]
        }
        """

        data = json.loads(ai_response)

        return data

    except Exception as e:

        print(f"Theme extraction failed: {e}")

        return {
            "themes": []
        }