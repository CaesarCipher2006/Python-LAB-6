def count_special_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count
strings = ["level", "ab", "abc", "radar", "hello", "noon"]
result = count_special_strings(strings)
print("Number of strings with the required conditions:", result)
