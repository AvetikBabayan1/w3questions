"""
a = int(input("Please enter the number to proceed: "))
if (a>17):
    print(2*(abs(a-17)))
else:
    print(17-a)



#same with a method
def difference(n):
    if n > 17:
        print(2*(n-17))
    else:
        print(17-n)

n = int(input("Please enter the n number: "))
difference(n)

#method for a range to a number
def closeToRange(m):
    return ((abs(1000-m))<=100) or (abs((2000-m))<=100)
print(closeToRange(899))
print(closeToRange(900))
print(closeToRange(1000))
print(closeToRange(1100))
print(closeToRange(1101))
print(closeToRange(1899))
print(closeToRange(1901))
print(closeToRange(2000))
print(closeToRange(2100))
print(closeToRange(2101))
"""
#sum of given numbers, if they are equal - triple of the sum
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
c = int(input("Please enter the thirf number: "))
if a==b and a==c:
    print(3*(a+b+c))
else:
    print(a+b+c)