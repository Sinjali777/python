#replace double spaces with single space
story = "once upon a time there was a youtuber named harry who  uploaded  python course  with notes upon"
doublespace = story.find("  ")
print(doublespace) #but only the 1st double space
story= story.replace("  ", " ")
print(story)