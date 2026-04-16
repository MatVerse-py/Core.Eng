# Real Sepolia Anchor Script (PoEP)
import os
from web3 import Web3

RPC = os.getenv("SEPOLIA_RPC")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
MERKLE_ROOT = os.getenv("MERKLE_ROOT")

if not RPC or not PRIVATE_KEY or not MERKLE_ROOT:
    raise RuntimeError("Missing environment variables")

w3 = Web3(Web3.HTTPProvider(RPC))
account = w3.eth.account.from_key(PRIVATE_KEY)

nonce = w3.eth.get_transaction_count(account.address)

tx = {
    "to": account.address,
    "value": 0,
    "gas": 100000,
    "gasPrice": w3.to_wei("20", "gwei"),
    "nonce": nonce,
    "data": w3.to_hex(text=MERKLE_ROOT)
}

signed_tx = account.sign_transaction(tx)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

print("TX_HASH:", tx_hash.hex())
