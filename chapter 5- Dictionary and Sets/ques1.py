#create a dictionary of Nepali words with values as their english translation. Provide user with an option to look it up.

myDict = {
    "dabba" : "box",
    "kalo": "black",
    "bhakundo": "football",
}
print("Options are: ", myDict.keys())
a=input("Enter the nepali word: \n ")
# print("The meaning of your word is: ",myDict[a])   ----> throws an error is the key is not present in the dictionary
print("The meaning of your word is: ",myDict.get(a))
