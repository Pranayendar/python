#If Elif Else Statement
x=int(input("enter a number: ")) #taking input from the user as integer
a=x%2#checking whether the input is divisible by 2
if a==0: #if the the reminder is 0 it returns true
    print("even")


x=int(input("enter a number: ")) #taking input from the user as integer
a=x%2#checking whether the input is divisible by 2
if a==0: #if the the reminder is 0 it returns true
    print("even")
else: #it returns odd if the reminder is 1
    print("odd")

#nested if and else
x=int(input("enter a number: "))
y=x%2
if y==0:
    print("even")#prints if the number is even
    if x>5: #if the above condition meets then it comes to this line of code
        print("greater than 5")#if the number is greater than 5 this will be printed
    else:
        print("lesser than 5")#iif less than 5 this will print
else:
    print("odd")#if the number is odd this will print
    if x>5:
        print("greater than 5")
    elif x==5:
        print("equals to 5")
    else:
        print("lesser than 5")
        # checks all the above conditions and returns according to the number