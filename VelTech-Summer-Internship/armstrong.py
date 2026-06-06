# Write a function to check if a number is an Armstrong number.

# Iterative Approach
def is_armstrong_iterative(num):
    power = len(str(num))
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    return total == num

# Recursive Approach
def armstrong_sum(num, power):
    if num == 0:
        return 0
    digit = num % 10
    return digit ** power + armstrong_sum(num // 10, power)
num = int(input("Enter a number: "))
power = len(str(num))
print("Iterative:", is_armstrong_iterative(num))
print("Recursive:", armstrong_sum(num, power) == num)
