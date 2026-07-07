"""
Command-line interface for fetching and saving Pokémon characteristics.

This module provides a simple CLI tool that retrieves Pokémon data from the
PokéAPI and displays it as a pandas DataFrame. Optionally, results can be
saved to a CSV file using the `--output` argument.
"""

import argparse
import sys
from fetch import fetch_and_format


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
    parser = argparse.ArgumentParser(
        description="Fetch and display Pokémon characteristics from the PokeAPI.",
        epilog=(
            "Examples:\n"
            "  python main.py pikachu\n"
            "  python main.py bulbasaur --output bulbasaur.csv\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("name", type=str, help="Name of the Pokémon to look up (e.g. pikachu)")
    parser.add_argument(
        "--output",
        type=str,
        metavar="FILE",
        help="Path to save the results as a CSV file (e.g. --output results.csv)",
    )
    args = parser.parse_args()

    try:
        df = fetch_and_format(args.name)
        print(df)

        if args.output:
            df.to_csv(args.output, index=False)
            print(f"Saved to {args.output}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
