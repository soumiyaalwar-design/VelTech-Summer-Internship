# Write a Python program to print the first N numbers in the Fibonacci series.

# Iterative Approach
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Recursive Approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = int(input("Enter N: "))
print("\nIterative Fibonacci Series:")
fibonacci_iterative(n)
print("\nRecursive Fibonacci Series:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
