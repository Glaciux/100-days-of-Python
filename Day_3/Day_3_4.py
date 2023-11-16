# Control Flow and Logic Operators
# The modulo %
# 7%2 = 1 (outputs the remainder)
# Edit the code to add the condition below:
# add $3 if they want a photo taken so make bill = 0.
print("Welcome to Disney World!")
print("")

name = input("What is your name? ")
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
bill = 0

if height >= 155:
    print("You can ride the rollercoaster!")
    if age < 12:
        # add bill for each age category.
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
    want_photo = input("Do you want your photo taken? Y/N. ")
    if want_photo == "Y" or "y" or "N" or "n":
        # add $3 to the bill -- additional fee for a photo
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you can't ride the rollercoaster!")


# # write a program that works out whether if a given number is an
# # odd or even number

# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")
