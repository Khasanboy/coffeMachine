import Tkinter
import os # needed for relative image paths


## This module holds the GUI description of the applications
class GUI(object):
    _images = [] # Holds image refs to prevent GC
    
    
    def __init__(self, root):

        self._root = root
        # Widget Initialization
        self.pinEntryMsg = Tkinter.Label(root,
            font = "{MS Sans Serif} 12 bold",
            text = "Please Enter Your PIN",
        )
        self.oneButton = Tkinter.Button(root,
            height = 2,
            text = 1,
            width = 5,
        )
        self.twoButton = Tkinter.Button(root,
            height = 2,
            text = 2,
            width = 5,
        )
        self.threeButton = Tkinter.Button(root,
            height = 2,
            text = 3,
            width = 5,
        )
        self.fourButton = Tkinter.Button(root,
            height = 2,
            text = 4,
            width = 5,
        )
        self.fiveButton = Tkinter.Button(root,
            height = 2,
            text = 5,
            width = 5,
        )
        self.sixButton = Tkinter.Button(root,
            height = 2,
            text = 6,
            width = 5,
        )
        self.sevenButton = Tkinter.Button(root,
            height = 2,
            text = 7,
            width = 5,
        )
        self.eightButton = Tkinter.Button(root,
            height = 2,
            text = 8,
            width = 5,
        )
        self.nineButton = Tkinter.Button(root,
            height = 2,
            text = 9,
            width = 5,
        )
        self.zeroButton = Tkinter.Button(root,
            height = 2,
            text = 0,
            width = 5,
        )
        self.okButton = Tkinter.Button(root,
            height = 2,
            text = "OK",
            width = 5,
            disabledforeground = "#808080",
            state = "disabled"                                       
        )
        self.eraseButton = Tkinter.Button(root,
            height = 2,
            text = "<-",
            width = 5,
        )
        self.cancelButton = Tkinter.Button(root,
            text = "Cancel",
        )
        self.textArea = Tkinter.Label(root,
            activebackground = "#ffffff",
            background = "#ffffff",
            text = ""                                      
        )

        # widget commands

        self.oneButton.configure(
            command = self.oneButton_command
        )
        self.twoButton.configure(
            command = self.twoButton_command
        )
        self.threeButton.configure(
            command = self.threeButton_command
        )
        self.fourButton.configure(
            command = self.fourButton_command
        )
        self.fiveButton.configure(
            command = self.fiveButton_command
        )
        self.sixButton.configure(
            command = self.sixButton_command
        )
        self.sevenButton.configure(
            command = self.sevenButton_command
        )
        self.eightButton.configure(
            command = self.eightButton_command
        )
        self.nineButton.configure(
            command = self.nineButton_command
        )
        self.zeroButton.configure(
            command = self.zeroButton_command
        )
        self.okButton.configure(
            command = self.okButton_command
        )
        self.eraseButton.configure(
            command = self.eraseButton_command
        )
        self.cancelButton.configure(
            command = self.cancelButton_command
        )

        self.show_card_waiting_screen(root)

        # Resize Behavior
        root.grid_rowconfigure(1, weight = 1, minsize = 40, pad = 0)
        root.grid_rowconfigure(2, weight = 1, minsize = 40, pad = 0)
        root.grid_rowconfigure(3, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(4, weight = 1, minsize = 40, pad = 0)
        root.grid_rowconfigure(5, weight = 1, minsize = 40, pad = 0)
        root.grid_rowconfigure(6, weight = 1, minsize = 40, pad = 0)
        root.grid_rowconfigure(7, weight = 1, minsize = 40, pad = 0)
        root.grid_rowconfigure(8, weight = 1, minsize = 40, pad = 0)
        root.grid_rowconfigure(9, weight = 1, minsize = 40, pad = 0)
        root.grid_columnconfigure(1, weight = 1, minsize = 40, pad = 0)
        root.grid_columnconfigure(2, weight = 1, minsize = 40, pad = 0)
        root.grid_columnconfigure(3, weight = 1, minsize = 40, pad = 0)
        root.grid_columnconfigure(4, weight = 1, minsize = 40, pad = 0)
        root.grid_columnconfigure(5, weight = 1, minsize = 40, pad = 0)

        

    ## Prepare the screen for displaying a message
    def prepareToDisplayMsg(self,root):
        self.pinEntryMsg.grid(
            in_    = root,
            column = 1,
            row    = 2,
            columnspan = 5,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 9,
            sticky = "nsew"
        )

        self.oneButton.grid_forget()
        self.twoButton.grid_forget()
        self.threeButton.grid_forget()
        self.fourButton.grid_forget()
        self.fiveButton.grid_forget()
        self.sixButton.grid_forget()
        self.sevenButton.grid_forget()
        self.eightButton.grid_forget()
        self.nineButton.grid_forget()
        self.zeroButton.grid_forget()
        self.okButton.grid_forget()
        self.eraseButton.grid_forget()
        self.cancelButton.grid_forget()
        self.textArea.grid_forget()


    ## Prepare the screen for displaying a PIN entry GUI
    def prepareToDisplayKeypad(self,root):

        # Geometry Management
        self.pinEntryMsg.grid(
            in_    = root,
            column = 1,
            row    = 2,
            columnspan = 5,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.oneButton.grid(
            in_    = root,
            column = 2,
            row    = 4,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.twoButton.grid(
            in_    = root,
            column = 3,
            row    = 4,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.threeButton.grid(
            in_    = root,
            column = 4,
            row    = 4,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.fourButton.grid(
            in_    = root,
            column = 2,
            row    = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.fiveButton.grid(
            in_    = root,
            column = 3,
            row    = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.sixButton.grid(
            in_    = root,
            column = 4,
            row    = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.sevenButton.grid(
            in_    = root,
            column = 2,
            row    = 6,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.eightButton.grid(
            in_    = root,
            column = 3,
            row    = 6,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.nineButton.grid(
            in_    = root,
            column = 4,
            row    = 6,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.zeroButton.grid(
            in_    = root,
            column = 3,
            row    = 7,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.okButton.grid(
            in_    = root,
            column = 4,
            row    = 8,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.eraseButton.grid(
            in_    = root,
            column = 3,
            row    = 8,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.cancelButton.grid(
            in_    = root,
            column = 2,
            row    = 8,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.textArea.grid(
            in_    = root,
            column = 2,
            row    = 3,
            columnspan = 3,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )

    def show_card_waiting_screen(self, root):

        self.pinEntryMsg.configure(text = "Please Present Your Card", fg='black')
        self.prepareToDisplayMsg(root)
        

    def show_invalid_card_screen(self, root):

        self.pinEntryMsg.configure(text = "Card Presented is Invalid", fg='red')
        self.prepareToDisplayMsg(root)

    def show_access_granted_screen(self, root):

        self.pinEntryMsg.configure(text = "Access Granted", fg='green')
        self.prepareToDisplayMsg(root)

    def show_access_denied_screen(self, root):

        self.pinEntryMsg.configure(text = "Access Denied", fg='red')
        self.prepareToDisplayMsg(root)

    def show_communication_error_screen(self, root):

        self.pinEntryMsg.configure(text = "Communication Error", fg='red')
        self.prepareToDisplayMsg(root)

    def show_station_auth_error_screen(self, root):

        self.pinEntryMsg.configure(text = "Station Authorization Error", fg='red')
        self.prepareToDisplayMsg(root)

    def show_swipe_retry_screen(self, root):

        self.pinEntryMsg.configure(text = "Error Reading Card, Try Again", fg='red')
        self.prepareToDisplayMsg(root)        

    def show_keypad_screen(self, root):

        self.pinEntryMsg.configure(text = "Please Enter Your PIN",fg='black')
        self.textArea.configure(text = "")
        self.okButton.configure(state = "disabled")
        self.prepareToDisplayKeypad(root)
        

    def show_pin_retry_screen(self, root):

        self.pinEntryMsg.configure(text = "PIN incorrect, Try again",fg='black')
        self.textArea.configure(text = "")
        self.okButton.configure(state = "disabled")
        self.prepareToDisplayKeypad(root)
                

    
    def changeTextAreaText(self,txt):
        self.textArea.configure(text = txt)
        pass

    def disableOkButton(self):
        self.okButton.configure(state = "disabled")

    def enableOkButton(self):
        self.okButton.configure(state = "normal")


        
