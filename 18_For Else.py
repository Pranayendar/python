# FOR ELSE in Python
# we even can use for else like we used for if
nums = [12,23,25,10,11]
for num in nums:
     if num%5==0:
         print(num)
         break #helps to print only 1st number which is divisible by 5



nums = [12,23,22,10,14]
for num in nums:
     if num%5==0:
         print(num)
         break #it helps to return only the number divisible by 5 and the code block stops executing here
else:
    print("not found") #Else is not written to the if part but written to the for
    # else is written to if then it returns output for every iteration in the list
