#!/usr/bin/env python3
# Script đóng gói và biên dịch sổ tay colab-drive.ipynb
import json
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
notebook_path = os.path.join(base_dir, 'colab-drive.ipynb')

scratch_script = r'C:\Users\Huy Vu\.gemini\antigravity-ide\brain\165b5953-47bc-413a-9736-2c93565d8cce\scratch\make_notebook.py'
sys.path.insert(0, os.path.dirname(scratch_script))
import make_notebook

notebook = {
    'nbformat': 4,
    'nbformat_minor': 0,
    'metadata': {
        'colab': {'provenance': []},
        'kernelspec': {'name': 'python3', 'display_name': 'Python 3'},
        'language_info': {'name': 'python'}
    },
    'cells': []
}

header_md = make_notebook.header_md

notebook['cells'].append({
    'cell_type': 'markdown',
    'metadata': {'id': 'header_intro'},
    'source': [line + '\n' for line in header_md.split('\n')]
})

notebook['cells'].append({
    'cell_type': 'code',
    'metadata': {'id': 'setup_environment', 'cellView': 'form'},
    'source': [line + '\n' for line in make_notebook.step1_code.split('\n')],
    'execution_count': None,
    'outputs': []
})

notebook['cells'].append({
    'cell_type': 'code',
    'metadata': {'id': 'mount_drive_storage', 'cellView': 'form'},
    'source': [line + '\n' for line in make_notebook.step2_code.split('\n')],
    'execution_count': None,
    'outputs': []
})

notebook['cells'].append({
    'cell_type': 'code',
    'metadata': {'id': 'inspect_source_urls', 'cellView': 'form'},
    'source': [line + '\n' for line in make_notebook.step3_code.split('\n')],
    'execution_count': None,
    'outputs': []
})

notebook['cells'].append({
    'cell_type': 'code',
    'metadata': {'id': 'execute_download_and_sync', 'cellView': 'form'},
    'source': [line + '\n' for line in make_notebook.step4_code.split('\n')],
    'execution_count': None,
    'outputs': []
})

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=2)

print('Build completed successfully: colab-drive.ipynb generated from modules')
