##Swaping of 2 varibales

x=3
y=4

#using 3 rd variable
amp=x
x=y
y=amp
print(x)
print(y)

#using formula
x = x+y
y=x-y
x=x-y
print(x)
print(y)

#using XOR so that it wont waste extra bit
x=x^y
y=x^y
x=x^y
print(x)
print(y)

#using
x,y = y,x
print(x)
print(y)