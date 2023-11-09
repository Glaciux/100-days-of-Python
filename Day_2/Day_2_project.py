# write a program for a calculator app that splits the bill between 5 people, with 12% tip.

print("Welcome to the tip calculator.\nEnter your details below.")

# add the total bill
totalBill = float(input("What is the total bill? "))

# enter the tip percentage
tipPercentage = float(input(
    "What percentage tip would you like to give? 5%, 10%, 12%, or 20%? "))

# number of people to split the bill
ratioPerPerson = input("How many people to split the bill? ")

# calculate the bill using float and round datatypes
splitRatio = round(float(totalBill/5) * float(1 + tipPercentage/100), 2)

# print the bill
print("Each person should pay: " + "$" + str(int(splitRatio)))
