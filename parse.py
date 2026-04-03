import json

with open('mecs6616_Spring2026_Assignment2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open('assignment_content.md', 'w', encoding='utf-8') as f:
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'markdown':
            f.write(f"\n<!-- Markdown Cell {i} -->\n")
            f.write("".join(cell['source']) + "\n")
        elif cell['cell_type'] == 'code':
            f.write(f"\n<!-- Code Cell {i} -->\n```python\n")
            f.write("".join(cell['source']) + "\n```\n")
