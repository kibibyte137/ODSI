import math
from collections import Counter
from pathlib import Path

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789"
SAMPLE_LEN = 4096
BLOCK = AES.block_size

def entropy(data: bytes) -> float:
    n = len(data)
    counts = Counter(data)
    return -sum((c / n) * math.log2(c / n) for c in counts.values())

def make_key(ch: str) -> bytes:
    return (ch * 16).encode("ascii")

path = Path("slaby_ecb.bin")
ct = path.read_bytes()
print(f"Plik: {path.name}, {len(ct)} B")

sample = ct[:SAMPLE_LEN]
sample = sample[:len(sample) - len(sample) % BLOCK]

candidates = []
for ch in ALPHABET:
    pt = AES.new(make_key(ch), AES.MODE_ECB).decrypt(sample)
    candidates.append((entropy(pt), ch))

candidates.sort()
print("\nTop 5 kandydatów (najniższa entropia):")
for h, ch in candidates[:5]:
    print(f"  '{ch}'  H = {h:.4f}")

best_h, best = candidates[0]
plaintext = unpad(AES.new(make_key(best), AES.MODE_ECB).decrypt(ct), BLOCK, style="pkcs7")
text = plaintext.decode("utf-8")
print(f"\nNajlepszy klucz: '{best}' * 16 = {make_key(best)!r}")
print("Pierwszy wiersz:", text.splitlines()[0])
printable = sum(c.isprintable() or c in "\r\n\t" for c in text) / len(text)
print(f"Udział znaków drukowalnych: {printable:.2%}")