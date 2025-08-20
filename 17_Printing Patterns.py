#Printing Patterns using Python

for i in range(5): #i represents the rows
    for j in range(4-i): #j represents the columns
        print("* ",end="")
    print()
#
# OUTPUT
# * * * *
# * * *
# * *
# *


for i in range(5): #i represents the rows
    for j in range(i+1): #j represents the columns
        print("* ",end="")
    print()
#
# OUTPUT
# *
# * *
# * * *
# * * * *
# * * * * *

#IGNORE THIS BLOCK OF SHITTY CODE BUT CAN SEE FOR UNDERSTANDING
for  j in range(4):
    print("# ",end="")#end="" helps to print the output in the same line
print() #it helps to come the next into new line

for  j in range(3):
    print("# ",end="")
print()

for  j in range(2):
    print("# ",end="")
print()

for  j in range(1):
    print("# ",end="")
print()