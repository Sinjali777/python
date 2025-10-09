#An empty set can be created using the below syntax:
b= set()
print(type(b))


#Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5)  #Adding a value repeatedly doesn't changes a set
b.add(6)
#b.add([4,5,6])    #cannot add list inside set
b.add((4,5,6))     #can add tuple
#b.add({4:5} )     #cannot add disctionary because it is not hashable

#something that can be changed in the future cannot be add/included in the set
print(b)

#Length of set
print(len(b)) #prints the length of the set

#Removal of an item
b.remove(4) # removes 4 from the ser
# b.remove(15) #throws an error while trying to remove 15(which is not present in the set)
print(b)

print(b.pop()) #remove an arbitrary elemnt from the set and returns the element removed

# b.clear() #empties the set

#s.union()-> returns union elements
#s.intersection() -> returns elements that falls under intersection 

print(b.union({5,10,11}))
print(b.intersection({5,10,11}))

