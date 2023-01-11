# Write a python program to store all the programming languages known to you using Set.
'''
s = {'c', 'c++', 'python', 'java', 'kotlin',
     'golang', 'Javascript', 'dottnet', 'R', 'ruby', }
print(s)
'''

# Write a python program to store your own information {name, age, gender, so on..}
'''
s = {"Brijesh Dubey", '22 year old', 'Male',
     'Computer Engineer', 'Student', 'Armiet collage', }
print(s)
'''

# Write a python script to get the data type of a Set.
'''
s = {1, 2, 'its a set'}
print(f"Type of {s} is {type(s)}")
'''

# Write a Python script to find if “Python” is present in the set this set = {"Java","Python", "Django"}
'''
s = {"Java", "Python", "Django"}
if 'Python' in s:
    print(f"Python is present in set={s}")
'''

# Write a python program to add items from another set to the current set. thisset ={"Java", "Python", "SQL"} secondset= {"C", "Cpp", "NoSQL"}
'''
s2 = {"Java", "Python", "SQL"}
s1 = {"C", "Cpp", "NoSQL"}
for i in s2:
    s1.add(i)
print(s1)
'''

# Write a python program to add elements of list to a set
# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]
'''
s = {"Python", "Django", "JavaScript"}
l = ["Java", "C"]

for i in l:
    s.add(i)
print(s)
'''

# Write a python program to remove last item of the given set
# thisset = {"Python", "Django", "JavaScript", “SQL”}
'''
s = {"Python", "Django", "JavaScript", "SQL"}
s.pop()
print(s)
'''

# Write a python program to delete the set completely.
'''
s = {1, 3, 3.44, "Hello Python"}
s.clear()
print(s)
'''

# Write a python program to loop through the set and print values
# thisset = {"Python", "Django", "JavaScript", “SQL”}
'''
s = {"Python", "Django", "JavaScript", "SQL"}
for e in s:
    print(e)
'''

# Write a python program to find the maximum and minimum value in a set.
'''
s = {int(i) for i in input("Enter numbers separated by comma:").split(',')}
print(f"Minimum value:{min(s)} and maximum value is:{max(s)}")
'''
