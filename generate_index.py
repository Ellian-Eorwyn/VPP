import os

ARCHIVE_DIR = "LFCommsArchives"
OUTPUT_FILE = os.path.join(ARCHIVE_DIR, "index.html")

folders = [
    name for name in os.listdir(ARCHIVE_DIR)
    if os.path.isdir(os.path.join(ARCHIVE_DIR, name)) and
       os.path.isfile(os.path.join(ARCHIVE_DIR, name, "index.html"))
]

folders.sort()

html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Archived Sites Index</title>
</head>
<body>
    <h1>Archived Websites</h1>
    <ul>
"""

for folder in folders:
    html += f'        <li><a href="{folder}/">{folder}</a></li>\n'

html += """    </ul>
</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Index page written to: {OUTPUT_FILE}")