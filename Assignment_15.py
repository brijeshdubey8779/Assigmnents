# Write a python script to create a String in 3 different possible ways
'''
s1 = 'Hello, this is first string.'
s2 = str('Hello, this is second string.')
s3 = str(1250)
print(s1, s2, s3, sep='\n')
'''


# 2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)
'''
s = 'iNeuron'
print(s[:6:])
'''

# Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)
'''
s = 'Hello Learners'
print(s[2:6:1])
'''

# Write a python script to demonstrate String Concatenation adding space in between (Given Strings a=”Learning” b=”Python” )
'''
a = 'Learning'
b = 'Python'
print(a + ' ' + b)
'''

# Write a python script to get the count of total number of characters in String a=“iNeuron”
'''
a = 'iNeuron'
print(len(a))
'''

# Write a python script to reverse a String. (“iNeuron”)
'''
s = 'iNeuron'

print(s[::-1])
'''

# Write a python script to determine whether a string contains a specific substring.
'''
s = input('Enter a string:\n')
s1 = input("Enter the substring you want to search:")
if s1 in s:
    print(f"{s1} is present in {s}")
'''

# Write a python script to check if a string contains only numbers.
'''
s = input('Enter a string:\n')
if s.isdigit():
    print("String contains only numbers.")
else:
    print("String contains characters and numbers.")
'''

# Write a python script to check if a string contains only characters of the alphabet.
'''
s = input('Enter a string:\n')
if s.isalpha():
    print("String contains only characters.")
else:
    print("String contains characters and numbers.")
'''

# Write a python script to convert an integer to a string.
'''
a = int(input("Enter a number:"))
a = str(a)
print(a, type(a))
'''
