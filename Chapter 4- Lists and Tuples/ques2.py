#accept marks of 6 students and display them in sorted manner
m1 = int(input( "Enter the marks of student1:" )) #using int to typecast it and make it integer
m2 = int(input( "Enter the marks of student2:" )) 
m3 = int(input( "Enter the marks of student3:" ))
m4 = int(input( "Enter the marks of student4:" ))
m5 = int(input( "Enter the marks of student5: "))
m6 = int(input( "Enter the marks of student6: "))
 
marks= [m1, m2, m3 , m4 , m5 , m6]
marks.sort()
print(marks)