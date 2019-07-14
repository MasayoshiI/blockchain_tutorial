# import libraries
import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5



class Client:
    def __init__(self):
        #set up random to safely generate a strong secret key
        random = Crypto.Random.new().read
        # using RSA Algo to create both private and public key
        # Private key should not be lost for record tracking and public key is used as an user's identity
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()

    @property
    def identity(self):
        """ The identity is unique to each client and can be made publicly available. 
        Anybody would be able to send virtual currency to you using this identity and it will get added to your wallet. """
        # DER is a binary format for data structures described
        # decoded in ascii format
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')


masa = Client()
print(masa.identity)