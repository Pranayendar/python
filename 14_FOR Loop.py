# FOR LOOP
# for loop generally works with the sequence
#increments by itself automatically unlike in While loop
x={'pranay',22,10.2} #not only with set it also works on all the sequence related data types
print(x)
for i in x:
    print(i)


y="pranay"
print(y)
for i in y:
    print(i)#prints out every character in the string


# can also be define like below
for i in [1,3,"pranay"]:
    print(i)


for i in range(10):
    print(i)#prints numbers from 0 to 9


for i in range(10,22,2):#(start point, end point, increment/decrement)
    print(i)#prints numbers from 10 to 22 with increment of 2


for i in range(20,11,-1): #by default it goes in accennding order so used -1
    print(i)#prints numbers from 20 to 11 with decrement of 1


for i in range(1,21):
    if(i%5!=0):#if inside a FOR loop
        print(i)#ptints the numbers which are not divisible by 5 from 1 to 20