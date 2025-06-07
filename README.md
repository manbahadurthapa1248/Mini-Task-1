# Blockchain Simulation Mini Task 1

This repository contains three Python scripts simulating fundamental blockchain concepts, designed for educational purposes:

---

## 1. `blockchain_simulator.py`

**Objective:** Build a simple blockchain with 3 linked blocks.

- Implements a `Block` class with index, timestamp, data, previous hash, hash, and nonce.
- Calculates SHA-256 hashes and links blocks by chaining their previous hashes.
- Demonstrates blockchain immutability by tampering with block data and showing validation failure.
- Validates the entire chain’s integrity.

**How to run:**

python blockchain_simulator.py


---


## 2. `mining_simulation.py`

**Objective:** Simulate Proof-of-Work (PoW) mining by finding a nonce that produces a hash meeting a difficulty target.

- Defines a `Block` class with mining functionality using a `mine_block(difficulty)` method.
- Mines the block by incrementally adjusting the nonce until the hash starts with a required number of zeros (difficulty).
- Prints mining progress details including nonce attempts and time taken.
- Helps illustrate the computational effort behind PoW consensus.

**How to run:**

python mining_simulation.py


---


## 3. `consensus_demo.py`

**Objective:** Simulate and compare three blockchain consensus mechanisms: Proof-of-Work (PoW), Proof-of-Stake (PoS), and Delegated Proof-of-Stake (DPoS).

- Creates mock validators with random attributes for each consensus type.
- PoW selects the validator with the highest computational power.
- PoS selects the validator with the highest stake.
- DPoS selects a delegate based on majority votes from voters.
- Prints detailed logs explaining the selection process and consensus logic.

**How to run:**

python consensus_demo.py
