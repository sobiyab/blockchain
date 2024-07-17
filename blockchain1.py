import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}".encode()
        return hashlib.sha256(value).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def add_block(self, data):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = time.time()
        new_block = Block(index, previous_block.hash, timestamp, data)
        self.chain.append(new_block)

# Usage
my_blockchain = Blockchain()
my_blockchain.add_block("First Block Data")
my_blockchain.add_block("Second Block Data")

# Display the blockchain
for block in my_blockchain.chain:
    print(f"Index: {block.index}, Hash: {block.hash}, Data: {block.data}, Timestamp: {block.timestamp}")
