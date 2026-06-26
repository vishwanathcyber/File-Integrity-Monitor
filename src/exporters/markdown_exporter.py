"""
Markdown Report Exporter
"""

def export_markdown(report, output_file):

    with open(output_file, "w") as file:

        file.write("# File Integrity Monitor Report\n\n")
        file.write(report)

    print(f"Markdown report saved to {output_file}")
