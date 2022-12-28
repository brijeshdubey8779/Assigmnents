# python script to display the number of days in a given month number.
'''
m = int(input("Enter month number( 1 to 12):"))

match m:
    case 1:
        print("31")
    case 2:
        print("28")
    case 3:
        print('31')
    case 4:
        print('30')
    case 5:
        print('31')
    case 6:
        print("30")
    case 7:
        print('31')
    case 8:
        print('31')
    case 9:
        print('30')
    case 10:
        print('31')
    case 11:
        print("30")
    case 12:
        print('31')
    case _:
        print("Please enter number betwen 1 to 12 only.")
'''

# menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division
'''
m = int(input("Choose one of the following\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n"))

match m:
    case 1:
        n1 = float(input("Enter the first number:"))
        n2 = float(input("Enter the second number:"))
        print("Sum of %1f and %1f is:" % (n1, n2), n1+n2)
    case 2:
        n1 = float(input("Enter the first number:"))
        n2 = float(input("Enter the second number:"))
        print("Diffrence of %1f and %1f is:" % (n1, n2), n1-n2)
    case 3:
        n1 = float(input("Enter the first number:"))
        n2 = float(input("Enter the second number:"))
        print("Multiplication of %1f and %1f is:" % (n1, n2), n1*n2)
    case 4:
        n1 = float(input("Enter the first number:"))
        n2 = float(input("Enter the second number:"))
        print("Division of %1f and %1f is:" % (n1, n2), n1/n2)
    case _:
        print("Invailid input")
'''

# 3. Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles
# triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right
# angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.
'''
m = int(input("\n1. Check whether a given set of three numbers are lengths of an isosceles triangle or not\n2. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not\n3. Check whether a given set of three numbers are equilateral triangle or not\n4. Exit.\n"))
match m:
    case 1:
        n1 = float(input("Enter the first number:"))
        n2 = float(input("Enter the second number:"))
        n3 = float(input("Enter the third number:"))
        if n1 == n2 or n2 == n3 or n1 == n3:
            print("Its isosceles triangle")
        else:
            print("Its not a isosceles triangle")
    case 2:
        n1 = float(input("Enter the first number:"))
        n2 = float(input("Enter the second number:"))
        n3 = float(input("Enter the third number:"))
        if n1 > n2 and n1 > n3:
            if n1**2 == (n2**2)+(n3**2):
                print("Its a right angle")
            else:
                print("Its not a right angle")
        elif n2 > n1 and n2 > n3:
            if n2**2 == (n1**2)+(n3**2):
                print("Its a right angle")
            else:
                print("Its not a right angle")
        elif n3 > n2 and n3 > n1:
            if n3**2 == (n1**2)+(n2**2):
                print("Its a right angle")
            else:
                print("Its not a right angle")
        else:
            print("Its not a right angle")
    case 3:
        n1 = float(input("Enter the first number:"))
        n2 = float(input("Enter the second number:"))
        n3 = float(input("Enter the third number:"))
        if n1 == n2 == n3:
            print("Its a equilateral triangle")
        else:
            print("Its not a equilateral triangle")
    case 4:
        exit(0)
    case _:
        print("Invailid input")
'''

# program which takes user’s age and display the category of person. Age below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
# Experienced, Age above or equal 60 - Senior Citizen.
'''
age = int(input("Enter your age:"))
if age < 10:
    c = 1
elif age < 20:
    c = 2
elif age < 40:
    c = 3
elif age < 60:
    c = 4
else:
    c = 5

match c:
    case 1:
        print("kid")
    case 2:
        print("Teen")
    case 3:
        print("Young")
    case 4:
        print("Experienced")
    case 5:
        print("Senior citizen")
'''

# Write a program which takes a number from user. Print Saurabh Shukla if the number
# is even, print Prateek Jain if the number is negative odd number and print Aditya
# Choudhary if number is positive odd number.
'''
n = int(input("Enter a number:"))
if n % 2 == 0:
    print("Saurabh Shukla")
elif n % 2 != 0 and n < 0:
    print("Pratekk Jain")
elif n % 2 != 0 and n > 0:
    print("Aditya Choudhary")
'''

# Write a python program to check whether a given string is a multiword string or single
# word string using match case statement
'''
s = input("Enter a string or character:")
if len(s) > 1:
    c = 1
else:
    c = 2
match c:
    case 1:
        print("Multiword string")
    case 2:
        print("single word string")
'''

# Write a python program to check whether a given number is positive, negative or
# zero using match case statement
'''
n = int(input("Enter the number:"))
match 0 if n < 0 else 1 if n > 0 else 2:
    case 0:
        print("Number is negative")
    case 1:
        print("Number is positive")
    case 2:
        print("Its zero")
'''

# Write a python script to check whether two given strings are identical, first string
# comes before the second in dictionary order or first string comes after the second
# string in dictionary order using match case statement
'''
s1 = input("Enter first string:")
s2 = input("Enter second string:")

match 0 if s1 == s2 else 1 if s1 > s2 else 2:
    case 0:
        print("Both strings are same")
    case 1:
        print("%s comes first in dictionary order" % s2)
    case 2:
        print("%s comes first in dictionary order" % s1)
'''

# Write a python script to check whether a given year is
# a. Non century leap year
# b. Century leap year
# c. Non century non leap year
# d. Century non leap year
'''
y = int(input("Enter the year:"))
match 0 if y % 4 == 0 and y % 400 != 0 and y % 100 != 0 else 1 if y % 4 == 0 and y % 400 == 0 and y % 100 == 0 else 2 if y % 4 != 0 else 3:
    case 0:
        print("Non century leap year")
    case 1:
        print("Century leap year")
    case 2:
        print("Non century on leap year")
    case 3:
        print("Century non leap year")
'''

# Write a program to display day name on the basis of user’s liking of a colour. Ask
# user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Assuming all colour name entered by user is in lowercase. Use match case to display
# day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colours - Sunday
'''
c = input("Enter the colour you like(can also say in sentence)").lower()
match "yellow" if "yellow" in c else "blue" if 'blue' in c else 'orange' if 'orange' in c else 'white' if 'white' in c else 'black' if 'black' in c else 'red' if 'red' in c else 0:
    case 'yellow':
        print("Monday")
    case 'blue':
        print("Tuseday")
    case 'orange':
        print("Wednesday")
    case 'white':
        print("Thusday")
    case 'black':
        print("Friday")
    case 'red':
        print("Saturday")
    case _:
        print("Sunday")
'''
