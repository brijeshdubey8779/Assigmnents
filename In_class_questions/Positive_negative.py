# Python code to check whether a given number is Positive or Negative
# using only "if" statement
"""
x = float(input("Enter a number"))
if x > 0:
    print(x, " is Positive number")
if x <= 0:
    print(x, " is non positve number")
"""

# using "if else" statement
'''
x = float(input("Enter a number"))
if x > 0:
    print(x, " is Positive number")
else:
    print(x, " is non positve number")
'''
# using single line if else

x = float(input("Enter a number"))
print(x, " is Positive number") if x > 0 else print(
    x, " is non positve number")
