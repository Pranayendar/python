#BREAK vs CONTINUE vs PASS
difference between them

#CONTINUE:- skips only particular iteration
for i in range(1,6):
    if i==3:
        continue
    print(i)

#OUTPUT
# 1
# 2
# 4
# 5

#BREAK:- comes out the loop itself without printing the next values
for i in range(1,6):
    if i==3:
        break
    print(i)

OUTPUT
# 1
# 2

# PASS:- to skip the particular block

i=5
if i==4:
    print("i is in range")
else:
    pass  #since if block code is not printed then it returned to else block and skipped and printed the below code


print("i is not in range")

#OUTPUT
# 5
# i is not in range
