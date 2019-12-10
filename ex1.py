import os.path
from os import path

#If file exists, open it. Otherwise make a new file.
if path.exists("SaveFile.txt"):
    saveFile = open("SaveFile.txt", 'r')
    print(saveFile.read())
elif path.exists("SaveFile.txt") == False:
    saveFile = open("SaveFile.txt", 'w')
    #Getting What To Write To File
    text = input('What Do You Want To Write To Your File? ')
    saveFile.write(text)
    saveFile.close()


#Handling user input and using it to call functions or format strings.
defaultResponse = "I didnt understand that"
functionBool = False

#Example of a function response retuning the string.
def nameResponse(a):
    global functionBool
    print('The inputted string is:', a)
    functionBool = True


#Dictionary of possible user inputs
switcher = {
    "hi":              lambda a : "Hello there!",
    "general kenobi":  lambda a : "You, {0}, are a bold one".format(a),
    "foolish":         nameResponse
}

#User input function
while True:
    a = input("> ").lower()

    #References the library and either calls a function or returns a string
    b = switcher.get(a, lambda a : defaultResponse)(a)

    #Handles string vs function
    if(functionBool == False):
        print(b)

    functionBool = False
