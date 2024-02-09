# Standard Deviation Algorithm - 101computing.net/standard-deviation-algorithm
from math import sqrt


def inputList():
    number_list = []
    userInput = input("Enter a number to add to your list or 'x' to exit.")
    while userInput != "x":
        number_list.append(float(userInput))
        userInput = input("Enter a number to add to your list or 'x' to exit.")
    return number_list


def calculate_std_deviation(values: list[float]) -> float:
    number_of_values = len(values)
    mean = sum(values) / len(values)
    squared_differences = [pow(x - mean, 2) for x in values]
    sum_of_squared_differences = sum(squared_differences)
    division = sum_of_squared_differences / number_of_values
    standard_deviation = sqrt(division)
    return standard_deviation


# input_list = inputList()
input_list = [10, 12, 23, 23, 16, 23, 21, 16]
std_deviation = calculate_std_deviation(input_list)
print(f"The Standard Deviation is: {std_deviation}")
