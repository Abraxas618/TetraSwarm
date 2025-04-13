"""
Run All TetraCrypt Modules: Demonstration CLI
Author: Michael Tass MacDonald
Version: v0.1.0
"""

import os

def run_external_simulations():
    print("🚀 Running Quantum + Swarm Simulations")
    os.system("python3 sim/simulate_quantum_attack.py")
    os.system("python3 sim/simulate_swarm.py")

def run_internal_demos():
    try:
        from src.tke import TetrahedralKeyExchange
        from src.qidl_encrypt import QIDLEncoder
        from src.rth import RecursiveTesseractHash
        from src.hbb_blockchain import HypercubeBlockchain
    except ImportError as e:
        print(f"[!] Import failed: {e}")
        return

    print("\n🧪 Running Core Module Demos")

    tke = TetrahedralKeyExchange()
    private_key, public_key = tke.generate_keypair()
    print("TKE Public Key:", public_key)

    message = "Hello, Hyperdimensional World!"
    qidl = QIDLEncoder()
    ciphertext, shared_secret = qidl.encrypt(public_key, message)
    print("QIDL Encrypted:", ciphertext)

    decrypted = qidl.decrypt(private_key, ciphertext, shared_secret)
    print("QIDL Decrypted:", decrypted)

    rth = RecursiveTesseractHash()
    bio_sample = b"EEG_SAMPLE|DNA_SAMPLE"
    hashed = rth.hash(bio_sample)
    print("RTH Hash:", hashed.hex())

    hbb = HypercubeBlockchain()
    hbb.add_block({"payload": hashed.hex()})
    print("HBB Chain Length:", len(hbb.chain))

if __name__ == "__main__":
    run_external_simulations()
    run_internal_demos()
