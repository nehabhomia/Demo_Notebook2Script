"""
Main entry point for the Pokémon data fetcher application.

This module simply delegates execution to the command-line interface defined
in `cli.py`. It can be run directly to start the Pokémon data fetch process.
"""

from cli import run_cli

if __name__ == '__main__':
    run_cli()
