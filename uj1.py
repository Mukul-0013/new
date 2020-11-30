import string
import random
from tkinter import *
from tkinter import Tk
import os

def listToString(arr):
    str = ""
    for element in arr:
        str += element
    return str

def click():
    password = generatePassword()
    output.delete(0.0, END)
    try:
        randPass = listToString(password)
    except:
        randPass = "There is somethong wrong :("
    output.insert(END, randPass)

def clear():
    output.delete(0.0, END)

def generatePassword():
    upperCase = string.ascii_uppercase
    lowerCase = string.ascii_lowercase
    digits = string.digits
    specialChar = string.punctuation

    password = []
    elements = []
    elements.extend(list(upperCase))
    elements.extend(list(lowerCase))
    elements.extend(list(digits))
    elements.extend(list(specialChar))

    for element in range(int(random.randrange(12, 32, 1))):
        password.append(random.choice(elements))

    length = len(password)

    # Make first char small letter
    password[0] = random.choice(list(lowerCase))
    # Mkae last char capital letter
    password[length - 1] = random.choice(list(upperCase))

    # Removed spaces
    for i in password:
        if i == " ":
            password.remove(password[i])
        else:
            continue
    return password

def copyToClipboard():
    c = Tk()
    c.withdraw()
    c.clipboard_clear()
    c.clipboard_append()
    c.update()
    c.destroy()

if __name__ == "__main__":

    win = Tk()
    win.title("Password Generator")

    Label (win, text="Click generate to get a new random password :",
                bg="white",
                fg="black",
                font="ariel 20 bold").grid(row=0, column=0, sticky=N)

    Button(win, text="Generate",
                width=8,
                command=click) .grid(row=3, column=0, sticky=E)

    output = Text(win, width=40, height=1, wrap=WORD, background="white")
    output.grid(row=5, column=0, columnspan=2, sticky=W)

    Button(win, text="CLEAR",
                width=5,
                command=clear) .grid(row=11, column=0, sticky=E)

    Button(win, text="Copy to clipboard",
                width=17,
                command=copyToClipboard).grid(row=10, column=0, sticky=E)

    win.mainloop()
