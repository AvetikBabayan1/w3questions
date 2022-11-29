def isInList(aList, n):
    for a in aList:
        if n ==a:
            return True
    return False

print(isInList([1,3,5,6,7], 4))
print(isInList([1,3,5,6,7], 5))