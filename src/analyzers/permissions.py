"""
Permission Analyzer
"""

import os

def check_permissions(file):

    return oct(os.stat(file).st_mode)[-3:]
