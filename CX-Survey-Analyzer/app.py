# import json

# from survey_comments import comments
# from analyzer import analyze_comments

# result = analyze_comments(comments)

# print(result)

# with open("output.json", "w") as file:
#     json.dump(result, file, indent=4)

# print("\nResults saved to output.json")

# from csv_reader import get_comments
# from analyzer import analyze_comments

# comments = get_comments("data/survey_comments.csv")

# result = analyze_comments(comments)

# print(result)

from csv_reader import get_comments
from analyzer import analyze_comments
from exporter import export_themes


comments = get_comments(
    "data/survey_comments.csv"
)

result = analyze_comments(comments)

export_themes(result)
