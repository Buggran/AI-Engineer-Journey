from theme_extractor import extract_themes

def identify_themes(comments):

    themes = []

    for comment in comments:

        text = comment.lower()

        if "advisor" in text:
            themes.append("Advisor Experience")

        if "website" in text:
            themes.append("Website Experience")

        if "mobile" in text:
            themes.append("Mobile Experience")

    return list(set(themes))


def calculate_sentiment(comments):

    return "Mixed"


def generate_recommendations(themes):

    recommendations = []

    if "Website Experience" in themes:
        recommendations.append(
            "Improve website usability"
        )

    if "Mobile Experience" in themes:
        recommendations.append(
            "Improve mobile experience"
        )

    return recommendations


import json
from theme_extractor import extract_themes


def analyze_comments(comments):

    theme_result = extract_themes(comments)

    # result = json.loads(theme_result)

    return theme_result
