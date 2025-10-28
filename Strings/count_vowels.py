word = "beauti ful12 45 "
vowels = consonents = digits = spaces = 0
vow = "aeiouAEIOU"
for char in word:
    if char in vow:
        vowels +=1
    elif char.isalpha():
        consonents +=1
    elif char.isdigit():
        digits +=1
    elif char.isspace():
        spaces +=1

print(vowels , consonents , digits , spaces)