import json
import requests
import sys
import random
from Security_Module import Security_Module

## This module is responsible for communicating with the server using HTTP posts
class Communication_Module:

    secMod = Security_Module() ## This object will be used for hashing

    HEADER = ""
    STATION_AUTH_CMD = ""
    VERIFY_UID_CMD = ""
    VERIFY_PIN_CMD = ""
    CARD_LIST_CMD = ""
    CARD_BY_UID = ""

    ## The constructor will set the header and web service commands according
    ## to the values extracted from the config file
    def __init__(self,header,services):
        self.STATION_AUTH_CMD = services[0]
        self.VERIFY_UID_CMD = services[1]
        self.VERIFY_PIN_CMD =services[2]
        self.CARD_LIST_CMD = services[3]
        self.CARD_BY_UID = services[4]
        self.HEADER = header


    ## This function takes the web service url and the parameters then returns 
    ## The resonse in JSON format s
    def post(self,url,params):

        rnd = random.randint(0,sys.maxint)

        params = {'data':params, 'rand':str(rnd), 'code':'0'}

        try:
            response = requests.post(url, data=json.dumps(params), verify='certificates/ca.crt')
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            print '\nconnection error'
            return None

        return response.json()                  
        
    def get(self,url,params):
        url = url + params
        try:
            print '\nGET:Request' + url
            response = requests.get(url)
            print '\nGETResponse' + url
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            print ('connection error')
            return None
        return response.json()

    def getCardByUID(self,uid):
        url = self.HEADER + self.CARD_BY_UID
        params = '/'+uid

        jsonResponse = self.get(url,params)
        if jsonResponse == None:
            print('Card with UID not found')
            return None
        print(jsonResponse)
        return (True,jsonResponse)

    ## This function used to authorize the station
    def authorizeStation(self, station_id, station_secrect):
        url = self.HEADER + self.STATION_AUTH_CMD
        params = {'station_id': station_id, 'station_secret': station_secrect}

        jsonResponse = self.post(url,params)

        if jsonResponse == None:
            print ('Authorization error')
            return None
        
        
        if jsonResponse['code'] == 0:
            return (True, jsonResponse['data']['access_token'])
        return (False, None)


    ## This function is used to verify the UID        
    def verifyUID(self, access_token, UID):
        url = self.HEADER + self.VERIFY_UID_CMD

        ## The UID is hashed before being sent over the network
        hashedUID = self.secMod.hashMessage(UID)

        params = {'access_token': access_token, 'uid': hashedUID}

        jsonResponse = self.post(url,params)

        if jsonResponse == None:
            print('connection error')
            return None
        
        if jsonResponse['code'] == 0:
            return (True,jsonResponse['data']['card_token'])
        return (False,None)
        

    ## This function is used to verify the PIN
    def verifyPIN(self, access_token, card_token, PIN):
        url = self.HEADER + self.VERIFY_PIN_CMD

        print (PIN)

        ## The PIN is hashed, then hash code is concatenated with the card_token
        ## then the whole string is hashed again
        hashedPin = self.secMod.hashMessage(self.secMod.hashMessage(PIN)+card_token)

        params = {'access_token': access_token, 'card_token': card_token, 'pin': hashedPin}

        jsonResponse = self.post(url,params)

        if jsonResponse == None:
            print('verify pin error')
            return None

        
        return jsonResponse['code']

