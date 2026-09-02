from agent_tools import (
    identify_themes,
    calculate_sentiment,
    generate_recommendations
)


def survey_agent():

    print("Step 1: Identifying themes...")
    themes = identify_themes()

    print("Step 2: Calculating sentiment...")
    sentiment = calculate_sentiment()

    print("Step 3: Generating recommendations...")
    recommendations = generate_recommendations()

    result = {
        "themes": themes,
        "sentiment": sentiment,
        "recommendations": recommendations
    }

    return result


output = survey_agent()

print("\nFinal Output:")
print(output)