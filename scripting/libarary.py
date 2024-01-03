import math
import datetime 
# thirdparty labarary
# install pytz  like this pip install pytz
import pytz
utc = pytz.utc
# factorial
print("the facorial of 5 is",math.factorial(5))
print("the facorial of 4 is",math.factorial(4))
print("the facorial of 7 is",math.factorial(7))
print("the facorial of 9 is",math.factorial(9))

print()
# power numbers
print("the powe of 5 to 2 is",math.pow(5,2))
print("the powe of 7 to 3 is",math.pow(7,3))
print("the powe of 3 to 2 is",math.pow(3,2))
print("the powe of 9 to 3 is",math.pow(9,3))

print()
# Return the square root of x.

print("the square root of 9 is", int(math.sqrt(9)))
print("the square root of 24 is", int(math.sqrt(24)))
print("the square root of 36 is",int(math.sqrt(36)))
print()
print("datetime now is",datetime.datetime.now(tz= utc))