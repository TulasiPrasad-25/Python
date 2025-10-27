def Longest(s):
    words = s.split()

    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(Longest("i Love python programming"))