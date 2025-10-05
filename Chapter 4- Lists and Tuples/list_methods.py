#list methods
l1=[1,6,7,8,3,4,5,67,8,0]
l1_sorted = l1.sort()
print(l1_sorted) #sorts l1 itself
print(l1) #sorted list
l1.reverse ()
print(l1)


#append -> adds at the end of the list
l1.append(85)
print(l1)

l1.insert(2, 545) #inserts 545 on index 2
print(l1)

l1.pop(2) #removes element from the index 2
l1.remove(5) #remove 545 from the list
