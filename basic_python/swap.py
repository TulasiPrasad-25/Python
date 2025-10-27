 # swap with temp
a = 10
b = 20
temp = a
a = b
b = temp
print(a , b)

# without temp
a = a+b
b = a-b
a = a-b
print(a, b)

#simple way
a, b = b,a
print(a)