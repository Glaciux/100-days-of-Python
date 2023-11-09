# write a program that calculates BMI.
# Formula: BMI = (weight/height**2)
# Ensure the BMI is in integer format.

# Enter your height and covert to a float datatype.
height = float(input("Enter your height in m: "))

# Enter your weight. convert to a float datatype.
weight = float(input("Enter your weight in kg: "))

# BMI calculation. convert to an integer as required.
BMI = int(weight/height**2)

# print result
print(BMI)
