# Write a program to check if two strings are anagrams of each other.

# Iterative Approach
def anagram_iterative(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

# Recursive Sorting Function
def recursive_sort(text):
    if len(text) <= 1:
        return text
    pivot = text[0]
    left = ''.join([char for char in text[1:] if char <= pivot])
    right = ''.join([char for char in text[1:] if char > pivot])
    return recursive_sort(left) + pivot + recursive_sort(right)

# Recursive Anagram Check
def anagram_recursive(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return recursive_sort(str1) == recursive_sort(str2)
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
print("\nIterative Approach")
if anagram_iterative(string1, string2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")
print("\nRecursive Approach")
if anagram_recursive(string1, string2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")
