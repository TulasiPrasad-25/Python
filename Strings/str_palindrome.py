str = "malayalam"

if str== str[::-1]:
    print(f"{str} is palindrome")
else:
    print("not a palindrome")

#another method

word = "malayalam"
reverse = ""

for char in word:
    reverse = char+reverse
if word == reverse:
    print(f"{word} is a palindrome")
else:
    print("not a palindrome")