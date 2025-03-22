def find_maximum(values):
    max_value = values[0]
    for i in range(1, len(values)):
        if values[i] > max_value:
            max_value = values[i]
    return max_value

numbers = [10, 3, 6, 8, 2]
max_number = find_maximum(numbers)
print(f"The maximum number is {max_number}")

more_numbers = []
max_more_numbers = find_maximum(more_numbers)
print(f"The maximum number in more numbers is {max_more_numbers}")
