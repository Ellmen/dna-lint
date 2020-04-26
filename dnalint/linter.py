from .printer import green_print


def lint(seq_path, seq):
    # TODO: create rules
    green_print('{} looks good!'.format(seq_path))
