# DNA lint

A linter for DNA sequences

## Why?

Biology tooling is way behind the times https://xkcd.com/2298/

Iterating in biology is very slow and mistakes can be very hard to identify. Mistakes like using the wrong antibiotic resistance, including golden gate restriction sites, or inserting a single nucleotide can cost weeks of time. DNA lint will check for errors and suggest experimental problems to watch out for.

## What is a linter?

From wikipedia, `lint, or a linter, is a tool that analyzes source code to flag programming errors, bugs, stylistic errors, and suspicious constructs`

https://en.wikipedia.org/wiki/Lint_(software)

## Installation

Clone this repository and run `pip install .`

## Usage

* To lint a sequence or directory, run `dnalint lint [path]`
* To lint the current directory, run `dnalint lint`

## Contributing

If you are interested in contributing, please get in touch! My email is in the setup.py

I am looking for people to help build the CLI, design the linting strategy, and suggest biological rules/style considerations to flag
