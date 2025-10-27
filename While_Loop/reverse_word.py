word = "hello world"
for i in word :
    length = len(word) -1
    while len >= 0:
        print(word[len] , end = " ")
        length -=1
    print()