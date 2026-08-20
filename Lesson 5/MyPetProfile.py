# ===============================
# My Pet Profile
# ===============================

# Function to display pet information
def pet_profile(name, animal, age):
    print("\n--- My Pet Profile ---")
    print("Pet Name:", name)
    print("Animal:", animal)
    print("Age:", age, "years old")

    if age < 5:
        print("Your pet is still young!")
    else:
        print("Your pet is a grown-up!")



# Function to give a greeting
def pet_greeting(name):
    print("\nHello", name + "!")
    print("Welcome to your pet profile!")

# Get information from the user
pet_name = input("Enter your pet's name:")
pet_animal = input("Enter the animal type:")
pet_age = int(input("Enter your pet's age:"))

# Call the function
pet_greeting(pet_name)
pet_profile(pet_name, pet_animal, pet_age)

print("\nThank you for creating your pet profile!")