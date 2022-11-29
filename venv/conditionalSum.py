"""
a = int(input("Please enter the first integer: "))
b = int(input("Please enter the second integer: "))
c = int(input("Please enter the third integer: "))
if (a==b) or (a==c) or (b==c):
    print ("As two integers are equal to each other, the sum will be equal to: ", 0)
else:
    print("The sum is ", a+b+c)
----------------------------------------------------
d = int(input("Please enter the first integer: "))
e = int(input("Please enter the second number: "))
if d+e > 15 and d+e < 20:
    print("As the sum is in non-acceptable range, the answer is: ", 20)
else:
    print("out of range, sum is: ", d+e)
----------------------------------------------------
f = int(input("Please enter the first number: "))
g = int(input("Please enter the secong digit: "))
if f==g or abs(f-g)==5 or abs(f+g==5):
    print(True)
else:
    print ("the sum is: ", f+g, "The difference is: ", abs(f-g), "And the numbers are not equal")

def add2numbers(a,b):
    if not (isinstance(a, int)) and (isinstance(b, int)):
        return ("Have to be integer")
    else:
        return (a+b)

print((add2numbers(3, 5)))
print((add2numbers(3, 5.5)))
print((add2numbers(3, 0)))
print((add2numbers("tweet", 5)))
print(add2numbers('5d', "dd"))

"""
def calcsquare(a, b):
    return(a+b)*(a+b)
a = int (input("Please enter the first integer"))
b = int (input("Please enter the second integer"))
print(calcsquare(a, b))