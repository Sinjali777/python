greeting= "Good Morning"
name="sugam"
print(type(name))
#print(greeting + name)
# concatinating two strings
c=greeting + name
print(c)
print("using array")
print(name[2])
# name[2]="d" --> doesn't work
print(name[0:4]) # string slicing
print(name[1:3])
print(name[:4]) #same as name[0:4]
print("negative indexing")
print(name[-1]) #gives the last character in the string 
print(name[-4:-1])

print("slicing with skip value")
print(name[1:4:1]) #prints every 1st character
print(name[1:4:2]) #prints every 2nd character
print(name[0::2]) #prints every 2nd character, skips 1 character



