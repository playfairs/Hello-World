#!/usr/bin/env python3
import os
import shutil

lang_map = {
    '.ada': 'ada',
    '.asm': 'asm',
    '.bf': 'brainfuck',
    '.c': 'c',
    '.cpp': 'cpp',
    '.i': 'c',
    '.m': 'objective-c',
    '.cs': 'csharp',
    '.cbl': 'cobol',
    '.dpr': 'delphi',
    '.exs': 'elixir',
    '.erl': 'erlang',
    '.f90': 'fortran',
    '.go': 'go',
    '.hs': 'haskell',
    '.hlsl': 'hlsl',
    '.java': 'java',
    '.js': 'javascript',
    '.jl': 'julia',
    '.kt': 'kotlin',
    '.tex': 'latex',
    '.lisp': 'lisp',
    '.lua': 'lua',
    '.mal': 'malbolge',
    '.pl': 'perl',
    '.php': 'php',
    '.psql': 'postgres',
    '.py': 'python',
    '.r': 'r',
    '.rb': 'ruby',
    '.rs': 'rust',
    '.sc': 'scala',
    '.scm': 'scheme',
    '.scss': 'scss',
    '.sh': 'shell',
    '.sol': 'solidity',
    '.sql': 'sql',
    '.swift': 'swift',
    '.t': 'tap',
    '.ts': 'typescript',
    '.vb': 'vbnet',
    '.jade': 'pug',
}

root = './lang'

for dirpath, dirnames, filenames in os.walk(root):
    for f in filenames:
        if dirpath.endswith('sql') and f in ['main.psql','query.sql']:
            ext = '.psql' if f=='main.psql' else '.sql'
        else:
            ext = os.path.splitext(f)[1].lower()

        lang_folder = lang_map.get(ext)
        if lang_folder:
            dest_folder = os.path.join(root, lang_folder)
            os.makedirs(dest_folder, exist_ok=True)
            src_path = os.path.join(dirpath, f)
            dest_path = os.path.join(dest_folder, f)
            shutil.move(src_path, dest_path)
            print(f'Moved {f} -> {dest_folder}')
