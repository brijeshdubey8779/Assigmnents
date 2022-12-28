# python script to check whether a given number is positive or non-positivepython script to check whether a given number is positive or non-positive
'''
n = int(input("Enter a number:"))
if n > 0:
    print("%d is positive number" % n)
else:
    print("%d is non-positive number" % n)
'''

# python script to check whether a given number is divisible by 5 or not
"""
n = int(input("Enter a number:"))
if n % 5 == 0:
    print("%d is divisible by 5" % n)
else:
    print("%d is not divisible by 5" % n)
"""

# python script to check whether a given number is even or odd

"""
n = int(input("Enter a number:"))
if n % 2 == 0:
    print("%d is even number" % n)
else:
    print("%d is odd number" % n)
"""

# python script to print greater between two numbers. Print number only once even if the numbers are the same.
"""
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

if n1 > n2 or n1 == n2:
    if n1 == n2:
        print("Both are same")
    else:
        print("%d is grater" % n1)
else:
    print("%d is greater" % n2)
"""

# python script to print two given words in dictionary order
'''
w1 = str(input("Enter first word:"))
w2 = str(input("Enter second word:"))
print("Words in dictionary order:")
if (w1 > w2):
    print(w2, w1, sep="\n")
else:
    print(w1, w2, sep="\n")
'''

# python script to check whether a given number is a three digit number or not.
'''
n1 = int(input("Enter first number:"))

if n1 % 1000 == n1 and n1 % 10 <= 9:
    print("%d is 3 digit number" % n1)
else:
    print("%d is not 3 digit number" % n1)
'''

# python script to check whether a given number is positive, negative or zero.
'''
n = int(input("Enter the number:"))
if n > 0:
    print("%d is positve number." % n)
elif n < 0:
    print("%d is negative number." % n)
else:
    print("Its zero")
'''

# python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
'''
a = float(input("Enter th value of a(co-efficient of x^2):"))
b = float(input("Enter th value of b(co-efficient of x):"))
c = float(input("Enter th value of c(Constent):"))
d = (b**2)-(4*a*c)

if d == 0:
    print("Quadratic equation has real & equal roots")
elif d > 0:
    print("Quadratic equation has two real roots")
else:
    print("Quadratic equation has imaginary roots")
'''

# python script to check whether a given year is a leap year or not.
'''
y = int(input("Enter the year:"))
if y % 4 == 0:
    print("%d is leap year" % y)
else:
    print("%d is not leap year" % y)
'''

# python script to print greater among three numbers. Print number only once even if the numbers are the same.
'''
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
n3 = int(input("Enter third number:"))

if n1 == n2 == n3:
    print(n1)
elif n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)
'''

# python script to take the month value in numeric format and display the number of days in it.
'''
m = int(input("Enter month(1 to 12:"))
if m == 2:
    print("If its leap year than it has 29 days else 28 days.")
elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print("It has 31 days.")
elif m == 4 or m == 6 or m == 9 or m == 11:
    print("It has 30 days.")
else:
    print("Please enter month number only( 1 to 12)")
'''

# python script to accept one complex number from the user and display the greater number between real part and imaginary part
'''
img = complex(input("Enter the imaginary number(use j on the place of i)"))
if img.real > img.imag:
    print(img.real)
else:
    print(img.imag)
'''
