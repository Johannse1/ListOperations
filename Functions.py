# functions file
import collections


def sort_list(numbers):
    print("Sorted list from least to greatest: ", numbers.sort())


def sum_list(numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
        return sum
    print(f"The sum of the list is: {sum}")


def product_list(numbers):
    product = 1
    for number in numbers:
        product = product * number
        return product
    print(f"The product of the list is: {product}")


def mean_list(numbers):
    mean = 1
    for number in numbers:
        mean = mean * number
        return mean
    mean = mean / len(numbers)
    print(f"The mean of the list is: {mean}")


def median_list(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        first_median = numbers[len(numbers) // 2]
        second_median = numbers[len(numbers) // 2 - 1]
        median = (first_median + second_median) / 2
    else:
        median = numbers[len(numbers) // 2]
        return median
    print(f"The median of the list is: {median}")


def mode_list(numbers):
    data = collections.Counter(numbers)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode_val) == len(numbers):
        print("No mode in the list")
    else:
        print("The Mode of the list is : " + ', '.join(map(str, mode_val)))


def largest_num(numbers):
    numbers.sort()
    print("The largest number in the list is ", numbers[-1])


def smallest_num(numbers):
    numbers.sort()
    print("The smallest number in the list is: ", numbers[0])


def duplicates(numbers):
    numbers.sort()
    print("This is the list: ", numbers)
    num = input("Type a number you want to remove from the list: ")
    for number in numbers:
        if numbers[number] == num:
            numbers.replace(number, ' ')
            print("The new list: ", numbers)
        else:
            print("this number is not in the list.")


def remove_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            numbers.replace(number, ' ')
    print("list with evens removed: ", numbers)

def remove_odds(numbers):
    for number in numbers:
        if number %2 != 0:
            numbers.replace(number, ' ')
    print("list with odds removed: ", numbers)


def find_number(numbers):
    num = input("Type a number you want to find in the list: ")
    for number in numbers:
        if numbers[number] == num:
            print("yes, this number is in the list.")
        else:
            print("no, this number is not in the list.")


def bonus(numbers):
    numbers.sort()
    print("The second largest number in the list is: ", numbers[-2])
