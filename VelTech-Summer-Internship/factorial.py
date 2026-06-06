# Write a program to compute the factorial of a number

# Iterative Approach
def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Recursive Approach
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial not defined for negative numbers.")
else:
    print("Iterative Factorial =", factorial_iterative(num))
    print("Recursive Factorial =", factorial_recursive(num))
