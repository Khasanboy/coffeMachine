import hashlib

## This module contains the hashing function to be used within the application
## The hashing function here uses SHA-512 hashing algorithm 
class Security_Module:

    def hashMessage(self,msg):
        return hashlib.sha512(msg).hexdigest();
        
        
