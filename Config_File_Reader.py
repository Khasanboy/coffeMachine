import ConfigParser

## This module is responsible for reading the application configurations from
## the config files
class configFileReader():

    ## This function reads the configurations from "rfid_config.ini"
    ## and returns a dictionary of the configurations
    def readConfigFile(self):

        configFile = "rfid_config.ini"

        Config = ConfigParser.ConfigParser()
        Config.read(configFile)


        ##Delays

        INVALID_CARD_DELAY = Config.getint("TimeDelays",'Invalid_Card_Delay')
        TRANSACTION_COMPLETE_DELAY = Config.getint("TimeDelays",'Transaction_Complete_Delay')
        PIN_TIMEOUT_DELAY = Config.getint("TimeDelays",'PIN_Timeout_Delay')
        

        ##Communication

        comm_metadata = Config.items("Communication")
        HEADER = comm_metadata[0][1]
        services = [comm_metadata[1][1],comm_metadata[2][1],comm_metadata[3][1]]


        ##NFC

        ATR = Config.get("NFC", 'ATR')
        apdu = [Config.getint("NFC",'CLASS'),Config.getint("NFC",'INS'),Config.getint("NFC",'P1'),Config.getint("NFC",'P2'),Config.getint("NFC",'Le')]


        ##Station
        
        stationConfigs = (Config.get("Station", 'Station_Id'),Config.get("Station", 'Station_Secret'))


        return {'INVALID_CARD_DELAY':INVALID_CARD_DELAY,'TRANSACTION_COMPLETE_DELAY':TRANSACTION_COMPLETE_DELAY,'PIN_TIMEOUT_DELAY':PIN_TIMEOUT_DELAY,'HEADER':HEADER,'services':services,'ATR':ATR,'apdu':apdu,'stationConfigs':stationConfigs} 
