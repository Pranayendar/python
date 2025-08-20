##BREAK, CONTINUE and PASS Keywords

#BREAK:- to come out the block of code
x=int(input("how many drinks do you want: "))

i=1 #increment value
available_drinks = 6 #limiting the x
while i<=x: #if the i<=x enters while loop
    if i>available_drinks: #if the i > x then it enters the if statement
        print("No stock left!")
        break #break is used to come out of the block
    print("Drink!")
    i+=1 #incrementing i with 1 every time until x < available_stock



#Continue:- used to skip a particular value and continue the loop
#using FOR loop
for i in range(1,20): #defining the range of i
    if i%3==0 and i%5==0: #i divisible by 3 and 5
        continue #skips the values divisible by 3and 5
    print(i)

#using WHILE loop
i=1 #defining i
while i<20: #enters the loop if i is less than 20
    if i%3==0 and i%5==0: #i divisible by 3 and 5
        i+=1 #increment i or else it goes under infinite loop when i reaches 15
        continue #it skips the value 15 and continue with the loop from 16
    print(i) #prints the number
    i+=1#increment the i value for checking next value of i


#PASS:- ignore the particular block of code and continue with the next code
#using FOR loop
for i in range(1,22):
    if i%2==0:
        print(i)
    else:
        pass #ignores the block if nothing to print there

#using WHILE loop

i=int(input())
while i<21:
    if i%2==0:
        print(i)
    else:
        pass #ignores the block if nothing to print there
    i+=1