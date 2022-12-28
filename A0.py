# Assignment 2
"""
Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py
"""

import A1 as a
import datetime as dt
import time as t

# print(a.a1)
d = dt.datetime.now()
t = t.ctime()
print(d, t, sep="\n")
