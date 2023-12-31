

f = open("./file.txt",'r')
read_data = f.read()
# print(read_data)


""""
With
Python provides a special syntax that auto-closes a file for you once you're finished using it.
"""

with open('another.txt', 'r') as f:
    file_data = f.read()



# reading line by line
camelot_lines = []
with open("names.txt") as f:
    for line in f:
    
        camelot_lines.append(line.strip())

for name in camelot_lines:
    print(name)
