import json
import os
from pathlib import Path

from .const import seq_types
from .io import read_seq
from .linter import lint
from .printer import red_print


def lint_seq(seq_path):
    ext = seq_path[seq_path.rfind('.') + 1:]
    if ext not in seq_types:
        red_print('dnalint can only read Fastas, GenBank files, and SnapGene files')
        return
    seq_data = read_seq(seq_path)
    lint(seq_path, seq_data['seq'])


def lint_dir(dir_path='.'):
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            ext = file_name[file_name.rfind('.') + 1:]
            if ext not in seq_types:
                continue
            seq_path = os.path.join(root, file_name)
            seq_data = read_seq(seq_path)
            lint(seq_path, seq_data['seq'])


def config():
    # TODO: configurable settings
    api_key = input('API key: ')
    cfg = {'api_key': api_key}

    home = str(Path.home())
    Path("{}/.dnalint".format(home)).mkdir(parents=True, exist_ok=True)
    with open('{}/.dnalint/config.json'.format(home), 'w') as f:
        f.write(json.dumps(cfg))
