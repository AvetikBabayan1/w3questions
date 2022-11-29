import math
def distanceCalculation(x1, x2, y1, y2):
    distance = math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    return distance

x1 = int(input("Please enter the x1 value: "))
x2 = int(input("Please enter the x2 value: "))
y1 = int(input("Please enter the y1 value: "))
y2 = int(input("Please enter the y2 value: "))
print("The first point coordinates are: ", x1, ":", y1)
print("The second point coordinates are: ", x2, ":", y2)
print("The distance between two points is equal to: ",  distanceCalculation(x1,x2,y1,y2))