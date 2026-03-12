#!/usr/bin/env python3
import os

root = '../lang'
github_base = 'https://github.com/playfairs/Hello-World/blob/master'
output_md = 'LIST.md'
entries = []

for dirpath, dirnames, filenames in os.walk(root):
    for f in filenames:
        if f.lower().endswith('.png'):
            continue

        lang = os.path.basename(dirpath)
        file_rel_path = os.path.join(dirpath, f)
        file_url = f'{github_base}/{file_rel_path.replace(os.sep, "/")}'

        image_file = os.path.join(dirpath, f'{lang}.png')
        if os.path.exists(image_file):
            image_url = f'{github_base}/{image_file.replace(os.sep, "/")}'
            image_md = f'![{lang}]({image_url})'
        else:
            image_md = ''

        entries.append((lang, f, file_url, image_md))

entries.sort(key=lambda x: x[0].lower())

with open(output_md, 'w', encoding='utf-8') as md:
    md.write('# All Files in Repository\n\n')
    md.write('Language | File | Image\n')
    md.write('-------- | ---- | -----\n')
    for lang, fname, file_url, image_md in entries:
        md.write(f'{lang} | [{fname}]({file_url}) | {image_md}\n')

print(f'Markdown file created at {output_md}')