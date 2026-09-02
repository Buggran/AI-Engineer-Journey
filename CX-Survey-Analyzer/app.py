import json

from survey_comments import comments
from analyzer import analyze_comments

result = analyze_comments(comments)

print(result)

with open("output.json", "w") as file:
    json.dump(result, file, indent=4)

print("\nResults saved to output.json")