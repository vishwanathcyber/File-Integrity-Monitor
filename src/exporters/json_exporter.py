"""
JSON Report Exporter
"""

import json

def export_json(report, output_file):

    with open(output_file, "w") as file:

        json.dump(report, file, indent=4)

    print(f"JSON report saved to {output_file}")
