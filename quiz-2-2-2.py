# Author JRI 12/7/21

statement = input("Please enter a statement ")
x = "not"

if x in statement:
    print(statement)
if x not in statement:
    print("{0} {1}".format(x, statement))
