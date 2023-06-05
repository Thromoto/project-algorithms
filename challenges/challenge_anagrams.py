def merge_sort(word, start=0, end=None):
    if end is None:
        end = len(word)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(word, start, mid)
        merge_sort(word, mid, end)
        merge(word, start, mid, end)


def merge(word, start, mid, end):
    left = word[start:mid]
    right = word[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            word[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            word[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            word[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            word[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    str1 = list(first_string.lower())
    str2 = list(second_string.lower())

    merge_sort(str1)
    merge_sort(str2)

    string1 = "".join(str1)
    string2 = "".join(str2)

    if len(string1) != len(string2):
        return (string1, string2, False)
    elif string1 == "" and string2 == "":
        return (string1, string2, False)
    else:
        return (string1, string2, string1 == string2)
