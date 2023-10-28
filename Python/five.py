# Day 5: My Discount
# Create a function called my_discount. The function takes no
# arguments but asks the user to input the price and the
# discount (percentage) of the product. Once the user inputs the
# price and discount, it calculates the price after the discount.
# The function should return the price after the discount. For
# example, if the user enters 150 as price and 15% as the discount,
# your function should return 127.5.

def my_discount():
    price=int(input('enter the price '))
    disc = int(input('Enter the discount in percentage '))
    return  price - price*(disc/100)

new_price = my_discount()
print(new_price)
# Extra Challenge: Tuple of Student Sex
# You work for a school and your boss wants to know how many
# female and male students are enrolled in the school. The school
# has saved the students in a list. Your task is to write a code that
# will count how many males and females are in the list. Here is a
# list below:
# students = ['Male', 'Female', 'female', 'male', 'male', 'male',
# 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
# Your code should return a list of tuples. The list above should
# return:
# [(‘Male’,7), (‘female’,6)]

def student_sex(lst:list):
    Male = 0
    female = 0
    for data in lst:
        if data.lower() == 'male':
            Male += 1
        else:
            female += 1

    tup = [('Male',Male),('Female',female)]
    return f'The summary is{tup}'

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
print(student_sex(students))