def getUserInputAsList():
    n = int(input("Enter number of elements : "))
    # Below line read inputs from user using map() function
    lst = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
    return lst

def listToString(dataList):
    result=''
    for data in dataList:
        result+=str(data)
    return result

print("String of the list entered is: ", listToString(getUserInputAsList()))