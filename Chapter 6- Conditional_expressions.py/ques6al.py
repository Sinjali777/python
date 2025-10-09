#convert marks into grade
marks=int(input("Enter tha marks: "))
print("Your grade is:")
if(marks>=90):
    print("EX")
elif(marks>=80 ):
    print("A")
elif(marks>=70 ):
    print("B")
elif(marks>=60 ):
    print("C")
elif(marks>=50 ):
    print("D")
else:
    print("F")
