#LOOPS
#WHILE LOOP
while loop works with the conditions provided
#it helps to print a same output for a number of times
x=6 #input
while x<=10: #if the x is less than equal to 10
    print("while loop") #this output is returned
    x=x+1 #then increments x with +1 and returns to the x

#Nested While loop
x=2
y=2
while x<=5:#this loop will execute
    print("while loop", end=" ") #end helps to print the next output in the same line
    while y<=4: #enters this loop and retunrs to outer loop after the completion
        print("nested", end=" ")
        y=y+1
    x=x+1 #this will increment the x
    print() #helps to print the next while loop in the new line

##OUTPUT
# while loop nested nested nested
# while loop
# while loop
# while loop

#
x=2
while x<=5:#this loop will execute
    print("while loop", end=" ") #end helps to print the next output in the same line
    y=2 #declaring the y here helps to print the nested after every while loop
    while y<=4: #enters this loop and retunrs to outer loop after the completion
        print("nested", end=" ")
        y=y+1
    x=x+1 #this will increment the x
    print() #helps to print the next while loop in the new line

##OUTPUT
# while loop nested nested nested
# while loop nested nested nested
# while loop nested nested nested
# while loop nested nested nested
