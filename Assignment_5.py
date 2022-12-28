# python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
'''
x = int((input("Enter a number")))
x = x//10
print(x)
'''

# python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)
'''
x = int((input("Enter a number")))
x = x % 10
print(x)
'''

# a python script to swap data of two variables
"""
a = int(input("Enter a number:"))
b = int(input("Enter second number:"))
print("a=", a, "b", b)
a, b = b, a
print("After swap\na=", a, "b=", b)
"""

# python script to find x power y, where values of x and y are given by user
'''
x = int(input("Enter a number:"))
y = int(input("Enter another number:"))
x = x**y
print("x power y is:", x)
'''

# python script which takes a three digit number from the user and displays only its first digit.
'''
n = int(input("Enter a 3 digi number:"))
m = n//100
print("First digit of", n, "is", m)
'''

# python script which takes a three digit number from the user and  only its middle digit.
'''
n = int(input("Enter a 3 digi number:"))
m = n//10
m = m % 10
print("Middle digit of", n, "is", m)
'''

# python script which takes a three digit number from the user and displays only its last digit.
'''
x = int((input("Enter a three digit number")))
l = x % 10
print("the last digit of",x,"is",l)
'''

# python script to use IN operator to display the data present in the list
"""
lst = [1, 2, "Brijesh", 17, 11, True]
for i in lst:
    print(i)
"""

# a python script to use NOT IN operator to display the data not present in list
"""
lst = [1, 2, "Brijesh", 17, 11, True]
if 3 not in lst:
    print("3 is not present in", lst)
"""

# python script to use IS operator to display if both variables are the same object or not?
"""
a = 23
b = a
if a is b:
    print("a nd b are same")
"""
