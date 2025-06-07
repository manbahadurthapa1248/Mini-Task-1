import random

# ---------- Proof of Work (PoW) Simulation ----------
# Validators have computational power; highest power wins
pow_validators = {
    'MinerA': {'power': random.randint(1, 100)},
    'MinerB': {'power': random.randint(1, 100)},
    'MinerC': {'power': random.randint(1, 100)}
}

# Select the miner with the highest computational power
selected_pow = max(pow_validators.items(), key=lambda x: x[1]['power'])

print("\n🔨 Proof of Work (PoW):")
print(f"Miner Powers: {pow_validators}")
print(f"Selected: {selected_pow[0]} with Power {selected_pow[1]['power']}")
print("✔️ PoW selects the miner with the highest computational power.\n")

# ---------- Proof of Stake (PoS) Simulation ----------
# Validators have stakes; highest stake wins
pos_validators = {
    'StakerA': {'stake': random.randint(1, 100)},
    'StakerB': {'stake': random.randint(1, 100)},
    'StakerC': {'stake': random.randint(1, 100)}
}

# Select the validator with the highest stake
selected_pos = max(pos_validators.items(), key=lambda x: x[1]['stake'])

print("💰 Proof of Stake (PoS):")
print(f"Staker Stakes: {pos_validators}")
print(f"Selected: {selected_pos[0]} with Stake {selected_pos[1]['stake']}")
print("✔️ PoS selects the validator with the highest amount of stake.\n")

# ---------- Delegated Proof of Stake (DPoS) Simulation ----------
# Voters cast votes for delegates; delegate with most votes wins
dpos_candidates = ['DelegateA', 'DelegateB', 'DelegateC']
votes = {
    'Voter1': random.choice(dpos_candidates),
    'Voter2': random.choice(dpos_candidates),
    'Voter3': random.choice(dpos_candidates)
}

# Count votes for each delegate
vote_counts = {candidate: list(votes.values()).count(candidate) for candidate in dpos_candidates}
selected_dpos = max(vote_counts.items(), key=lambda x: x[1])

print("🗳️ Delegated Proof of Stake (DPoS):")
print(f"Votes: {votes}")
print(f"Vote Counts: {vote_counts}")
print(f"Selected Delegate: {selected_dpos[0]} with {selected_dpos[1]} vote(s)")
print("✔️ DPoS chooses a delegate based on majority voting.")