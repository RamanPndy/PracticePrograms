import hashlib
import ecdsa
import json
import time

'''
Components
Wallet: Manages user's private and public keys, creates and signs transactions.
Transaction: Represents a transfer of Bitcoin from one address to another.
Block: Contains a list of transactions and metadata.
Blockchain: A chain of blocks, each containing a set of transactions.
Node: Participates in the network, validates transactions, and propagates them to other nodes.
Network: Connects multiple nodes, enabling them to communicate and share the blockchain state.
'''

'''
Step 1: Define the Wallet
'''
class Wallet:
    def __init__(self):
        self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def get_address(self):
        pk_bytes = self.public_key.to_string()
        return hashlib.sha256(pk_bytes).hexdigest()

    def sign_transaction(self, transaction):
        tx_json = json.dumps(transaction, sort_keys=True).encode()
        return self.private_key.sign(tx_json)

    def verify_signature(self, transaction, signature, public_key):
        tx_json = json.dumps(transaction, sort_keys=True).encode()
        try:
            public_key.verify(signature, tx_json)
            return True
        except ecdsa.BadSignatureError:
            return False

'''
Step 2: Define the Transaction
'''
class Transaction:
    def __init__(self, sender_address, recipient_address, amount, signature=None):
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.amount = amount
        self.timestamp = time.time()
        self.signature = signature

    def to_dict(self):
        return {
            'sender_address': self.sender_address,
            'recipient_address': self.recipient_address,
            'amount': self.amount,
            'timestamp': self.timestamp,
            'signature': self.signature
        }

    def sign_transaction(self, wallet):
        self.signature = wallet.sign_transaction(self.to_dict())

'''
Step 3: Define the Block
'''
class Block:
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_data).hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

'''
Step 4: Define the Blockchain
'''
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = []
        self.mining_reward = 50

    def create_genesis_block(self):
        return Block("0", [])

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        block = Block(self.get_latest_block().hash, self.pending_transactions)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        self.pending_transactions = [Transaction(None, miner_address, self.mining_reward)]

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for tx in block.transactions:
                if tx.sender_address == address:
                    balance -= tx.amount
                if tx.recipient_address == address:
                    balance += tx.amount
        return balance

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Create wallets
wallet1 = Wallet()
wallet2 = Wallet()

# Initialize blockchain
blockchain = Blockchain()

# Create transactions
tx1 = Transaction(wallet1.get_address(), wallet2.get_address(), 10)
tx1.sign_transaction(wallet1)

# Add transactions to the blockchain
blockchain.create_transaction(tx1)

# Mine pending transactions
blockchain.mine_pending_transactions(wallet1.get_address())

# Check balances
print(f"Wallet1 Balance: {blockchain.get_balance(wallet1.get_address())}")
print(f"Wallet2 Balance: {blockchain.get_balance(wallet2.get_address())}")

# Validate blockchain
print(f"Blockchain valid? {blockchain.is_chain_valid()}")
