# Pokémon API Demo

This project demonstrates how to interact with the [PokeAPI](https://pokeapi.co/) using both a Jupyter notebook and a modular Python script.

---

## 📘 Contents

- `pokemon_api_demo.ipynb`  
  A Jupyter notebook for exploring the Pokémon API in an interactive and iterative manner.

- `scripts/`  
  A clean, multi-file version of the CLI tool.

- `outputs/`  
  A directory to store outputs from both the notebook and the scripts version.

- `requirements.txt`  
  Dependencies list

---

## 🚀 How to Use the Script

1. **Install dependencies** (if needed):
    ```bash
    # For running the script only
    pip install -r requirements.txt

    # For running the Jupyter notebook
    pip install -r requirements-dev.txt
    ```

2. **Run from the command line**:
    ```bash
   cd scripts 
   python main.py pikachu
    ```

3. **Example Output**:
    ```
    Name: pikachu
    Height: 4
    Weight: 60
    Types: electric
    Abilities: static, lightning-rod
    ```

---

## 🧠 Learning Points

### ✅ Jupyter Notebook Advantages:
- Ideal for exploratory data analysis.
- Great for visualizing intermediate results and debugging.
- Good for teaching and documentation.

### ❌ Jupyter Notebook Limitations:
- Hard to reproduce results consistently if cell execution order changes.
- Difficult to reuse logic without copying code between cells.
- Challenging to scale or integrate into automation.

---

### ✅ Python Script Advantages:
- Modular and reusable with clear separation of concerns.
- Easy to reproduce: always runs top-to-bottom.
- Works well with version control, automation, and command-line arguments.

### ❌ Script Limitations:
- Less interactive.
- Not ideal for trying out small snippets or visualizations.

---

## 🧪 Extension Ideas

- Allow batch input of multiple Pokémon names.
- Include stats or evolution chain data.
- Visualize types or abilities using matplotlib.

---

## Contributing
Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.


Happy Coding!
