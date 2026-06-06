# Write a function that checks if a given string or number is a palindrome.

# Iterative Approach
def is_palindrome_iterative(text):
    text = str(text)
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

# Recursive Approach
def is_palindrome_recursive(text):
    text = str(text)
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome_recursive(text[1:-1])
value = input("Enter a string or number: ")
print("Iterative:", is_palindrome_iterative(value))
print("Recursive:", is_palindrome_recursive(value))
