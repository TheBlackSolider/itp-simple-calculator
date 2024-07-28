def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The sum of the two numbers.
    """
    return a + b


def subtract(a, b):
    """
    Subtracts the second number from the first number and returns the result.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The difference between the two numbers.
    """
    return a - b


def multiply(a, b):
    """
    Multiplies two numbers and returns the result.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The product of the two numbers.
    """
    return a * b


def divide(a, b):
    """
    Divides the first number by the second number and returns the result.
    If the second number (denominator) is zero, returns an error message.

    Parameters:
    a (int, float): The numerator.
    b (int, float): The denominator.

    Returns:
    int, float, str: The quotient of the two numbers or an error message if division by zero.
    """
    if b == 0:
        return "Invalid value for denominator, can't divide by 0!"
    return a / b


def square(a):
    """
    Returns the square of a number.

    Parameters:
    a (int, float): The number to be squared.

    Returns:
    int, float: The square of the number.
    """
    return a * a


def power(a, b):
    """
    Raises the first number to the power of the second number and returns the result.

    Parameters:
    a (int, float): The base number.
    b (int, float): The exponent.

    Returns:
    int, float: The result of raising the base to the power of the exponent.
    """
    return a ** b


def sqrt(a):
    """
    Returns the square root of a number. If the number is negative, returns an error message.

    Parameters:
    a (int, float): The number to find the square root of.

    Returns:
    int, float, str: The square root of the number or an error message if the number is negative.
    """
    if a < 0:
        return "Invalid value for square root, input must be non-negative!"
    return a ** 0.5
