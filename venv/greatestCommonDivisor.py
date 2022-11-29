def gcd(x, y):
   gcd = 1
   if x % y == 0:
       return y
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break
   return gcd

x = int (input("Please enter the first positive integer: "))
y = int (input("Please enter the second positive integer: "))

print("The GCD for ", x, "and ", y, "is equal to: ", gcd(x,y))