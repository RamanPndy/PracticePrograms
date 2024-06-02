from ecdsa import SigningKey, SECP256k1

'''
Wallet Management:
Wallet Class: Manages Bitcoin addresses and private keys.
Address Generation: Generates new Bitcoin addresses using ECDSA.
'''
class Wallet:
    def __init__(self):
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()
        self.address = self.public_key.to_string().hex()

    def get_address(self):
        return self.address

    def sign_transaction(self, transaction):
        return self.private_key.sign(transaction.encode())

class WalletManager:
    def __init__(self):
        self.wallets = []

    def create_wallet(self):
        wallet = Wallet()
        self.wallets.append(wallet)
        return wallet

'''
Transaction Creation and Validation:
Transaction Class: Represents a Bitcoin transaction with inputs, outputs, and signatures.
Transaction Validation: Validates transactions for correctness and sufficiency of funds.
'''
class TransactionInput:
    def __init__(self, transaction_id, output_index, signature=None):
        self.transaction_id = transaction_id
        self.output_index = output_index
        self.signature = signature

class TransactionOutput:
    def __init__(self, address, amount):
        self.address = address
        self.amount = amount

class Transaction:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def to_string(self):
        return f"Inputs: {self.inputs}, Outputs: {self.outputs}"

class TransactionValidator:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def validate_transaction(self, transaction):
        # Check if inputs are valid and unspent
        for tx_input in transaction.inputs:
            if not self.blockchain.is_unspent(tx_input.transaction_id, tx_input.output_index):
                return False
        return True

'''
Blockchain Interaction:
Block and Blockchain Classes: Represents blocks and the blockchain, managing transaction inclusion and validation.
'''
import hashlib
class Block:
    def __init__(self, previous_hash):
        self.previous_hash = previous_hash
        self.transactions = []
        self.nonce = 0

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def compute_hash(self):
        block_string = f"{self.previous_hash}{self.transactions}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.unspent_transactions = []

    def add_block(self, block):
        self.chain.append(block)
        self.update_unspent_transactions(block)

    def is_unspent(self, transaction_id, output_index):
        for tx in self.unspent_transactions:
            if tx['transaction_id'] == transaction_id and tx['output_index'] == output_index:
                return True
        return False

    def update_unspent_transactions(self, block):
        for transaction in block.transactions:
            for output_index, output in enumerate(transaction.outputs):
                self.unspent_transactions.append({
                    'transaction_id': transaction.to_string(),
                    'output_index': output_index,
                    'output': output
                })

'''
Network Communication:
Network Node Class: Manages communication between nodes, broadcasting transactions, and receiving blocks.
'''
import socket
class NetworkNode:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = []

    def connect_to_peer(self, peer_host, peer_port):
        peer = (peer_host, peer_port)
        self.peers.append(peer)

    def broadcast_transaction(self, transaction):
        for peer in self.peers:
            self.send_message(peer, transaction.to_string())

    def send_message(self, peer, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(peer)
            s.sendall(message.encode())

    def receive_block(self, block):
        # Process received block and add to blockchain
        pass

# Create Wallet
wallet_manager = WalletManager()
wallet = wallet_manager.create_wallet()
print("New Address:", wallet.get_address())

# Create Transaction
tx_input = TransactionInput("some_tx_id", 0)
tx_output = TransactionOutput(wallet.get_address(), 10)
transaction = Transaction([tx_input], [tx_output])
signature = wallet.sign_transaction(transaction.to_string())
tx_input.signature = signature

# Validate and Add Transaction to Blockchain
blockchain = Blockchain()
validator = TransactionValidator(blockchain)
if validator.validate_transaction(transaction):
    block = Block("previous_hash_placeholder")
    block.add_transaction(transaction)
    blockchain.add_block(block)

# Network Communication (broadcast transaction to peers)
node = NetworkNode('localhost', 8333)
node.connect_to_peer('peer_host', 8333)
node.broadcast_transaction(transaction)
