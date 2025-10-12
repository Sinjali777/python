#multiplication table of any number from the user
num=int(input("Enter any number"))
i=1
for i in range(1,11): #11 used because it goes as i-1
    
    print("Normal Way  ")
    print(str(num)+"X" + str(i) +"=" + str(i*num))

    print("Using F string") #fstring makes it easy to use strings, we just have to use {} brackets
    print(f"{num}X{i}={num*i}")
    
    
