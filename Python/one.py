# Day 1: Division and Square-root
# Write a function called divide_or_square that takes one
# argument (a number), and returns the square root of the number
# if it is divisible by 5, returns its remainder if it is not divisible by
# 5. For example, if you pass 10 as an argument, then your function
# should return 3.16 as the square root.

def divide_or_square(num):
    if num % 5 is 0:
        sqrt = num ** (1/2)
        return f'The squareroot of{num} is {sqrt}'
    else:  
        return num % 5
    
print(divide_or_square(10))
print(divide_or_square(21))

# Extra Challenge: Longest Value
# Write a function called longest_value that takes a dictionary
# as an argument and returns the first longest value of the
# dictionary. For example, the following dictionary should return
# – apple as the longest value.
# fruits = {'fruit': 'apple', 'color': 'green'}

def longest_value(d:dict):
    longest = max(d.values(), key=len)
    return longest

fruits = {'fruit':'apple', 'color':'green'}
(longest_value(fruits))