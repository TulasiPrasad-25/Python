sentence = " i love cricket and football"
word = sentence.split()

longest_word = word[0]

for char in word:
    if len(char) > len(longest_word):
        longest_word = char
print(longest_word)
print(len(longest_word))
