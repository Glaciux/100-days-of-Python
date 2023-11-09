# f-string: add before a string.
# e.g. print(f"your name is {}")

# write a program to show the number of days, weeks, and months
# if you live up to 90.

# add your name
name = input("what is your name? ")

# add your age
age = int(input("What is your age? "))

# add age and years in months
ageInMonths = age * 12
ninetyYearsInMonths = 90 * 12

# add age and years in days
ageInDays = age * 365
ninetyYearsInDays = 90 * 365

# add age and years in weeks
ageInWeeks = age * 52
ninetyYearsInWeeks = 90 * 52

# calculate the months, weeks, and days to reach 90 years.

monthsToNinetyLeft = ninetyYearsInMonths - ageInMonths
daysToNinetyLeft = ninetyYearsInDays - ageInDays
weeksToNinetyLeft = ninetyYearsInWeeks - ageInWeeks

# print with f string
yearsLeft = (f"Yo {name}! You have {daysToNinetyLeft} days, {
    weeksToNinetyLeft} weeks, and {monthsToNinetyLeft} months to live up to 90.")

print(yearsLeft)

# # alternative solution
# age = int(input("what is your age? "))
# yearsLeft = 90 - age
# daysLeft = yearsLeft * 365
# monthsLeft = yearsLeft * 12
# weeksLeft = yearsLeft * 52
# report = f"Dear {name}!\nYou have {daysLeft} days, {
#     weeksLeft} weeks, and {monthsLeft} months to hit 90 years of age."
# print(report)
