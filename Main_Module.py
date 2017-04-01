from GUI import GUI_Impl
from Comm_Module import Communication_Module
from NFC_Module import NFC_Module
from Tkinter import *
import time
from threading import Thread
from Config_File_Reader import configFileReader
import signal
import sys
from threading import Timer

## This module is the driver script of the application

##_geom='200x200+0+0'

INVALID_CARD_DELAY = 0
TRANSACTION_COMPLETE_DELAY = 0
PIN_TIMEOUT_DELAY = 0

apdu = []
ATR = []

stationConfigs = ()

##
#Global Modules
##

nfcMod = None
commMod = None
rfidGui = None

_root = None

    
## This function gets the configurations and set them as global variables, and
## initialize the communication and NFC modules    
def readConfigs():

        global INVALID_CARD_DELAY
        global TRANSACTION_COMPLETE_DELAY
        global PIN_TIMEOUT_DELAY
        
        global apdu
        global ATR
        
        global stationConfigs

        global commMod
        global nfcMod
        
        confReader = configFileReader()

        configs = confReader.readConfigFile()
        
        INVALID_CARD_DELAY = configs['INVALID_CARD_DELAY']
        TRANSACTION_COMPLETE_DELAY = configs['TRANSACTION_COMPLETE_DELAY']
        PIN_TIMEOUT_DELAY = configs['PIN_TIMEOUT_DELAY']
        apdu = configs['apdu']
        ATR = configs['ATR']
        stationConfigs = configs['stationConfigs']

        commMod = Communication_Module(configs['HEADER'],configs['services'])
        nfcMod = NFC_Module()

## The callback function for pin entry timeout
def pin_timeout():        
    global pin_timeout_passed
    rfidGui.pin_timeout_passed = True
    print ('pin timeout')


## This function holds the main functionality of the system
def main_func():

    root = _root

    while root != None:
            
        super(rfidGui.__class__,rfidGui).show_card_waiting_screen(root)

        UID = nfcMod.readUID(ATR,apdu)

        if UID == None:
                super(rfidGui.__class__,rfidGui).show_swipe_retry_screen(root)
                time.sleep(2)
                continue
        
        authorizationResponse = commMod.authorizeStation(stationConfigs[0], stationConfigs[1])
        if authorizationResponse == None:
                super(rfidGui.__class__,rfidGui).show_communication_error_screen(root)
                time.sleep(TRANSACTION_COMPLETE_DELAY)
                continue
        elif authorizationResponse[0] == False:
                super(rfidGui.__class__,rfidGui).show_station_auth_error_screen(root)
                time.sleep(TRANSACTION_COMPLETE_DELAY)
                continue
        
        access_token = authorizationResponse[1]
        
        UID_response = commMod.verifyUID(access_token, UID)
        if access_token == None:
                super(rfidGui.__class__,rfidGui).show_communication_Error_screen(root)
                time.sleep(TRANSACTION_COMPLETE_DELAY)
                continue
        
        if UID_response[0] == True:

            card_token = UID_response[1]
            
            super(rfidGui.__class__,rfidGui).show_keypad_screen(root)

            PIN_response = 4  
            while PIN_response == 4:
                rfidGui.PIN = ""
                
                pinTimer = Timer(PIN_TIMEOUT_DELAY, pin_timeout) ## Creating PIN timeout timer
                pinTimer.start() ## Start the PIN timeout timer
                
                while rfidGui.ok_button_pressed == False and rfidGui.cancel_button_pressed == False and rfidGui.pin_timeout_passed == False:
                    time.sleep(0.1)
                    pass
                
                if rfidGui.pin_timeout_passed == True:
                    rfidGui.pin_timeout_passed = False
                    break

                
                elif rfidGui.ok_button_pressed == True:

                    pinTimer.cancel() ## Canel the PIN timeout timer                       
                    
                    rfidGui.ok_button_pressed = False
                    PIN_response = commMod.verifyPIN(access_token, card_token, rfidGui.PIN)

                    if PIN_response == None:
                        super(rfidGui.__class__,rfidGui).show_communication_Error_screen(root)
                        time.sleep(TRANSACTION_COMPLETE_DELAY)
                        break

                    if PIN_response == 0:
                        super(rfidGui.__class__,rfidGui).show_access_granted_screen(root)
##                      self.commMod.sendConfirmation(access_token)
                        time.sleep(TRANSACTION_COMPLETE_DELAY)
                    elif PIN_response == 3:
                        super(rfidGui.__class__,rfidGui).show_access_denied_screen(root)
                        time.sleep(TRANSACTION_COMPLETE_DELAY)
                    else:
                        super(rfidGui.__class__,rfidGui).show_pin_retry_screen(root)
                    
                else:
                    pinTimer.cancel() ## Canel the PIN timeout timer 
                    rfidGui.cancel_button_pressed = False
                    break

            
            
        else:
                super(rfidGui.__class__,rfidGui).show_invalid_card_screen(root)
                time.sleep(INVALID_CARD_DELAY)


def _quit(event):
    sys.exit()

## This function starts the main functionality as an asynchronous thread to the main GUI thread
def runMain():
    Thread(target = main_func).start()


def main():

    global rfidGui
    global _root

    readConfigs()
    
    try: userinit()
    except NameError: pass
    root = Tk()
    _root = root
    rfidGui = GUI_Impl(root)
    #root.title('RFID')
    
##    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight())) ## Make the window full-screen
    
##    root.overrideredirect(True) ## Remove window borders
    
##    root.bind('<Control-Q>', sys.exit)
##    root.bind('<Escape>', sys.exit)
    
    root.after(100, runMain)
    try: run()
    except NameError: pass
    root.protocol('WM_DELETE_WINDOW', root.quit)
    root.mainloop()
    
    
    
    
            
        

if __name__ == '__main__': main()
