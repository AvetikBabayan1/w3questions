#script to receive a single symbol integer(x) and return the format xxx+xx+x
"""""
def calc(x):
    return x*100+2*x*10+3*x

print (calc(1))
print (calc(2))
print (calc(3))
print (calc(4))
print (calc(5))
print (calc(6))
print (calc(7))
print (calc(8))
print (calc(9))


def calc2(x):
    return(x*1000+2*x*100+3*x*10+4*x)
print (calc2(1))
print (calc2(2))
print (calc2(3))
print (calc2(4))
print (calc2(5))
print (calc2(6))
print (calc2(7))
print (calc2(8))
print (calc2(9))


def evenOrOdd(n):
    if n%2==0:
        print("The given number is even ")
    else:
        print("The given number is odd ")

n = int(input("Enter the number to check if it is even "))
evenOrOdd(n)

"""

def countNumberFromTheList(numList):
    count = 0
    for n in numList:
        if n ==4:
            count+=1
    return count

print(countNumberFromTheList([3,4,2,3,4,2,4]))