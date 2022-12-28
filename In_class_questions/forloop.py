# counting number of character repeated in a given string
st = input("Enter a string")
count = input("which variable you want to count in given string")
no = 0
for i in st:
    if count == i:
        no += 1
print(no)
