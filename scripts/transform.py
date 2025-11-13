"""
Utility functions for extracting key characteristics from Pokémon data.

This module provides helper functions to parse and format relevant attributes
such as name, height, weight, types, and abilities from a Pokémon API response.

Example
-------
extract_characteristics(pokemon_data)
{
    'name': 'pikachu',
    'height': 4,
    'weight': 60,
    'types': 'electric',
    'abilities': 'static, lightning-rod'
}
"""


def extract_characteristics(data):
    """
        Extract key characteristics from a Pokémon data dictionary.

        Parameters
        ----------
        data : dict
            Dictionary containing Pokémon details, including 'name', 'height',
            'weight', 'types', and 'abilities'.

        Returns
        -------
        dict
            A dictionary with simplified Pokémon characteristics.
        """
    name = data['name']
    height = data['height']
    weight = data['weight']
    types = [t['type']['name'] for t in data['types']]
    abilities = [a['ability']['name'] for a in data['abilities']]
    return {
        'name': name,
        'height': height,
        'weight': weight,
        'types': ", ".join(types),
        'abilities': ", ".join(abilities)
    }