# Function to convert lowercase string to uppercase
def to_uppercase(text):
    result = ""
    for char in text:
        # Check if character is lowercase (between 'a' and 'z')
        if 'a' <= char <= 'z':
            # Convert to uppercase by subtracting 32 from ASCII value
            result += chr(ord(char) - 32)
        else:
            # Keep other characters as they are
            result += char
    return result

# Input from user
string = input("Enter a lowercase string: ")

# Call the function
upper_string = to_uppercase(string)

print("Uppercase string:", upper_string)
