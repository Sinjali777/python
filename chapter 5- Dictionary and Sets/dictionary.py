myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1,3,4,],
    "anotherdict": {'harry': 'player'} #nested dictionary

}
print(myDict['Fast'])
myDict['Marks']= [2,4,5] #changeable
print(myDict['Marks'])

print(myDict['anotherdict']['harry']) # nested dictionary 
