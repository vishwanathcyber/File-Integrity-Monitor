"""
Severity Classification
"""

def classify(change):

    if change == "deleted":

        return "Critical"

    if change == "modified":

        return "High"

    if change == "new":

        return "Medium"

    return "Low"
