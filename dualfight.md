# A Pokemon Types Table Plot In Python
## Seaborn Approach:
### References:
### https://stackoverflow.com/questions/33158075/custom-annotation-seaborn-heatmap
### https://stackoverflow.com/questions/40734343/artificial-tick-labels-for-seaborn-heatmaps
### Pokemon Type Table Reference: https://img.pokemondb.net/images/typechart.png

```
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

pokemon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                 "Fighting", "Poison", "Ground", "Flying", "Psychic",
                 "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

```
### A 2 Dimenstional Numpy Array Of Damage Multipliers For Attacking Pokemon:
```    
damage_array = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
                    [1, 2, 1/2, 1, 1/2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1/2, 1, 1, 1],
                    [1, 1, 2, 1/2, 1/2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1/2, 1, 1, 1],
                    [1, 1/2, 2, 1, 1/2, 1, 1, 1/2, 2, 1/2, 1, 1/2, 2, 1, 1/2, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 1/2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1/2, 1],
                    [2, 1, 1, 1, 1, 2, 1, 1/2, 1, 1/2, 1/2, 1/2, 2, 0, 1, 2, 2, 1/2],
                    [1, 1, 1, 1, 2, 1, 1, 1/2, 1/2, 1, 1, 1, 1/2, 1/2, 1, 1, 0, 2],
                    [1, 2, 1, 2, 1/2, 1, 1, 2, 1, 0, 1, 1/2, 2, 1, 1, 1, 2, 1],
                    [1, 1, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1/2, 1],
                    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1/2, 1, 1, 1, 1, 0, 1/2, 1],
                    [1, 1/2, 1, 1, 2, 1, 1/2, 1/2, 1, 1/2, 2, 1, 1, 1/2, 1, 2, 1/2, 1/2],
                    [1, 2, 1, 1, 1, 2, 1/2, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 1/2, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1/2, 0],
                    [1, 1, 1, 1, 1, 1, 1/2, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1/2],
                    [1, 1/2, 1/2, 1/2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1/2, 2],
                    [1, 1/2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1, 1, 1, 2, 2, 1/2, 1]])
```
### Define a function to calculate the modified values for a specific type interaction
```
def calculate_modified_values(attacking_types, defending_types, chart):
    modified_values = np.ones_like(chart, dtype=float)
    for i, attacker_type in enumerate(pokemon_types):
        for j, defender_type in enumerate(pokemon_types):
            attacking_modifier = 1
            defending_modifier = 1
            for at in attacking_types:
                attacking_modifier *= chart[pokemon_types.index(at)][j]
            for df in defending_types:
                defending_modifier *= chart[i][pokemon_types.index(df)]
            modified_values[i][j] = attacking_modifier * defending_modifier
    return modified_values
```
### Define a function to calculate the modified values for a specific type interaction
```
def calculate_modified_values(attacking_types, defending_types, chart):
    modified_value = 1.0
    for at in attacking_types:
        for df in defending_types:
            modified_value *= chart[pokemon_types.index(at)][pokemon_types.index(df)]
    return modified_value
```
### Get user input for attacking and defending types
```
attacking_types = input("Enter the attacking types (comma-separated): ").strip().split(',')
defending_types = input("Enter the defending types (comma-separated): ").strip().split(',')
```
### Calculate attack and defense values
```
attack_value = calculate_modified_values(attacking_types, defending_types, damage_array)
defense_value = calculate_modified_values(defending_types, attacking_types, damage_array)
```
### Display the results
```
print(f"Attack value: {attack_value:.2f}")
print(f"Defense value: {defense_value:.2f}")
```
