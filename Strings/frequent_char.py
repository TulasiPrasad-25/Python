def repeating_char(s):
    count = {}
    
    # Count frequency of each character
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    max_char = ""
    max_count = 0

    # Find character with maximum frequency
    for char, freq in count.items():
        if freq > max_count:
            max_count = freq
            max_char = char

    return max_char, max_count


# Example
string = "programming"
char, freq = repeating_char(string)
print(f"The most frequent character is '{char}' which appears {freq} times.")
