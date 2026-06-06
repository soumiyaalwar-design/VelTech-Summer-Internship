# Write a program to check if a number is prime, and print all primes between 1 and 100.

# Iterative Approach
def is_prime_iterative(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Recursive Approach
def is_prime_recursive(num, divisor=2):
    if num < 2:
        return False
    if divisor > int(num ** 0.5):
        return True
    if num % divisor == 0:
        return False
    return is_prime_recursive(num, divisor + 1)
number = int(input("Enter a number: "))
print("Iterative:", is_prime_iterative(number))
print("Recursive:", is_prime_recursive(number))
print("\nPrime Numbers from 1 to 100:")
for i in range(1, 101):
    if is_prime_iterative(i):
        print(i, end=" ")
