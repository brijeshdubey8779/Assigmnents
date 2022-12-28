# Write a python script to print the first 10 multiples of 5.
'''
for i in range(1, 11):
    print(i*5)
'''

# Write a python script to print first 10 multiples of N
'''
i = int(input("Enter the number you want table of:"))
for n in range(1, 11):
    print(n*i)
'''

# Write a python script to print first M multiples of N.
'''
n = int(input("Enter the numbr you want table of:"))
m = int(input("How multiplier you want:"))

for i in range(1, m+1):
    print(n*i)
'''

# Write a python script to print the first 10 multiples of N in reverse order.
'''
n = int(input("Enter the numbr you want table of in reverse order:"))

for i in range(10, 0, -1):
    print(i*n)
'''

# Write a python script to print table of user’s choice
'''
n = int(input("Enter the numbr you want table of:"))

for i in range(1, 11):
    print("%d*%d=%d" % (n, i, n*i))
'''

# Write a python script to print first N even natural numbers.
'''
n = int(input("Enter a number:"))

for i in range(1, 2*n+1):
    if i % 2 == 0:
        print(i)
'''

# Write a python script to print first N odd natural numbers.
'''
n = int(input("Enter a number:"))

for i in range(1, 2*n+1):
    if i % 2 != 0:
        print(i)
'''

# Write a python script to print squares of first N natural numbers.
'''
n = int(input("Enter a number:"))

for i in range(1, n+1):
    print(i**2)
'''

# Write a python script to print cubes of first N natural numbers.
'''
n = int(input("Enter a number:"))

for i in range(1, n+1):
    print(i**3)
'''

# Write a python script to display all prime numbers within a range.
# * range
# start = 15
# end = 45
'''
count = 0
for i in range(15, 45):
    for j in range(1, i//2):
        if j == 1:
            continue
        elif i % j == 0:
            break
        else:
            continue
    else:
        print(i)
'''
