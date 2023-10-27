# Day 3: Register Check
# Write a function called register_check that checks how many
# students are in school. The function takes a dictionary as a
# parameter. If the student is in school, the dictionary says ‘yes’. If
# the student is not in school, the dictionary says ‘no’. Your
# function should return the number of students in school. Use the
# dictionary below. Your function should return 3.
# register = {'Michael':'yes','John': 'no',
# 'Peter':'yes', 'Mary': 'yes'}
def register_check(dct:dict):
    count = 0
    for item in dct.values():
        if item == 'yes':
            count += 1

    return count



register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}
print(register_check(register))

# Extra Challenge: Lowercase Names
# names = ["kerry", "dickson", "John", "Mary",
# "carol", "Rose", "adam"]
# You are given a list of names above. This list is made up of names
# of lowercase and uppercase letters. Your task is to write a code
# that will return a tuple of all the names in the list that have only
# lowercase letters. Your tuple should have names sorted
# alphabetically in descending order. Using the list above, your
# code should return:
# ('kerry', 'dickson', 'carol', 'adam')

def lowercase_name(lst:list):
    print(lst)
    a = [ name for name in sorted(names, reverse=True) if name.islower()]
    b = tuple(a)
    print(b)



names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
lowercase_name(names)