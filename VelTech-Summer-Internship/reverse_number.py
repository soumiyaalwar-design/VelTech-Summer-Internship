# Write a Python program to reverse a number and calculate the sum of its digits.

# Iterative Approach
def reverse_and_sum(num):
    reverse = 0
    digit_sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        digit_sum += digit
        temp //= 10
    return reverse, digit_sum

# Recursive Sum of Digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

# Recursive Reverse
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)
number = int(input("Enter a number: "))
reverse_num, total = reverse_and_sum(number)
print("Iterative Reverse =", reverse_num)
print("Iterative Sum =", total)
print("Recursive Reverse =", reverse_number(number))
print("Recursive Sum =", sum_of_digits(number))
