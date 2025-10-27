import numpy as np

print(" \n array opeerations \n")

range = np.arange(0,10+1)
print(range)

arr1 = np.linspace(0,1,5)
print(arr1)

arr2 = np.zeros([2,4])
print(arr2)

arr3 = np.ones([2,4])
print(arr3)

arr4 = np.full([2,4] ,7)
print(arr4)

print("\n random \n")
arr5 = np.random.rand(5) #generates 10 random numbers between 0 and 1
print(arr5)

arr6 = np.random.randint(1 , 10 , size=(2,3)) #numbers between 1 to 1-0 for 2 rows and theree columns
print(arr6)

print("\n reshape \n")

arr7 = np.array([1,2,3,4,5,6])
reshaped = arr7.reshape([2,3])
print(reshaped)

#arithemetic operations

print(" \n arithemetic operations \n")
a= np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a-b)
print(a*b)
print(a/b) #it will return float values as a result
print(a//b) #it will return integer values as a reasult
print(a%b) #Gives remainder
print(a**b) #power of


#universal functions --> ufuncs

print("\n ufuncs \n")
arr8 = np.array([1,4,9,16])
print(np.sqrt(arr8))
print(np.exp([1,2]))

print("\n ****(imp) indexing and slicing :- \n")

arr9 = np.array([2,5,7,9,6])
arr9[0] #access the element based on index number
arr9[2]
arr9[0 : 4]
arr9[ : : 2] # skips one element after one
arr9[ : 4]
arr9[0 : ]
arr9[-1] #access the element which is in the last of the list
arr9[-3]
arr9[-1 : -4 : -1] #slices the last elements by substracing -1 element from the list to reach the element

print("\n multi dimentional araray slicing \n")

mat1 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

print("\n most of the indexing and slicing concepts are same as normal one ")

print(mat1[0 : 2 , 0 : 3]) #rows and columns also starts from 0th index syntax:(row start : row end , col start : col end)
print(mat1[0 :  , 0 : ]) #starts from first row and col and ends at last row and col
print(mat1[ : ,  : ]) #Wdefaultly prints from the first row to the last row and forst col to last col
print(mat1[1 : 3 , 1 :3]) # access middle elements of the matrix