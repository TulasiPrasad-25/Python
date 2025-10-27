# first non repeting charector from a word returns its index
def Non_repet(s):
    count = {}
    for char in s:
        if char in count:
            count[char] +=1
        else:
            count[char] =1
    for i in range(len(s)):
        if count[s[i]]==1:
            
            return i
    return -1
t=Non_repet("sccucess")
print(t)

