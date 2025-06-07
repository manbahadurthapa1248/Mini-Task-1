import hashlib
import datetime
import time

# Block class representing a single block in the chain
class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # Number used to vary the hash during mining
        self.hash = self.calculate_hash()

    # Calculate the SHA-256 hash of the block’s contents including nonce
    def calculate_hash(self):
        raw_data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(raw_data.encode()).hexdigest()

    # Proof-of-Work mining: find a hash with a prefix of '0' repeated difficulty times
    def mine_block(self, difficulty):
        print(f"\n⛏️ Mining Block {self.index} with difficulty {'0' * difficulty}...")
        start_time = time.time()  # Start timer to measure mining duration
        target = '0' * difficulty  # Target prefix of zeros for valid hash

        attempts = 0  # Count nonce attempts
        while not self.hash.startswith(target):
            self.nonce += 1  # Increment nonce to change hash
            self.hash = self.calculate_hash()  # Recalculate hash
            attempts += 1

        end_time = time.time()  # End timer after successful mining

        # Print summary of mining results
        print(f"✅ Block {self.index} mined!")
        print(f"⏱️ Time taken: {end_time - start_time:.4f} seconds")
        print(f"🔁 Nonce attempts: {attempts}")
        print(f"📦 Final Hash: {self.hash}")

if __name__ == "__main__":
    difficulty = 4  # Set difficulty level (number of leading zeros required)

    # Create a block with current timestamp and sample data
    block = Block(1, str(datetime.datetime.now()), "Proof of Work Simulation")
    
    # Start mining process
    block.mine_block(difficulty)