def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if low_index >= high_index:
        return True
    elif word[low_index] != word[high_index]:
        return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# print(is_palindrome_recursive("osso", 0, 3))
# print(is_palindrome_recursive("reviver", 0, 6))
