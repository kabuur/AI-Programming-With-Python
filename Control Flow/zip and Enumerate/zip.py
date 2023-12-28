list1 = list(zip(['a', 'b', 'c'], [1, 2, 3]))
print(list1)


#unzip the list
leters1, numbers1 = zip(*list1)

print("this is the numbers when unziped", numbers1)


print()
print("MWTHOD 2")
print()

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))