#count number of vowels in a string
count =0
vowels = "aeiouAEIOU"
word = "Beautiful"
for char in word:
    if (char in vowels):
        count +=1
print(count)