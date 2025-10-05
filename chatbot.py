import random
import datetime

response ={
    "hello" : ["hello","hello buddy!"],
    "hi" : ["hi there!","hi buddy","hi bro"],
    "how are you" :["ofcourse! iam fine, how about you","iam fine","iam fine and how are you?"],
    "what is your name" : ["you know...iam mashine idont have any name but also you can call by any name"],
    "bye" : ["bye have a great day","bye dude!"],
    "thanks":["thank you buddy","thanks"]
}

print("chatbot : hi there how can i help you today ?. type 'bye' to exit \n")
while True:
    user_input = input("user :-").lower().strip()

    if user_input == "bye":
        print("thnak you have a great day dear!")
        break
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f" CB :- current time is :- {current_time}")
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%B %d, %y")
        print(f" CB :- date is :- {current_date}")
    elif user_input in response:
        print(f"CB :- {random.choice(response[user_input])}")
    else:
        print("sorry, iam not that trained till ")
    
        
        