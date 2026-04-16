# External Full Verifier (PoEP)
import json, hashlib, os
from web3 import Web3

RPC = os.getenv("SEPOLIA_RPC")
ARTIFACT_FILE = "poep/artifact.json"
LEDGER_FILE = "poep/ledger.json"

w3 = Web3(Web3.HTTPProvider(RPC))

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

def verify_chain(ledger):
    prev = "genesis"
    for b in ledger:
        raw = json.dumps(b["data"], sort_keys=True)
        h = sha256(raw)
        if h != b["hash"]:
            return False
        if b["prev_hash"] != prev:
            return False
        prev = b["hash"]
    return True

def merkle_root(blocks):
    hashes = [sha256(json.dumps(b, sort_keys=True)) for b in blocks]
    while len(hashes) > 1:
        if len(hashes) % 2 == 1:
            hashes.append(hashes[-1])
        hashes = [sha256(hashes[i] + hashes[i+1]) for i in range(0, len(hashes), 2)]
    return hashes[0]

def verify_anchor(tx_hash, expected_root):
    tx = w3.eth.get_transaction(tx_hash)
    data_hex = tx["input"][2:]
    data = bytes.fromhex(data_hex).decode()
    return data == expected_root

if __name__ == "__main__":
    with open(ARTIFACT_FILE) as f:
        artifact = json.load(f)
    with open(LEDGER_FILE) as f:
        ledger = json.load(f)

    chain_ok = verify_chain(ledger)
    root = merkle_root(ledger)
    merkle_ok = root == artifact["merkle_root"]
    anchor_ok = verify_anchor(artifact["tx_hash"], artifact["merkle_root"])

    print("CHAIN:", chain_ok)
    print("MERKLE:", merkle_ok)
    print("ANCHOR:", anchor_ok)
    print("PROOF VALID:", chain_ok and merkle_ok and anchor_ok)
