# Write a python program to create and print a dictionary which stores your information.(name, age, gender .....)
'''
MyInfo = {'Name': "Brijesh Dubey", 'Age': 22,
          'Gender': "Male", 'Profession': "Student", }
print(MyInfo)
'''

# Write a python program to access the items of a dictionary by referring to its key name.
'''
MyInfo = {'Name': "Brijesh Dubey", 'Age': 22,
          'Gender': "Male", 'Profession': "Student", }
print(MyInfo['Name'])
'''

# Write a python program to get a list of the values from a dictionary.
'''
MyInfo = {'Name': "Brijesh Dubey", 'Age': 22,
          'Gender': "Male", 'Profession': "Student", }
print(MyInfo.values())
'''

# Write a python program to change the value of a specific item by referring to its key name.
'''
MyInfo = {'Name': "Brijesh Dubey", 'Age': 22,
          'Gender': "Male", 'Profession': "Student", }
MyInfo["Age"] = 21
print(MyInfo)
'''

# Write a python program to print all key names in the dictionary, one by one.
'''
MyInfo = {'Name': "Brijesh Dubey", 'Age': 22,
          'Gender': "Male", 'Profession': "Student", }
for k in MyInfo:
    print(k)
'''

# Write a python program to create a dictionary that contains three dictionaries.(nested)
'''
D = {"D1": {"A": "Neststed Dict 1"}, "D2": {
    "B": "Nested Dict 2"}, "D3": {"C": "Nested Dict 3"}}
print(D)
'''

# Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
'''
D1 = {"A": "Dict 1"}
D2 = {"B": "Dict 2"}
D3 = {"C": "Dict 3"}
D = {'D1': D1, "D2": D2, "D3": D3}
print(D)
'''

# Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
'''
l1 = ["Name", "Age", "Gender"]
l2 = ["Brijesh Dubey", 22, "Male"]
D = {}
i = 0
while i < len(l1):
    j = i
    D[l1[i]] = l2[j]
    i += 1
print(D)
'''

# Write a python program to merge two python dictionaries into one dictionary.
'''
D1 = {1: "One", 2: "Two"}
D2 = {3: "Three", 4: "Four"}
D1.update(D2)
print(D1)
'''

# Write a python program to get the key of lowest value from the dictionary.
# sample_dict = {
# 'C': 92,
# 'Java': 66,
# 'Python': 85
# }
'''
d = {'C': 92, 'Java': 66, 'Python': 85}
l = d.values()
m = min(l)
j = {i for i in d if d[i] == m}
print(j)
'''
