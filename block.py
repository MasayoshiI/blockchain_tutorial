
from transaction import Transaction
from client import Client

class Block:
    """
    Block Class
        verified_transactions to indicate that only the verified valid transactions will be added to the block. 
        Each block also holds the hash value of the previous block, so that the chain of blocks becomes immutable.
        Nonce for storing the nonce created by the miner during the mining process.
        a nonce is an arbitrary number that can be used just once in a cryptographic communication.
        nonce prevents replay attack
    """
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.nonce = ""

last_block_hash = ""


def test():
    # make two clients for the transaction
    Masa = Client()
    Kenny = Client()

    # this is the transaction info
    t0 = Transaction (
       Kenny.identity,
       Masa.identity,
       500.0
    )

    # create a block

    block0 = Block()

    # there is no previous block and nonce so set hash to None because first transaction
    block0.previous_block_hash = None
    block0.nonce = None

    # verify now
    block0.verified_transactions.append(t0)

    # get hash of the block we just made for the next block set it to last block hash
    digest = hash(block0)
    last_block_hash = digest

test()

