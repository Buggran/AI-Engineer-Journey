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


def analyze_comments(comments):

    # themes = identify_themes(comments)
    # themes = extract_themes(comments)
    theme_result = extract_themes(comments)
    themes = theme_result["themes"]

    sentiment = calculate_sentiment(comments)

    recommendations = generate_recommendations(
        themes
    )

    return {
        "overall_sentiment": sentiment,
        "themes": themes,
        "recommendations": recommendations
    }