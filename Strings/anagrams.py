# Input two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Check if lengths are equal first (quick elimination)
if len(str1) != len(str2):
    print("The strings are not anagrams.")
else:
    # Create empty dictionaries to count frequency of each character
    count1 = {}
    count2 = {}

    # Count frequency of characters in first string
    for ch in str1:
        count1[ch] = count1.get(ch, 0) + 1

    # Count frequency of characters in second string
    for ch in str2:
        count2[ch] = count2.get(ch, 0) + 1

    # Compare both dictionaries
    if count1 == count2:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
