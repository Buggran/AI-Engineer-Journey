import json

from llm_client import generate


def build_theme_prompt(comments):

    comment_text = "\n".join(comments)

    prompt = f"""
        You are a Customer Experience analyst.

        Analyze these survey comments.

        Return ONLY valid JSON.

        Comments:
        {comments}

        Required JSON format:

        {{
            "overall_sentiment": "",
            "theme_count": 0,
            "positive_themes": [],
            "negative_themes": [],
            "themes": [
                {{
                    "theme": "",
                    "sentiment": "",
                    "evidence": []
                }}
            ],
            "recommendations": []
        }}
"""


    return prompt


def extract_themes(comments):

    prompt = build_theme_prompt(comments)

    print("\nPROMPT SENT TO AI:\n")

    response_text = generate(prompt)

    print(response_text)

    data = json.loads(response_text)

    return data