#User Input
x=input("Enter a number: ")
y=input("Enter another number: ")
z=x+y
print(z)
#returns the numbers as strings
#by default the input function takes as the string


x=input("Enter a number: ")
a=int(x) #converting the string into int
y=input("Enter another number: ")
b=int(y) #converting the string into int
z=a+b
print(z)

##like wise converting the string into the int in the same line
x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
z=x+y
print(z)

#taking input as character
ch = input("Enter a character: ")
print(ch)
#since it doesn't allow only single character

#we limit the number of characters to single using index (0)
ch = input("Enter a character: ")[0]#index value to print only the 1st char
print(ch)

# Evaluate the expression you provide as an user input
result = eval(input())
print(result)


# taking input from the user from the command line
import sys
#argv argument values
#index values is given during declaring variable
#converting the value into integer during the assigning
x=int(sys.argv[1])
y=int(sys.argv[2])
z=x+y
print(z)