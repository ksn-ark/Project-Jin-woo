import math
for i in range (1, 101):
  result = math.ceil(i*2.5)
  if result % 3 == 0:
    
    print(i)
    print(result)
    print("divisible")