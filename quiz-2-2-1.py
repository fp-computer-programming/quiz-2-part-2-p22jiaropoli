# Author JRI 12/7/21

letter_day = input("Enter a letter A to G ")
x = letter_day.upper()

if x == "A" or x == "C" or x == "E":
    print("You have class today because it is {0} day.".format(x))
elif x == "B" or x == "D" or x == "F" or x == "G":
    print("You do not have class today because it is {0} day.".format(x))
else:
    print("Day {0} is not a day of the school week.".format(x))
