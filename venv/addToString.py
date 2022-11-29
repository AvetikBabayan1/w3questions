"""
#check if some string contains another and do some actions if it contains
a = "Is"
b = input("Please enter any string: ")
if a in b:
    print(b)
else:
    print(a+ " " +b)

#multiply the string given number of time

a = input(" This is the string:  ")
b = int(input("Please provide number to multiply: "))

print(a*b)
"""

a = input(" Please enter the string: ")
b = int(input("Please enter the integer: "))
if len(a) <2:
    print(b*a)
else:
    print(b*(a[0:2]))