import os

from .cmds import config, lint_dir, lint_seq


class DNALint(object):
    """A linter for DNA"""

    def __str__(self):
        return "A linter for DNA"

    def lint(self, path='.'):
        if os.path.isdir(path):
            lint_dir(path)
        else:
            lint_seq(path)

    def config(self):
        config()
