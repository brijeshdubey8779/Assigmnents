# python script to add comments and print “Learning Python” on screen.
import keyword
print("Learning Python")  # printing text on screen

# python script to add multi line comments and print values of four variables, each in a new line. Variable contains any values.
""" 
Lets create 3 variables named as x,y and z and assigne them random values or strings and print them
in new line using only one print statement
"""
x = 17
y = "Brijesh Dubey"
z = "ARMIET/CS20DB014"
print(f"Roll NO : {x} \nName : {y} \nPin : {z}")

# python script to print types of variables. Create 5 variables each of them containing different types of data.
a = 1
b = True
c = "Brijesh Dubey"
d = "3.33"
e = 2+3j
print(f"a:{a} is {type(a)} \nb:{b} is {type(b)} \nc:{c} is {type(c)} \nd:{d} is {type(d)} \ne:{e} is {type(e)}")

# python script to print the id of two variables containing the same integer values.
g = 5
f = 5
print(f"g:{g} has id : {id(g)}\nh:{f} has id : {id(f)}")

"""Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable"""
a = 1
c = "Brijesh Dubey"
d = "3.33"
e = 2+3j
print(f"a:{a} is {type(a)} and has id:{id(a)} \nc:{c} is {type(c)} and has id:{id(c)} \nd:{d} is {type(d)} and has id:{id(d)}  \ne:{e} is {type(e)} and has id:{id(e)} ")

# python script to print all the keywords
print(keyword.kwlist)
