#student pass or fail? pass if total 40% and at least 33% each. Assume 3 subjects and take marks as an input from the user
sub1 = int(input("Enter first subject marsk \n"))
sub2 = int(input("Enter second subject marsk \n"))
sub3 = int(input("Enter third subject marsk \n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail!")
elif(sub1+sub2+sub3)/3 <40:
    print("you are fail due to total percentage less than 40")
else:
    print("you passed!")