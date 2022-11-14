
# Python program to  create a simple GUI
# calculator using tkinter
# Author: Brady Chen, created on April 16, 2019
# Updated by:
# GUI Calculator Program
# This program implements the arithmetic operations.
#
from tkinter import *


class Calculator:
    # define the text on each button
    # ButtonValues[0][0] = '7', ButtonValues[1][0] = '4'
    ButtonValues = [['7', '8', '9', '/'],
                    ['4', '5', '6', '*'],
                    ['1', '2', '3', '-'],
                    ['0', 'C', '=', '+'],
                    ['.', '(', ')', '%']]

    # Constructor
    def __init__(self):
        self.Calc = Tk()
        self.Calc.title('Calculator')

        # Create two frames: frame1 is to house the display acreen
        #                    frame2 is to house all the buttons
        self.frame1 = Frame(self.Calc)
        self.frame2 = Frame(self.Calc)

        #
        self.expression = ""
        self.equation = StringVar()

        # Create an Entry display and bind the entry to a StringVar instance
        # equation:
        #   You can call set() to set a value in the entry or call get() to
        #   get a value from the entry
        self.theDisplay = Entry(self.frame1, width=30,
                                textvariable=self.equation)
        self.myButtons = []

    # Define all the buttons
    def SetButtons(self):
        self.frame1.pack()
        self.frame2.pack(side=BOTTOM)

        self.theDisplay.grid(row=0)

        self.myButtons.append([])
        self.myButtons[0].append(
            Button(self.frame2, text=Calculator.ButtonValues[0][0], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[0][0])))

        self.myButtons[0].append(
            Button(self.frame2, text=Calculator.ButtonValues[0][1], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[0][1])))

        self.myButtons[0].append(
            Button(self.frame2, text=Calculator.ButtonValues[0][2], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[0][2])))

        self.myButtons[0].append(
            Button(self.frame2, text=Calculator.ButtonValues[0][3], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[0][3])))

        self.myButtons.append([])

        self.myButtons[1].append(
            Button(self.frame2, text=Calculator.ButtonValues[1][0], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[1][0])))

        self.myButtons[1].append(
            Button(self.frame2, text=Calculator.ButtonValues[1][1], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[1][1])))

        self.myButtons[1].append(
            Button(self.frame2, text=Calculator.ButtonValues[1][2], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[1][2])))

        self.myButtons[1].append(
            Button(self.frame2, text=Calculator.ButtonValues[1][3], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[1][3])))
        self.myButtons.append([])
        self.myButtons[2].append(
            Button(self.frame2, text=Calculator.ButtonValues[2][0], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[2][0])))

        self.myButtons[2].append(
            Button(self.frame2, text=Calculator.ButtonValues[2][1], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[2][1])))

        self.myButtons[2].append(
            Button(self.frame2, text=Calculator.ButtonValues[2][2], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[2][2])))

        self.myButtons[2].append(
            Button(self.frame2, text=Calculator.ButtonValues[2][3], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[2][3])))

        self.myButtons.append([])

        self.myButtons[3].append(
            Button(self.frame2, text=Calculator.ButtonValues[3][0], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[3][0])))
        self.myButtons[3].append(
            Button(self.frame2, text=Calculator.ButtonValues[3][1], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[3][1])))
        self.myButtons[3].append(
            Button(self.frame2, text=Calculator.ButtonValues[3][2], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[3][2])))
        self.myButtons[3].append(
            Button(self.frame2, text=Calculator.ButtonValues[3][3], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[3][3])))

        self.myButtons.append([])

        self.myButtons[4].append(
            Button(self.frame2, text=Calculator.ButtonValues[4][0], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[4][0])))
        self.myButtons[4].append(
            Button(self.frame2, text=Calculator.ButtonValues[4][1], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[4][1])))
        self.myButtons[4].append(
            Button(self.frame2, text=Calculator.ButtonValues[4][2], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[4][2])))
        self.myButtons[4].append(
            Button(self.frame2, text=Calculator.ButtonValues[4][3], font=8,
                   width=4,
                   command=lambda: self.Press(Calculator.ButtonValues[4][3])))

        # position the buttons in self.frame2
        for i in range(5):
            for j in range(4):
                self.myButtons[i][j].grid(row=i, column=j, sticky="nsew")

    # This method is triggered by pressing a button. It will do the following
    #   (1) update expression if the button is not "=" or "C"
    #   (2) if the button "=" is pressed, call eval() to evaluate the
    #       expression and display the result by calling set() in StringVar
    #       instance equation
    #   (3) if the button "C" is pressed, set expression to "" and set display
    #       to ""
    #
    def Press(self, num):
        # If the button "=" is pressed, then the expression will be
        # evaluated
        if num == '=':
            total = str(eval(self.expression))  # '10'
            self.equation.set(total)
            # Fixing the bug by applying the expression  to be equal to the
            # total value from the equality
            self.expression = total
        elif num == 'C':
            self.expression = ""
            self.equation.set("")
        else:
            # point out the global expression variable
            # global self.expression
            # concatenation of string
            self.expression = self.expression + num  # '' + '3' = '3'
            # update the expression by using set method
            self.equation.set(self.expression)

        # main program


if __name__ == '__main__':
    myCalc = Calculator()
    myCalc.SetButtons()
    myCalc.Calc.mainloop()
