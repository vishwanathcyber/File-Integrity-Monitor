"""
Risk Score Analyzer
"""

def calculate_risk(modified, deleted, new):

    score = modified * 5 + deleted * 10 + new * 3

    if score >= 30:
        return "Critical"

    if score >= 20:
        return "High"

    if score >= 10:
        return "Medium"

    return "Low"
