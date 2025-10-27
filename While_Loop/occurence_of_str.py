string = "cccharecter"
charector = "c"
count =0
i = 1
while i <= len(string) -1:
    for char in string:
        if(char == charector):
            count +=1
        i +=1
    print(count)
     

     #or
while i <= len(string):
    if string[i] == charector:
        count += 1
    i +=1
print(count)
       

