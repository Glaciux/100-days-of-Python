# Bandname generator.
# Ensure the cursor shows on a new line.

# Start with a greeting!
print("Welcome to the Band Name generator!!!\n")

# Ask the user their name.
# The "+ "\n" " will print the input results in a new line
username = input("What is your name?\n")

# Ask the user for the city they grew up in
city = input("What city did you grow up in?\n")

# Ask the user for the name of a pet
pet_name = input("What's your pet's name?\n")

# Combine the name of the city and pet and show their band name
print("Welcome to the Band Name generator, " + username + "!" +
      "\n" + "Your band name could be " + city + " " + pet_name + ".")
