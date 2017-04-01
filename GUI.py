from Tkinter import *
from GUI_ui import GUI


PIN_LEN = 6

## This module holds the functional commands of the PIN entry GUI
class GUI_Impl(GUI):
    
    PIN = ""

    ok_button_pressed = False
    cancel_button_pressed = False
    pin_timeout_passed = False

    # BEGIN CALLBACK CODE

    # cancelButton_command --
    #
    # Callback to handle cancelButton widget option -command
    def cancelButton_command(self, *args):
        self.cancel_button_pressed = True
        pass

    # eightButton_command --
    #
    # Callback to handle eightButton widget option -command
    def eightButton_command(self, *args):
        self.addNum('8')
        pass

    # eraseButton_command --
    #
    # Callback to handle eraseButton widget option -command
    def eraseButton_command(self, *args):
        self.eraseNum()
        pass

    # fiveButton_command --
    #
    # Callback to handle fiveButton widget option -command
    def fiveButton_command(self, *args):
        self.addNum('5')
        pass

    # fourButton_command --
    #
    # Callback to handle fourButton widget option -command
    def fourButton_command(self, *args):
        self.addNum('4')
        pass

    # nineButton_command --
    #
    # Callback to handle nineButton widget option -command
    def nineButton_command(self, *args):
        self.addNum('9')
        pass

    # okButton_command --
    #
    # Callback to handle okButton widget option -command
    def okButton_command(self, *args):
        self.ok_button_pressed = True
        pass

    # oneButton_command --
    #
    # Callback to handle oneButton widget option -command
    def oneButton_command(self, *args):
        self.addNum('1')
        pass

    # sevenButton_command --
    #
    # Callback to handle sevenButton widget option -command
    def sevenButton_command(self, *args):
        self.addNum('7')
        pass

    # sixButton_command --
    #
    # Callback to handle sixButton widget option -command
    def sixButton_command(self, *args):
        self.addNum('6')
        pass

    # threeButton_command --
    #
    # Callback to handle threeButton widget option -command
    def threeButton_command(self, *args):
        self.addNum('3')
        pass

    # twoButton_command --
    #
    # Callback to handle twoButton widget option -command
    def twoButton_command(self, *args):
        self.addNum('2')
        pass

    # zeroButton_command --
    #
    # Callback to handle zeroButton widget option -command
    def zeroButton_command(self, *args):
        self.addNum('0')
        pass

    # textArea_xscrollcommand --
    #
    # Legacy command found in callback code. Add user comments inside body.
    def textArea_xscrollcommand(self, *args):
        pass

    # textArea_yscrollcommand --
    #
    # Legacy command found in callback code. Add user comments inside body.
    def textArea_yscrollcommand(self, *args):
        pass

    def addNum(self, num):
        if len(self.PIN) < PIN_LEN:
            self.PIN = self.PIN + num
            GUI.changeTextAreaText(self,'*'*len(self.PIN))
            if len(self.PIN) == PIN_LEN:
                GUI.enableOkButton(self)    
            
        print (self.PIN)
        print (len(self.PIN))

    def eraseNum(self):
        if len(self.PIN) > 0:
            self.PIN = self.PIN[:(len(self.PIN)-1)]
            GUI.changeTextAreaText(self,'*'*len(self.PIN))
            GUI.disableOkButton(self)
            
        

    # END CALLBACK CODE


