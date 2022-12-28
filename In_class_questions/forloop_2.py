# print the string entered by user until 'r' appres and print all charaters printed succesfully if whole string is printed

a = input("Enter a string:")
for i in a:
    if i == 'r' or i == 'R':
        break
    print(i, end=' ')
else:
    print('\nAll charaters printed succesfully')
