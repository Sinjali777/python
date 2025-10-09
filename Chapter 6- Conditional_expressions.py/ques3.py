#write a program to detect spams
a="make a lot of money"
b="buy now"
c="suscribe this"
d="click this"
text=input("Enter the text:")
spam=False
if(a in text):
    spam=True
elif(b in text):
    spam=True
if(c in text):
    spam=True
elif(d in text):
    spam=True

if(spam):
    print("This text is spam")
else:
    print("This is not a spam")
    