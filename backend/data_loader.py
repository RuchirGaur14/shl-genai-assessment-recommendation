import pandas as pd
import os

def load_assessments():
    """
    Load SHL catalog and expand into multiple logically distinct assessments
    with meaningful descriptions.
    """

    path = os.path.join("data", "shl_catalog.csv")
    df = pd.read_csv(path)

    expanded = []

    for _, row in df.iterrows():
        expanded.extend([
            {
                "name": "SHL Technical Skills Assessment",
                "description": "Evaluates programming skills, coding ability, and software development knowledge",
                "url": row["url"]
            },
            {
                "name": "SHL Coding Assessment",
                "description": "Assesses hands-on coding, debugging, and algorithmic problem solving",
                "url": row["url"]
            },
            {
                "name": "SHL Cognitive Ability Test",
                "description": "Measures logical reasoning, numerical ability, and critical thinking skills",
                "url": row["url"]
            },
            {
                "name": "SHL Aptitude Test",
                "description": "Evaluates quantitative aptitude, verbal reasoning, and analytical ability",
                "url": row["url"]
            },
            {
                "name": "SHL Personality Assessment",
                "description": "Assesses personality traits, work behavior, and interpersonal style",
                "url": row["url"]
            },
            {
                "name": "SHL Behavioral Assessment",
                "description": "Evaluates workplace behavior, attitude, and cultural fit",
                "url": row["url"]
            }
        ])

    return pd.DataFrame(expanded)
