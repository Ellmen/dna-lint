from setuptools import setup

setup(
    name='dnalint',
    version='0.1',
    description='A linter for DNA',
    url='http://github.com/Ellmen/dna-lint',
    author='Isaac Ellmen',
    author_email='isaacellmen@gmail.com',
    packages=['dnalint'],
    entry_points={
        'console_scripts': ['dnalint=dnalint.command_line:main'],
    }
)
