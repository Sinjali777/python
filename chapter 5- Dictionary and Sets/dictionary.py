myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Coder",
    "marks": [1,3,4,],
    "anotherdict": {'harry': 'player'}, #nested dictionary
    1: 2
}
print(myDict['fast'])
myDict['marks']= [2,4,5] #changeable
print(myDict['marks'])

print(myDict['anotherdict']['harry']) # nested dictionary 

#Dictionary Methods
print(type(myDict.keys())) #prints the type of  the dictionary
print(list(myDict.keys())) #prints the keys of the dictionary
print(myDict.values()) #prints the (key,values) of all the contents in the dictionary
updateDict = {
    "Lovish": "Friend",
    "Sugam" : "Nitisha",
    "harry" : "dancer" #updates the exisiting content
}
myDict.update(updateDict) #updates the dictionary by adding key value pairs from updayeDict
print(myDict)
print(myDict.get("harry"))
print(myDict["harry"]) 

#the diffference between .get and [] sytax
print(myDict.get("harry2"))#returns none as harry2 is not present in the dictionary/ runs a search in the dictionary
print(myDict["harry2"]) #throws an error as harry2 is not present in the dictionary
