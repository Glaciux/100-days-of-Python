# Build an automatic pizza order program
# use the camel naming style

# prepare the basic requirements to take orders.
print("Welcome to Python Pizza Deliveries!\nWhat will your order be?")

# take the order
size = input("What size do you want? S, M, or L\n")
addPepperoni = input("Do you want pepperoni? Y/N\n")
extraCheese = input("Do you want extra cheese? Y/N\n")

# add the conditions here
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if addPepperoni == "Y":
    bill += 2
else:
    bill += 3

if extraCheese == "Y":
    bill += 1

print(f"Your bill is: ${bill}")
