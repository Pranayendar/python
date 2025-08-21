# Finding Prime Numbers

num = int(input("Enter a number: "))
for i in range(2,num):
    if num % i == 0:
        print("its not prime")
        break
else:
    print("its prime")
