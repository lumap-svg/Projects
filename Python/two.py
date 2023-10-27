# Day 2: Strings to Integers
# Write a function called convert_add that takes a list of strings
# as an argument and converts it to integers and sums the list. For
# example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
# summed to 9.

def convert_add(lst:list):
    a =[ int(val) for val in lst]
    print(sum(a))

lsty = ['1', '3', '5']
convert_add(lsty)
        

# Extra Challenge: Duplicate Names
# Write a function called check_duplicates that takes a list of
# strings as an argument. The function should check if the list has
# any duplicates. If there are duplicates, the function should return
# the duplicates. If there are no duplicates, the function should
# return "No duplicates". For example, the list of fruits below
# should return apple as a duplicate and list of names should
# return "no duplicates".
# fruits = ['apple', 'orange', 'banana', 'apple']
# names = ['Yoda', 'Moses', 'Joshua', 'Mark']
def check_duplicates(arr:list):
    duplicates = [ data for data in arr if arr.count(data) > 1]
    # for item in arr:
    #     if arr.count(item) > 1:
    #         duplicates.append(item)
    
    if len(duplicates) == 0:
        return f'There are {len(duplicates)} duplicates'
    else:
        return f'the duplicates are{duplicates}'


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

print(check_duplicates(fruits))
print(check_duplicates(names))