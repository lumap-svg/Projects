# Day 4: Only Floats
# Write a function called only_floats, which takes two
# parameters a and b, and returns 2 if both arguments are floats,
# returns 1 if only one argument is a float, and returns 0 if neither
# argument is a float. If you pass (12.1, 23) as an argument, your
# function should return a 1.

def only_floats(a, b):
    if (type(a) and type(b)) is float:
        return 2 
    elif (type(a) or type(b)) is float:
        return 1
    else:
        return 0
    
print(only_floats(12.1, 23))

# Extra Challenge: Index of the Longest Word
# Write a function called word_index that takes one argument,
# a list of strings and returns the index of the longest word in the
# list. If there is no longest word (if all the strings are of the same
# length), the function should return zero (0). For example, the list
# below should return 2.
# words1 = ["Hate", "remorse", "vengeance"]
# And this list below, shoul return zero (0)
# words2 = ["Love", "Hate"]

def word_index(a):
    length = 0
    lgth = []
    for item in a:
        lgth.append(len(item))
        if len(item) > length:
            length = len(item)
    if len(set(lgth)) == 1:
        return f'Zero {0}'
    else:
        return f'The longest word has {length} words'   

words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

print(word_index(words1))
print(word_index(words2))