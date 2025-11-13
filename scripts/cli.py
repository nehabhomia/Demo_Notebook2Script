"""
Command-line interface for fetching and saving Pokémon characteristics.

This module provides a simple CLI tool that retrieves Pokémon data from the
PokéAPI and displays it as a pandas DataFrame. Optionally, results can be
saved to a CSV file using the `--output` argument.
"""

import argparse
from fetch import fetch_and_format
import pandas as pd

def run_cli() -> None:
    """
        Run the Pokémon data fetcher command-line interface.

        The CLI accepts a Pokémon name and optionally an output file path for saving
        results as CSV.

        Example
        -------
        $ python cli.py pikachu
        $ python cli.py bulbasaur --output bulbasaur.csv
        """
    parser = argparse.ArgumentParser(description="Fetch Pokémon characteristics from PokeAPI.")
    parser.add_argument("name", type=str, help="Name of the Pokémon")
    parser.add_argument("--output", type=str, help="Optional path to save results as CSV")
    args = parser.parse_args()

    try:
        df = fetch_and_format(args.name)
        print(df)

        if args.output:
            df.to_csv(args.output, index=False)
            print(f"Saved to {args.output}")
    except Exception as e:
        print(f"Error: {e}")