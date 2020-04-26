from .const import seq_types
from .parse_seq import parse_seq
from .printer import red_print


def read_seq(seq_path):
    ext = seq_path[seq_path.rfind('.') + 1:]
    seq_type = seq_types.get(ext)
    if not seq_type:
        red_print('dnalint can only read Fastas, GenBank files, and SnapGene files')
        return {}
    seq_data = parse_seq(seq_path, seq_type)
    return seq_data
