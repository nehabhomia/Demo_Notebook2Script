"""
Client utilities for fetching and formatting Pokémon data.

This module retrieves Pokémon details from the public PokéAPI and converts
them into a tabular pandas DataFrame using helper functions from `transform`.
"""

import requests
import pandas as pd
from transform import extract_characteristics
from typing import Any


def get_pokemon_data(name: str) -> dict[str, Any]:
    """
        Retrieve raw Pokémon data from the PokéAPI.

        Parameters
        ----------
        name : str
            The name of the Pokémon to fetch.

        Returns
        -------
        dict
            JSON-like dictionary returned by the PokéAPI.

        Raises
        ------
        ValueError
            If no Pokémon with the given name is found.
        """
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Pokémon '{name}' not found.")
    return response.json()


def fetch_and_format(name: str) -> pd.DataFrame:
    """
        Fetch a Pokémon by name and return its characteristics as a DataFrame.

        Parameters
        ----------
        name : str
            The name of the Pokémon to fetch.

        Returns
        -------
        pandas.DataFrame
            A DataFrame containing one row of Pokémon characteristics.
        """
    data = get_pokemon_data(name)
    row = extract_characteristics(data)
    return pd.DataFrame([row])