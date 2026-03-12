#!/usr/bin/env python3
import os

root = '../lang'
output_md = 'LIST.md'

entries = []

for dirpath, dirnames, filenames in os.walk(root):
    for f in filenames:
        if f.lower().endswith('.png'):
            continue

        rel_path = os.path.relpath(os.path.join(dirpath, f), start='.')
        lang = os.path.basename(dirpath)

        image_path = os.path.join(dirpath, f'{lang}.png')
        if os.path.exists(image_path):
            image_md = f'![{lang}]({os.path.relpath(image_path, start=".")})'
        else:
            image_md = ''

        entries.append((lang, rel_path, image_md))

entries.sort(key=lambda x: x[0].lower())

with open(output_md, 'w', encoding='utf-8') as md:
    md.write('# All Files in Repository\n\n')
    md.write('Language | File | Image\n')
    md.write('-------- | ---- | -----\n')
    for lang, path, image in entries:
        md.write(f'{lang} | [{os.path.basename(path)}]({path}) | {image}\n')

print(f'Markdown file created at {output_md}')