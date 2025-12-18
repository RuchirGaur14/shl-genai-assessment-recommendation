def enrich_metadata(assessment_name: str):
    """
    Infer metadata based on assessment type.
    """

    name = assessment_name.lower()

    if "coding" in name or "technical" in name:
        return {
            "test_type": "Technical Skill Test",
            "duration": "60 minutes",
            "remote_support": "Yes",
            "adaptive_support": "Yes"
        }

    if "cognitive" in name or "aptitude" in name:
        return {
            "test_type": "Cognitive Ability Test",
            "duration": "45 minutes",
            "remote_support": "Yes",
            "adaptive_support": "Yes"
        }

    if "personality" in name or "behavioral" in name:
        return {
            "test_type": "Personality Assessment",
            "duration": "30 minutes",
            "remote_support": "Yes",
            "adaptive_support": "No"
        }

    return {
        "test_type": "General Assessment",
        "duration": "45 minutes",
        "remote_support": "Yes",
        "adaptive_support": "No"
    }
