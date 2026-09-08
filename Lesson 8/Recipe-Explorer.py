# ------ Recipe Explorer -------

# STEP 1 - CREATE TUPLES FOR RECIPE DETAILS (FIXED - CANNOT BE CHANGED)
pasta = ("Pasta Arrabita", "Italian", 20, "Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hard")
print("Recipe 1:", pasta)
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty:", pasta[-1])

# STEP 2 - NESTED TUPLES AND SLICING

all_recipes = (pasta, biryani)
print("\nFirst recipe name:", all_recipes[0][0])
print("Seconf recipe item:", all_recipes[1][2], "mins")
print("Pasta details (sliced):", pasta[1:3])

# STEP 3 - ITERATE THROUGH A TUPLE 
print("\nPasta Recipe details:")
for detail in pasta:
    print(" -", detail)

# STEP 4 - CREATE SETS FOR INGREDIENTS (NO DUPLICATE ALLOWED)
pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
biryani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}
print("\nPasta ingredients:", pasta_ingredients)
print("\nBiryani ingredients:", biryani_ingredients)
print("Total pasta ingredients:", len(pasta_ingredients))

# STEP 5 - MODIFY THE SET
pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chilli")
print("\nUpdated pasta ingredients:", pasta_ingredients)

# STEP 6 - SET OPERATIONS
all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll ingredients (union):", all_ingredients)
print("Common ingredients (intersection):", common)
print("Only in Pasta (difference):", only_pasta)
print("Not shared (sym. difference):", unique_to_each)