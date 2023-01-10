# Write a python script to store multiple items in a single variable(Items are “Java”, “Python”, “SQL”, “C”) using tuple
'''
t = ('Java', 'Python', 'SQL', 'C')
print(t)
'''

# Write a python program to store only one item using tuple.
'''
t = ('Brijesh',)
print(t, type(t))
'''

# Write a python program to reverse the tuple.
'''
t = tuple(eval(e)
          for e in input("Enter the items sperated by comma").split(','))
print(t[::-1])
'''

# Write a python program to Swap two tuples in Python.
'''
t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)

t1, t2 = t2, t1
print(f't1={t1} \nt2={t2}')
'''

# Write a python program to check if all items in the tuple are the same.
'''
t = tuple(eval(e)
          for e in input("Enter the items sperated by comma").split(','))

l = len(t)
if t.count(t[0]) == l:
    print("All elements are same")
else:
    print("All elements are not same")
'''

# Write a python program to divide the tuple into four variables. tuple1=(100, 200, 300, 400)
'''
tuple1 = (100, 200, 300, 400)

a, b, c, d = tuple1
print(a, b, c, d, sep='\n')
'''

# Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)
'''
tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (tuple1[4:6:1])
print(tuple2)
'''

# Write a python program to Sort a tuple of tuples by the second item. tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
'''
tuple1 = (('a', 21), ('b', 37), ('c', 11), ('d', 29))
t = sorted(tuple1, key=lambda x: x[1])
t1 = tuple(t)
print(t1)
'''

# Write a python program to print the value 20 from given nested tuple tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
'''
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

for i in tuple1:
    for j in i:
        if j == 20:
            print(j)
            break
'''

# Write a python program to change the first item (22) of a list within the following tuple to 222.
'''
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)
'''
