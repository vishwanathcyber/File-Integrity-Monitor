"""
HTML Report Exporter
"""

def export_html(report, output_file):

    html = f"""
    <html>
    <head>
        <title>File Integrity Monitor Report</title>
    </head>
    <body>
        <h1>File Integrity Monitor</h1>
        <pre>{report}</pre>
    </body>
    </html>
    """

    with open(output_file, "w") as file:

        file.write(html)

    print(f"HTML report saved to {output_file}")
