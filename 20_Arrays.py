# Array in Python
# Array is collection of elements of same data types
# same as list but doesn't allow elements of different data types
# they don't have specific size it's flexible to modify for different sizes

# * means wants to work with all the functions in the array
from array import *

values = array('i',[5,9,8,4,2])#type code need to be specified and cannot convert to another once declared
'i' refers to the signed values
print(values)

print(values.buffer_info())#buffer info will give both the address and size of the array
print(values.typecode)#returns the type of the code
values.reverse() #to reverse the values in array
print(values)
#append to add values
values.append(3)
print(values)
#remove to delete values
values.remove(5)
print(values)

# since array is similar to list we can consider indexing
print(values[0]) #print the value at the index of 0
print(values[2:4])

#print the values from 0 to 3 index values one by one
for i in range(4): #if we know the length of the array
    print(values[i])


for i in range(len(values)): #if we don't know the length of the array
    print(values[i]) #len function is used to specify the length of the values array

#Goes with the every value in the array
for e in values:
    print(e)


# get the data type and elements from the values array
newvals = array(values.typecode, (a for a in values))
print(newvals)

# get the data type and square of the elements from the values array
newvals = array(values.typecode, (a*a for a in values))
print(newvals)


# We can even print the elements one by one using while loop
i=0 #starting with the 0 index element
while i<len(values):
    print(values[i])
    i+=1