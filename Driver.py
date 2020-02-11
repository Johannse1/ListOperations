# Evan Johanns
# List operations
# 02/10/20
import Functions

numbers = []
i = 0
print(" welcome to the program, you will now be asked to enter 5 numbers.")
input("press enter to continue")
while i < 5:                    # while loop for amount of #'s in list
    numbers.append(input("please enter a number: "))
    i = i + 1

Functions.sort_list(numbers)
Functions.sum_list(numbers)
Functions.product_list(numbers)
Functions.mean_list(numbers)
Functions.median_list(numbers)
Functions.mode_list(numbers)
Functions.largest_num(numbers)
Functions.smallest_num(numbers)
Functions.duplicates(numbers)
Functions.remove_even(numbers)
Functions.remove_odds(numbers)
Functions.find_number(numbers)
Functions.bonus(numbers)






