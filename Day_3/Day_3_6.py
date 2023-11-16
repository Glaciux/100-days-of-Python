# Build a love calculator that will count the number of times "true love" appeared in ones name
# and assign a score.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your name? \n")

# Think logically. count(), lower(), concatenate,
# first combine the name1 & name2 to get a string to enable concatenation
combinedName = name1 + name2

# switch to lower case
lower_case_name = combinedName.lower()

# find the count of t, r, u, e and sum
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")
true = t + r + u + e

# find the count of l, o, v, e and sum
l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")
love = l + o + v + e

# find the score. Remember, it's in "int" format so convert to "str" to
# concatenate

loveScore = int(str(true) + str(love))

if (loveScore < 10) or (loveScore > 90):
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif (loveScore >= 40) and (loveScore <= 50):
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}")
