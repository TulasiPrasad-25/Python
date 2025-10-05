#this code is too smart 😂🤣
import random

print("Think of a number between 1 and 100, and I will try to guess it!")

low = 1
high = 100
attempts = 0

while True:
    
    guess = (low + high) // 2
    attempts += 1
    
    print(f"My guess is: {guess}")
    user_feedback = input("Is it too high (H), too low (L), or correct (C)? ").strip().upper()
    
    if user_feedback == "H":
        high = guess - 1
    elif user_feedback == "L":
        low = guess + 1
    elif user_feedback == "C":
        print(f"I guessed it! The number is {guess}. It took me {attempts} attempts.")
        break
    else:
        print("Please enter H, L, or C.")
