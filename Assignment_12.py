# Write a python script to reverse a number.
'''
n = int(input("Enter the number:"))
count = len(str(n))

while n >= 1:
    j = n % 10
    print(j, end="")
    n //= 10
'''

# Write a python script to check whether a given number is Prime or not
'''
n = int(input("Enter then number:"))

for i in range(2, (n//2)+1):
    if n % i == 0:
        break
else:
    print("Its a prime number")
    exit()
print("Its not a prime number")
'''

# Write a python script to print all Prime numbers under 100
'''
for i in range(2, 101):
    for j in range(1, (i//2)+1):
        if j == 1:
            continue
        elif i % j == 0:
            break
        else:
            continue
    else:
        print(i)
'''

# Write a python script to print all Prime numbers between two given numbers (both values inclusive)
'''
print("Enter two numbers you want prime number between of:")
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

for i in range(n1, n2+1):
    for j in range(1, (i//2)+1):
        if j == 1:
            continue
        elif i % j == 0:
            break
        else:
            continue
    else:
        print(i)
'''

# Write a python script to find next prime number of a given number
'''
n = int(input("Enter the number you want next prime number of:"))
count = 0
while count == 0:
    n += 1
    for i in range(2, (n//2)+1):
        if n % i == 0:
            break
        else:
            continue
    else:
        print(n)
        count += 1
    if count != 0:
        break
'''

# Write a python script to print first N prime numbers
'''
n = int(input("How many prime numbers you want:"))
count = 0
n1 = 2
while count < n:
    for i in range(2, (n1//2)+1):
        if n1 % i == 0:
            n1 += 1
            break
        else:
            continue
    else:
        print(n1)
        count += 1
        n1 += 1
'''

# Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
'''
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

for i in range(2, (n1//2)+1):
    if n1 % i == 0 and n2 % i == 0:
        print("They are not co-prime numbers")
        break
    else:
        continue
else:
    print("they are co prime numbers")
'''

# Write a python script to print first N terms of a Fibonacci series
'''
n = int(input("Enter a number:"))
a = 0
b = 1
for i in range(0, n):
    if i == 0:
        print(a, end=",")
    elif i == 1:
        print(b, end=",")
    else:
        a = a+b
        print(a, end=",")
        a, b = b, a
'''

# Write a python script to calculate LCM of two numbers
'''
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

a = n1 if n1 > n2 else n2

while True:
    if a % n1 == 0 and a % n2 == 0:
        print("Lcm is", a)
        break
    else:
        a += 1
'''

# Write a python script to calculate HCF of two numbers
'''
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

a = n1 if n1 > n2 else n2
b = n1 if n1 < n2 else n2
while True:
    c = a % b
    if c == 0:
        print(b)
        break
    elif b % c == 0:
        print(c)
        break
    else:
        a, b = b, c
'''
