# Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list
'''
a = ['Java', 'Python', 'SQL', 'C']
print(a)
'''

# Write a python script to get the data type of a list.

# l = []
# print(type(l))

# Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
'''
mylist = ["Java", "C", "Python"]
print(mylist[-1])
'''

# Write a python script to Change the values "SQL" and "Reactnative" with the values
# "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

# l = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
# l[1] = 'NoSQL'
# l[3] = 'Flutter'
# print(l)

# Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"]

# mylist = ["Java", "SQL", "C", "Reactnative"]
# mylist.append('python')
# print(mylist)

# Write a python program to append elements from another list to the current list.(
# firstlist = ["Java", "Python", "SQL"]
# secondlist = ["C", "Cpp", "NoSQL"] )
'''
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]

for i in secondlist:
    firstlist.append(i)

print(firstlist)
'''

# Write a python program to Print all items by referring to their index number (thislist =
# ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
'''
l = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
for i in range(len(l)):
    print(l[i])
'''

# Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL",
# "C", "Reactjs", "Javascript", "Python"]
'''
l = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
l.sort()
print(l)
'''

# Write a Python script to create a list of city names taken from the user.
'''
l = []
n = int(input("How many cities you want to enter:"))

for i in range(n):
    l.append(input(f"Enter city {i+1}:"))
else:
    c = input("Want to add more cities?(y/n)")
    if c == "y" or c == "Y" or c == "yes" or c == "Yes":
        n = int(input("How many cities you want to enter:"))
        for i in range(n):
            l.append(input(f"Enter city {i+1}:"))
    else:
        break
print(l)
'''

# Write a Python script to create a list, where each element of the list is a digit of a given number.
'''
n = input("Enter a number:")
l = [i for i in n]
print(l)
'''
