This is a for fun personality quiz that simply using a variety of preference questions to score you as a certain type of bread. 
There are 8 questions with 3 answers each, leading to being scored as a certain type of bread depending on your answers

# Features

A simple GUI made with Tkinter
8 questions
Score tracking
Dynamic question progression through the GUI

# Functions

incrementCount

Increases the score for the bread type associated with the selected answer.

resultMessage

Compares the three bread scores and displays the bread type with the highest score.

addAndHide

Records the selected answer, hides the current buttons, and moves the quiz to the next question.

countAndShowMessage

Records the final answer, hides the current buttons, and displays the quiz result.

buttons2 - buttons8

Create the answer buttons for each question and assign the appropriate scoring and progression functions to each button.

createButton

Creates a Tkinter button with the given text and command, adds it to the window, and returns the button.

hideButtons

Hides the current set of answer buttons from the window.



One note is that there is no handling for a tie in points so the resulting winner will be the first, so bagel, garlic bread, white bread in that order. 
