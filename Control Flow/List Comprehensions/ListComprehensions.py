
squires = [x ** 2 for x in range(10)]

print("list of squires from 0,9",squires)


check_Odd_squires  = [x ** 2  if x % 2 == 0 else x+3 for x in range(10)]
print("check_Odd_squires" , check_Odd_squires)

Odd_squires  = [x ** 2  for x in range(10) if x % 2 == 0]

print("list of Odd Squires number is ", Odd_squires)