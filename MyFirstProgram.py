#This is my first program in Python
#I like to think of it as a simple dialog...

print ("Hello. What's your name?")
print () #I am leaving this space blank, as to form a paragraph
theirName = input() #Whatever name they enter, it will be stored as a string called "theirName" (variable)
print ()
print ("Hi," + theirName + ". Nice to meet you")
print ()
print (theirName + ", I will tell you how many letters there are in your name:")
len(theirName) #"lenght" function
print (str(len(theirName)) + " letters are needed to form your name... :D ") #Passing "lenght", which is an int as a string
print ()
print ("How old are you, " + theirName + "?")
theirAge = input ()
print ()
print("OK, " + theirName + ". Now, I will tell you how old you will be on the next year.")
print ("The next year, you will be " + str((int(theirAge)) + 1) + " years old, " + theirName) #Passing an int number (theirAge) as a string


print ("----Version 2----")

print ("Hello. What's your name?")
theirName = input()
len (theirName)
print ()
print ("Hi," + theirName + ". Nice to meet you. I will tell you how many letters there are in your name:" + str(len(theirName)) + " letters are needed to form your name... :D ")
print ()
print ("How old are you, " + theirName + "?")
theirAge = input ()
print ()
print ("OK, " + theirName + ". Now, I will tell you how old you will be on the next year. In 2018, you will be " + (str 1 + str(int(theirAge))) + " years old.") # Makes program crash



