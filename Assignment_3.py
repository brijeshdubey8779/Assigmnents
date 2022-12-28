# python script to convert a number into str type.
n = 17
print(n, type(n))
n = str(n)
print("After conversion\n", n, type(n))

# python script to print Unicode of the character ‘m’
print("Unicode of 'm' is :", ord('m'))

# python script to print character representation of a given unicode 100.
print("Symbol having unicode 100 is :", chr(100))

# a python script to print any number and its binary equivalent
print("Binary of 101 is :", bin(101))

# a python script to print any number and its octal equivalent.
print("Octal of 101 is :", oct(101))

# a python script to print any number and its hexadecimal equivalent.
print("Hexadecimal of 101 is :", hex(101))

# python script to store binary number 1100101 in a variable and print it in decimal format.
x = 0b1100101
print("Decimal of 1100101 is :", x)

# python script to store a hexadecimal number 2F in a variable and print it in octal format.
y = 0x2F
print(f"Octal of {hex(y)} is : ", oct(y))

# python script to store an octal number 125 in a variable and print it in binary format.
z = 0o125
print(f"Binary of {oct(z)} is : ", bin(z))

# python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and  display the result in binary format.
x = bin(0o25)
y = bin(0x39)
# x = bin(x)

print("Sum of 0o25 and 0x39 in binary is:", x)
