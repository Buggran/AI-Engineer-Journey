import pandas as pd


def export_themes(result):

    themes = result["themes"]

    rows = []

    for theme in themes:

        rows.append(
            {
                "Theme": theme["theme"],
                "Sentiment": theme["sentiment"],
                "Evidence": " | ".join(
                    theme["evidence"]
                )
            }
        )

    df = pd.DataFrame(rows)
    print(df)
    df.to_excel(
        "ai_analysis.xlsx",
        index=False
    )

    print(
        "Excel file created: ai_analysis.xlsx"
    )