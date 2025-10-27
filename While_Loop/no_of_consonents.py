vowels = "aeiou"
count = 0
index = 0
word = "tulasiprasad"

while index < len(word):
    if word[index] not in vowels:
        count +=1
    index += 1
print(count)