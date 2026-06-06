# Write a Python function to count the number of vowels and consonants in a given string.

# Iterative Approach
def count_iterative(text):
    vowels = 0
    consonants = 0
    for ch in text.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants


# Recursive Approach
def count_recursive(text, index=0):
    if index == len(text):
        return 0, 0
    vowels, consonants = count_recursive(text, index + 1)
    ch = text[index].lower()
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
    return vowels, consonants
text = input("Enter a string: ")
v1, c1 = count_iterative(text)
v2, c2 = count_recursive(text)
print("\nIterative Approach")
print("Vowels =", v1)
print("Consonants =", c1)
print("\nRecursive Approach")
print("Vowels =", v2)
print("Consonants =", c2)
