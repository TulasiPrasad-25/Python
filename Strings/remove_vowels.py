word = input("enter a string: ")
vowels = "aeiouAEIOU"

for char in word:
    if char in vowels:
        word = word.replace(char , "")
    
print("final string is " , word)