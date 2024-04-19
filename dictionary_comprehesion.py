def create_squared_numbers_dict(numbers):
    """
    Create a dictionary where the keys are the numbers from the given list and the values are the squares of those numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        dict: A dictionary where the keys are the numbers from the given list and the values are the squares of those numbers.
    """
    squared_numbers = {num: num**2 for num in numbers}
    return squared_numbers

numbers = [1, 2, 3, 4, 5]
squared_numbers = create_squared_numbers_dict(numbers)
print(squared_numbers)
numbers = [1, 2, 3, 4, 5]
squared_numbers = {num: num**2 for num in numbers}
print(squared_numbers)
