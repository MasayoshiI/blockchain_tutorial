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
        return collections.OrderedDict ({
        'sender': self.sender.identity,
        'recipient': self.recipient,
        'value': self.value,
        'time' : self.time
        })
    
    def sign_transaction(self):
        """sign a dictionary object using the private key of the sender. Use the built-in PKI with SHA algorithm. 
        The generated signature is decoded to get the ASCII representation for printing and storing it in our blockchain. """

        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')
    
def display_transaction(transaction):
    #for transaction in transactions:
    t_dict = transaction.to_dict()
    print ("sender: " + t_dict['sender'])
    print ('-----')
    print ("recipient: " + t_dict['recipient'])
    print ('-----')
    print ("value: " + str(t_dict['value']))
    print ('-----')
    print ("time: " + str(t_dict['time']))
    print ('-----')


def test():
    # create a transaction queue
    transaction_queue = []
    # add clients
    masa = client.Client()
    gonta = client.Client()
    dimi = client.Client()
    kenny = client.Client()
    # start adding transactions on the queue
    t1 = Transaction(masa, gonta.identity, 5.0)
    t1.sign_transaction()
    transaction_queue.append(t1)

    t2 = Transaction(dimi, masa.identity, 6.0)
    t2.sign_transaction()
    transaction_queue.append(t2)

    t3 = Transaction(kenny, gonta.identity, 2.0)
    t3.sign_transaction()
    transaction_queue.append(t3)

    t4 = Transaction(gonta, kenny.identity, 4.0)
    t4.sign_transaction()
    transaction_queue.append(t4)

    t5 = Transaction(masa, kenny.identity, 7.0)
    t5.sign_transaction()
    transaction_queue.append(t5)

    t6 = Transaction(gonta, dimi.identity, 3.0)
    t6.sign_transaction()
    transaction_queue.append(t6)

    t7 = Transaction(masa, dimi.identity, 8.0)
    t7.sign_transaction()
    transaction_queue.append(t7)

    t8 = Transaction(gonta, masa.identity, 1.0)
    t8.sign_transaction()
    transaction_queue.append(t8)

    t9 = Transaction(kenny, masa.identity,5.0)
    t9.sign_transaction()
    transaction_queue.append(t9)

    t10 = Transaction(dimi, masa.identity, 3.0)
    t10.sign_transaction()
    transaction_queue.append(t10)
    

    for transaction in transaction_queue:
        display_transaction(transaction)
        print ('--------------')

     
