text = "Hello World"
toggled_text = ""

for char in text:
    if char.islower():
        toggled_text += char.upper()
    elif char.isupper():
        toggled_text += char.lower()
    else:
        toggled_text += char
print(toggled_text)