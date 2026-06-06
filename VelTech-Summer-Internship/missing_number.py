# Given a list of N-1 elements from a range 1 to N, find the missing number.

# Recursive Sum Function
def recursive_sum(numbers, index=0):
    if index == len(numbers):
        return 0
    return numbers[index] + recursive_sum(numbers, index + 1)
n = int(input("Enter N: "))
numbers = list(map(int, input("Enter N-1 numbers separated by spaces: ").split()))
expected_sum = n * (n + 1) // 2
actual_sum_iterative = sum(numbers)
actual_sum_recursive = recursive_sum(numbers)
print("\nIterative Approach")
print("Missing Number =", expected_sum - actual_sum_iterative)
print("\nRecursive Approach")
print("Missing Number =", expected_sum - actual_sum_recursive)
