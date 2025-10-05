#type a letter template
letter = ''' Dear <|NAME|>,

You are selected !

Date: <|DATE|>'''

name = input("Enter Your name \n")
date = input("Enter Date \n") 
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
