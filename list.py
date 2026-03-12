#!/usr/bin/env python3
import os

root = './lang'
output_md = 'FILES.md'

entries = []

for dirpath, dirnames, filenames in os.walk(root):
    for f in filenames:
        rel_path = os.path.relpath(os.path.join(dirpath, f), start='.')
        lang = os.path.basename(dirpath)
        entries.append((lang, rel_path))

entries.sort(key=lambda x: x[0].lower())

with open(output_md, 'w', encoding='utf-8') as md:
    md.write('# All Files in Repository\n\n')
    md.write('Language | File\n')
    md.write('-------- | ----\n')
    for lang, path in entries:
        md.write(f'{lang} | [{os.path.basename(path)}]({path})\n')

print(f'Markdown file created at {output_md}')