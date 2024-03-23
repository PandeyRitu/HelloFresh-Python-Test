import json
import csv

def read_json_file(file):
    try:
        with open(file, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File '{file}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{file}'.")
        return None

def find_recipes_with_ingredient(recipes, ingredient):
    found_recipes = []
    for recipe in recipes:
        ingredients = recipe.get('ingredients', [])
        # Check if the ingredient (case-insensitive) is in the list of ingredients
        if any(ingredient.lower() in ing.lower() for ing in ingredients):
            found_recipes.append(recipe)
    return found_recipes

def calculate_difficulty(recipe):
    prep_time = recipe.get('prepTime', 0)  # Default to 0 if prepTime is missing
    cook_time = recipe.get('cookTime', 0)  # Default to 0 if cookTime is missing
    total_time = prep_time + cook_time
    if total_time > 60:
        return "Hard"
    elif total_time >= 30:
        return "Medium"
    elif total_time < 30:
        return "Easy"
    else:
        return "Unknown"

file = "bi_recipes.json"



# Calling the function to read the file
recipes_data = read_json_file(file)


            writer = csv.writer(csvfile, delimiter = ‘|’)
            writer.writerow(['Difficulty', 'AverageTotalTime'])
            for difficulty, average_time in average_times.items():
                writer.writerow([difficulty, average_time])

        print("Results.csv file created successfully.")
    else:
        print("No recipes found with 'Chilies' (or variations) as one of the ingredients.")
 

      # Maintain a set of unique recipe titles
        unique_titles = set()

        # Write data to CSV file
        with open('Chilies.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')

            # Write header
            writer.writeheader()

            # Write each unique recipe as a row in the CSV file
            for recipe in all_chili_recipes:
                title = recipe.get('title')
                # Check if the title is already written to CSV
                if title not in unique_titles:
                    # Calculate difficulty and add it to the recipe
                    recipe['difficulty'] = calculate_difficulty(recipe)
                    writer.writerow(recipe)
                    # Add title to set of unique titles
                    unique_titles.add(title)

        print("Chilies.csv file created successfully.")
    else:
        print("No recipes found with 'Chilies' (or variations) as one of the ingredients.")