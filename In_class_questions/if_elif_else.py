# write a python program to print grade obtained in a test. Take marks obtainbed from user to display the grade

m = int(input("Enter your marks"))

if 100 >= m > 90:
    print("A grade")
elif 90 >= m > 80:
    print("B grade")
elif 80 >= m > 70:
    print("C grade")
elif 70 >= m > 60:
    print("D grade")
elif 60 >= m > 50:
    print("E grade")
else:
    print("F grade")
