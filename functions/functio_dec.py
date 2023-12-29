
name = "Ahmed"
def  printing_name():
    print("Hello", name)

printing_name()

print()
print()

def cylinder_volume(height, radius):
    pi = 3.14159
    return height  *pi*  radius ** 2
cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)


print()
print()


def population_density(population, land_area):
    return population/land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

print()
print("/////////////////////")
print()

def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))



print()
print()
# local variables
egg_count = 0

def buy_eggs(count):
     egg_count += 12 # error ocuur

# egg_count = buy_eggs(egg_count)
# print ("changing the local variables egg_count to {}" .format(egg_count))

print()
print()


egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)


print("the egg count is {}".format(egg_count))





