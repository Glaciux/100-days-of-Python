# Control Flow and Logic Operators
# The modulo %
# 7%2 = 1 (outputs the remainder)

print("Welcome to Disney World!")
print("")

height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))

if height >= 155:
    print("You can ride the rollercoaster!")
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You can't ride the rollercoaster!")


# # write a program that works out whether if a given number is an
# # odd or even number

# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")
