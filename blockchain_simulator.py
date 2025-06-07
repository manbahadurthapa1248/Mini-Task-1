import hashlib
import datetime

# Block class representing each block in the chain
class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # Number used once, changed during mining to find valid hash
        self.hash = self.calculate_hash()

    # Calculate SHA-256 hash based on block content and nonce
    def calculate_hash(self):
        to_hash = (str(self.index) + str(self.timestamp) +
                   str(self.data) + self.previous_hash + str(self.nonce))
        return hashlib.sha256(to_hash.encode()).hexdigest()

    # Simulate Proof-of-Work by mining until hash starts with required prefix (difficulty)
    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block {self.index} mined with nonce {self.nonce}: {self.hash}")

# Blockchain class manages the chain of blocks
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2  # Difficulty level for mining (number of leading zeros)

    # Create the first block in the chain
    def create_genesis_block(self):
        return Block(0, str(datetime.datetime.now()), "Genesis Block", "0")

    # Return the most recent block on the chain
    def get_latest_block(self):
        return self.chain[-1]

    # Add a new block to the chain after mining it
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        print(f"\nMining block {new_block.index}...")
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    # Verify the integrity of the blockchain by checking hashes and links
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            # Check if current block's hash is valid
            if curr.hash != curr.calculate_hash():
                print(f"Block {curr.index} has invalid hash.")
                return False

            # Check if current block correctly links to previous block
            if curr.previous_hash != prev.hash:
                print(f"Block {curr.index} previous hash does not match Block {prev.index}'s hash.")
                return False
        return True

    # Display all blocks and their details
    def print_chain(self):
        for block in self.chain:
            print(f"\nBlock {block.index}:")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Nonce: {block.nonce}")

# ------------ Testing the Blockchain ------------

my_chain = Blockchain()

# Add two blocks with data to the chain, mining them
my_chain.add_block(Block(1, str(datetime.datetime.now()), "Block 1 Data"))
my_chain.add_block(Block(2, str(datetime.datetime.now()), "Block 2 Data"))

print("\nOriginal Blockchain:")
my_chain.print_chain()
print(f"\nIs blockchain valid? {my_chain.is_chain_valid()}")

# Tamper with block 1's data and update its hash (simulating malicious change)
print("\nTampering with Block 1's data...\n")
my_chain.chain[1].data = "Tampered Data"
my_chain.chain[1].hash = my_chain.chain[1].calculate_hash()

print("After Tampering:")
my_chain.print_chain()
print(f"\nIs blockchain valid? {my_chain.is_chain_valid()}")

print("\nNote: Tampering with a block's data invalidates all subsequent blocks unless their hashes are recomputed.")