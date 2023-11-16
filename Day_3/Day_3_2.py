"""
update BMI claculator
create a program that a]calculate the BMI with the conditions:
1. If the BMI = 18.5, they are underweight
2. If the BMI > 18.5 but BMI < 25, they are a normal weight
3. If the BMI is > 25 but < 30 , then overweight
4. If the BMI is > 30 but < 35, then obese
5. If the BMI is > 35 the clinically obese."""

# enter the height and weight
height = float(input("Enter height in m: "))
weight = float(input("Enter weight in kg: "))

# calculate the BMI
BMI = round(weight/height**2)

# calculate your conditions

if BMI == 18.5:
    print(f"Your BMI is {BMI}. You are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}. You are normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}. You are overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}. You are obese.")
else:
    print(f"Your BMI is {BMI}. You are clinically obese.")
