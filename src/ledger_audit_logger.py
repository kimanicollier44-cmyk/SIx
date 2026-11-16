import hashlib
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class DecentralizedLedgerAuditLogger:
    """Immutable hash-chained audit logger for tracking mesh state transitions and safety violations."""
    def __init__(self):
        self.chain = []
        self.genesis_block()

    def genesis_block(self):
        block = {"index": 0, "prev_hash": "0" * 64, "data": "SIx Genesis Block", "hash": self._hash_block("0" * 64, "SIx Genesis Block")}
        self.chain.append(block)

    def _hash_block(self, prev_hash: str, data: str) -> str:
        hasher = hashlib.sha256()
        hasher.update(f"{prev_hash}:{json.dumps(data)}".encode())
        return hasher.hexdigest()

    def append_entry(self, data: dict):
        prev_block = self.chain[-1]
        new_hash = self._hash_block(prev_block['hash'], str(data))
        new_block = {"index": len(self.chain), "prev_hash": prev_block['hash'], "data": data, "hash": new_hash}
        self.chain.append(new_block)
        logging.info(f"Audit Log Appended [Index {new_block['index']}]: {new_hash[:16]}...")
