from smartcard.System import readers
import smartcard.util
from smartcard.CardRequest import CardRequest
from smartcard.CardType import ATRCardType
from smartcard.CardType import AnyCardType
from smartcard.Exceptions import CardConnectionException
from smartcard.util import toBytes 

## This module is responsible for reading the UID from RFID cards
class NFC_Module():

    def readUID(self,ATR,apdu):

        cardtype = ATRCardType(toBytes(ATR))
        cardrequest = CardRequest(timeout=None, cardType=cardtype)
        cardservice = cardrequest.waitforcard()

        try:
            cardservice.connection.connect()
            response, sw1, sw2 = cardservice.connection.transmit(apdu)
        except CardConnectionException:
            return None   
##        print toHexString(cardservice.connection.getATR())
        
        
        print "%x %x" % (sw1, sw2)
        print "%x, %x, %x, %x" % (response[0],response[1],response[2],response[3])

        if sw1 == 0x90 and sw2 == 0x00: #check if UID was read successfully
            UID = str(hex(response[0]))+str(hex(response[1]))+str(hex(response[2]))+str(hex(response[3]))
            return UID.replace("0x","")

        return None
