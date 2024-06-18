def factorial_iterative(num):
    if num < 0:
        return "Factorial does not exist for negative numbers"
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

# Example usage:
number = 7
print(f"The factorial of {number} is {factorial_iterative(number)}")
