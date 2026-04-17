#TASK-1
"""def factorial(n):
    result = 1
    for i in range(1, n):
        result = result * i
    return result """
#MODIFIED CODE
"""def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
print(factorial(5))"""
#Original: range(1, n) iterates from 1 to n-1, so factorial(5) calculates 1×2×3×4 = 24
#Modified: range(1, n + 1) iterates from 1 to n, so factorial(5) correctly calculates 1×2×3×4×5 = 120

#TASK-2 
"""def calc(a, b, c):
    if c == "add":
        return a + b
    elif c == "sub":
        return a - b
    elif c == "mul":
        return a * b
    elif c == "div":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
print(calc(10, 5, "add"))  # Output: 15
print(calc(10, 5, "sub"))  # Output: 5
print(calc(10, 5, "mul"))  # Output: 50
print(calc(10, 5, "div"))  # Output: 2.0"""

#TASK-3
"""def Checkprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        return True"""
#MODIFIED CODE
"""def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True"""
#Original: The function incorrectly returns True after the first iteration, which is not correct for numbers greater than 2.
#Modified: The function now correctly checks all numbers from 2 up to the square root of n, and only returns True if no divisors are found, ensuring accurate prime number checking.


#TASK-4
"""def processData(d):
    return [x * 2 for x in d if x % 2 == 0]"""
#MODIFIED CODE
"""def filter_and_multiply(data: List[Union[int, float]], multiplier: int = 2, filter_even: bool = True) -> List[Union[int, float]]:
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    
    if not data:  # Handle empty list
        return []
    
    try:
        result = []
        for x in data:
            if not isinstance(x, (int, float)):
                raise TypeError(f"List contains non-numeric element: {x}")
            
            condition = (x % 2 == 0) if filter_even else (x % 2 != 0)
            if condition:
                result.append(x * multiplier)
        return result
    except TypeError as e:
        raise TypeError(f"Error processing data: {e}")

# Usage examples:
print(filter_and_multiply([1, 2, 3, 4, 6]))  # [4, 8, 12]
print(filter_and_multiply([1, 2, 3, 4], multiplier=3))  # [6, 12]
print(filter_and_multiply([1, 2, 3, 4], filter_even=False))  # [2, 6]"""
#original: The function processes a list of numbers, multiplying even numbers by 2 and ignoring odd numbers.
#modified: The function now includes type annotations, error handling for non-list inputs and non-numeric elements, and allows for customizable multiplier and filter options, making it more robust and flexible.

'''#TASK-5
# ORIGINAL (BUGGY) VERSION
def sum_of_squares_original(numbers: List[int]) -> int:
    total = 0
    for num in numbers:
        total += num ** 2
        return total
# TASK-5
# MODIFIED (CORRECTED) VERSION
def sum_of_squares(numbers: List[int]) -> int:
    total = 0
    for num in numbers:
        total += num ** 2
    return total

# Usage example:
print(sum_of_squares([1, 2, 3, 4, 5]))  # Output: 55'''