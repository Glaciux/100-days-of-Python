# write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output
# should be 3 + 5 = 8

two_digit_number = input("Type the two digit number: ")

# find the index of the two digit numbers.
a = int((two_digit_number)[0])
b = int((two_digit_number)[1])

# assing the int function to each index and add.
print(a + b)
