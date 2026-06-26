"""
Audit Logger
"""

from datetime import datetime

def audit(event):

    print(f"[AUDIT] {datetime.now()} : {event}")
