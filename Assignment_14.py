# Write a Python script to create a list of first N natural numbers.
'''
n = int(input("How many natural numbers you want in the list:"))
l = [i for i in range(1, n+1)]
print(l)
'''

# Write a Python script to create a list of first N odd natural numbers.
'''
n = int(input("How many odd natural numbers you want in the list:"))
l = []

for i in range(1, 2*n+1):
    if i % 2 != 0:
        l.append(i)
print(l)
'''

# Write a Python script to create a list of first N even natural numbers.
'''
n = int(input("How many even natural numbers you want in the list:"))
l = []

for i in range(1, 2*n+1):
    if i % 2 == 0:
        l.append(i)
print(l)
'''

# Write a Python script to find the greatest number in a given list of numbers.
'''
l = eval(input('Enter the list of numbers:'))
print(max(l))
'''

# Write a Python script to find the smallest number in a given list of numbers.
'''
l = eval(input('Enter the list of numbers:'))
print(min(l))
'''

# Write a Python script to calculate the sum of elements in a given list of numbers.
'''
l = eval(input('Enter the list of numbers:'))
print(sum(l))
'''

# Write a Python script to remove all non int values from a list.

'''
l1 = [int(i) for i in eval(input('Enter the list:')) if type(i) == int]
print(l1)
'''

# Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
'''
l = [e for e in eval(input('Enter the list:'))]
l1 = []
for i in l:
    c = l.count(i)
    if c > 1:
        if i not in l1:
            l1.append(i)
            print(i, 'has frequncy of', c)
    else:
        print(i, 'has frequncy of', c)
'''

# Write a Python script to print indices of all occurrences of a given element in a given list.
'''
l = [e for e in eval(input('Enter the list:'))]
l1 = []
ln = len(l)
lo = []
for i in l:
    if i not in l1:
        l1.append(i)
        j = 0
        while j < ln:
            if l[j] == i:
                lo.append(j)
            j += 1
        print(f'{i} has occurance at {lo}')
        lo.clear()
'''

# Write a python script to sort a list.
'''
l = [e for e in eval(input('Enter the list:'))]
l.sort()
print(l)
'''
