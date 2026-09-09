import tkinter as tk
from tkinter import messagebox


def incrementCount(bread):
    global b1, b2, b3

    if bread == 'b1':
        b1 += 1
    elif bread == 'b2':
        b2 += 1
    elif bread == 'b3':
        b3 += 1


def resultMessage():
    finalCount = max(b1, b2, b3)
    if finalCount == b1:
        breadType = "bagel"
    elif finalCount == b2:
        breadType = "garlic bread"
    elif finalCount == b3:
        breadType = "white bread"

    messagebox.showinfo("Favorite bread", f"Your bread type is {breadType}")


def addAndHide(bread, nextFunction):
    global currentButtons
    incrementCount(bread)
    hideButtons(currentButtons)
    nextFunction()


def countAndShowMessage(bread):
    global currentButtons
    hideButtons(currentButtons)
    incrementCount(bread)
    resultMessage()


def buttons2():
    global currentButtons
    currentButtons = [
        createButton("Space", lambda: addAndHide('b1', buttons3)),
        createButton("Desert", lambda: addAndHide('b2', buttons3)),
        createButton("Ocean", lambda: addAndHide('b3', buttons3))
    ]


def buttons3():
    global currentButtons
    currentButtons = [
        createButton("Skiing", lambda: addAndHide('b1', buttons4)),
        createButton("Snowboarding", lambda: addAndHide('b2', buttons4)),
        createButton("Neither", lambda: addAndHide('b3', buttons4))
    ]


def buttons4():
    global currentButtons
    currentButtons = [
        createButton("Hotdog", lambda: addAndHide('b1', buttons5)),
        createButton("Pizza", lambda: addAndHide('b2', buttons5)),
        createButton("Apple", lambda: addAndHide('b3', buttons5))
    ]


def buttons5():
    global currentButtons
    currentButtons = [
        createButton("Morning", lambda: addAndHide('b1', buttons6)),
        createButton("Afternoon", lambda: addAndHide('b2', buttons6)),
        createButton("Night", lambda: addAndHide('b3', buttons6))
    ]


def buttons6():
    global currentButtons
    currentButtons = [
        createButton("Easter", lambda: addAndHide('b1', buttons7)),
        createButton("Halloween", lambda: addAndHide('b2', buttons7)),
        createButton("Thanksgiving", lambda: addAndHide('b3', buttons7))
    ]


def buttons7():
    global currentButtons
    currentButtons = [
        createButton("Rain", lambda: addAndHide('b1', buttons8)),
        createButton("Sun", lambda: addAndHide('b2', buttons8)),
        createButton("Snow", lambda: addAndHide('b3', buttons8))
    ]


def buttons8():
    global currentButtons
    currentButtons = [
        createButton("Sourdough", lambda: countAndShowMessage('b1')),
        createButton("Ciabatta", lambda: countAndShowMessage('b2')),
        createButton("Pumpernickel", lambda: countAndShowMessage('b3'))
    ]


def createButton(text, command):
    button = tk.Button(root, text=text, command=command)
    button.pack()
    return button


def hideButtons(buttons):
    for button in buttons:
        button.pack_forget()


b1 = 0
b2 = 0
b3 = 0

root = tk.Tk()

root.title("What bread are you?")

buttonLabel = tk.Label(root, text="What is your favorite?")
buttonLabel.pack()

currentButtons = []

currentButtons.extend([
    createButton("Dog", lambda: addAndHide('b1', buttons2)),
    createButton("Cat", lambda: addAndHide('b2', buttons2)),
    createButton("Monkey", lambda: addAndHide('b3', buttons2))
])

root.mainloop()






