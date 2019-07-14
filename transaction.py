import client
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

class Transaction:
    """Transaction Class: send money from a sender to a recipient """
    def __init__(self, sender, recipient, value):
        """construct from sender's public key, recipient's public key, value and time"""
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        """make it into a dictionary"""
        return collections.OrderedDict({
        'sender': self.sender.identity,
        'recipient': self.recipient.identity,
        'value': self.value,
        'time' : self.time})
    
    def sign_transaction(self):
        """sign a dictionary object using the private key of the sender. Use the built-in PKI with SHA algorithm. 
        The generated signature is decoded to get the ASCII representation for printing and storing it in our blockchain. """

        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')



def test():
    masa = client.Client()
    gonta = client.Client()

    t = Transaction(masa, gonta, 5.0)

    signature = t.sign_transaction()
    print (signature) 

test()