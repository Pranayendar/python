#Taking the values of array from the user
from array import *
from operator import index

arr = array('i',[])#creating the empty array using []
#taking the size of the array
n=int(input("enter the length of the array: "))
#taking the values of the array
for i in range(n):
    x = int(input("enter the next value: "))
    arr.append(x) #this helps to add the values to the array

print(arr)

##finding the index number of a value in the array
val = int(input("enter the value to search: "))

# a is the element comes from the array
k=0
for a in arr:
     if a==val:
         print(k)
         break
     k+=1

#finding the index directly by function
print(arr.index(val))