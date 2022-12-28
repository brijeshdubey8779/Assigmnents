# Write a python script to calculate sum of first N natural numbers
'''
n = int(input("Enter the number:"))
j = 0
for i in range(1, n+1):
    j = j+i
print(j)
'''

# Write a python script to calculate sum of squares of first N natural numbers
'''
n = int(input("Enter the number:"))
j = 0
for i in range(1, n+1):
    j = j+i**2
print(j)
'''

# Write a python script to calculate sum of cubes of first N natural numbers
'''
n = int(input("Enter the number:"))
j = 0
for i in range(1, n+1):
    j = j+i**3
print(j)
'''

# Write a python script to calculate sum of first N odd natural numbers
'''
n = int(input("Enter the number:"))
j = 0
for i in range(1, n+1):
    if i % 2 != 0:
        j = j+i
print(j)
'''

# Write a python script to calculate sum of first N even natural numbers
'''
n = int(input("Enter the number:"))
j = 0
for i in range(1, n+1):
    if i % 2 == 0:
        j = j+i
print(j)
'''

# Write a python script to calculate factorial of a given number
'''
n = int(input("Enter the number:"))
j = 1
for i in range(1, n+1):
    j = j*i
print(j)
'''

# Write a python script to count digits in a given number
'''
n = int(input("Enter the number:"))
count = 0
for i in str(n):
    count += 1
print(count)
'''

# Write a python script to calculate sum of digits of a given number
'''
n = int(input("Enter the number:"))
count = 0
for i in str(n):
    i = int(i)
    count = count + i
print(count)
'''

# Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
'''
n = int(input("Enter the number:"))
j = 0
s = ""
while n >= 1:
    j = n % 2
    s = s+str(j)
    n = n//2
l = len(s)
for i in range(l-1, -1, -1):
    print(s[i], end='')
'''

# Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
'''
n = int(input("Enter the octal number:"))
count = len(str(n))
# while n != 0:
#     n //= 10
#     count += 1
# # print(count)
num = 0
for i in range(0, count):
    x = n % 10
    num = num+x*8**i
    n //= 10
print(num, end='')
'''
