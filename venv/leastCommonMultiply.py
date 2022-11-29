def lcm(x, y):
  if x > y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1
  return lcm
x = int(input("Please enter the first positive integer: "))
y = int(input("Please enter the second positive integer: "))
print(lcm(x,y))