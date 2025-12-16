#factorial
num=int(input("Enter a number"))
f=1
n=num
while num !=0:
    f=f*num
    num=num-1

print("factorial of " + str(n) +  " is ", f)