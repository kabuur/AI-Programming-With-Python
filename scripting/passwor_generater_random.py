# TODO: First import the `random` module
import random
# We begin with an empty `word_list`
word_file = "file.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower().split()
        # print(word)
        # don't include words that are too long or too short
        for one_word in word:
            if 3 < len(one_word) < 8:
                word_list.append(one_word)
              

# TODO: Add your function generate_password below
print(word_list)
def generate_password():
    return ''.join(random.sample(word_list, 3))
# def generate_password():
#     return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

# It should return a string consisting of three random words 
# concatenated together without spaces

# Now we test the function
password = generate_password()

print(password )