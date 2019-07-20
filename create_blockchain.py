from transaction import Transaction
from client import Client
from block import Block



def dump_blockchain (self):
   print ("Number of blocks in the chain: " + str(len(self)))

def test_blockchain():
    TPCoins = []
    for x in range (len(TPCoins)):
        block_temp = TPCoins[x] 
        print ("block # " + str(x))

    for transaction in block_temp.verified_transactions:
        Transaction.display_transaction (transaction)

