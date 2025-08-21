
##Numpy package
##which helps to use multi dimensional arrays
##since in python it doesn't support directly using multi dimensional arrays
##cmd to install in IDLE :-  pip3 install numpy
# #
from numpy import *
arr = array([1,2,3,4,5],'i')#defining the datatype is optional in numpy package
print(arr)


# 6 ways to create arrays
# 1> array()
# 2> linspace()
# 3> logspace()
# 4> arange()
# 5> zeros()
# 6> ones()

#check the datatype of the array
from numpy import *
arr =array([1,2,3,4,5])
print(arr.dtype)#returns the data type of the array
#if change one value to float then the interpreter converts all the values into float and returns float

arr = linspace(0,5,10)#takes 3 parameters (start, stop,no.of parts)
print(arr)# if we dont specify the parts will 50 default

arr=arange(1,10,3)
print(arr)

arr = logspace(1,10,4)#in linspace the difference will be fixed but here it depends on log
print(arr)
print(log(arr))

arr = zeros(5)
print(arr)

arr=ones(5)
print(arr)