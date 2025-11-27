"""Proof-of-Semantic-Entropy."""
import hashlib


def pose_hash(x):
    return hashlib.sha256(str(x).encode()).hexdigest()
