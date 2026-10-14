import math
import sys
import time
from itertools import product

def read_file(path: str) -> bytes:
    with open(path, "rb") as f:
        data = f.read()
    return data

def write_file(path: str, data: bytes) -> None:
    with open(path, "wb") as f:
        f.write(data)

def rc4_ksa(key: bytes) -> list:
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def rc4_prga(S: list, length: int) -> bytes:
    S = S.copy()
    i = j = 0
    keystream = bytearray()
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
    return bytes(keystream)

def rc4_crypt(data: bytes, key: bytes) -> bytes:
    if not key:
        raise ValueError("Klucz nie może być pusty")
    S = rc4_ksa(key)
    keystream = rc4_prga(S, len(data))
    return bytes(d ^ k for d, k in zip(data, keystream))

def entropy(data: bytes) -> float:
    if not data:
        return 0.0
    counts = [0] * 256
    for b in data:
        counts[b] += 1
    n = len(data)
    return -sum(c / n * math.log2(c / n) for c in counts if c)

assert rc4_crypt(b"Plaintext", b"Key").hex() == "bbf316e8d940af0ad3"
probka = b"Ala ma kota \x00\xff"
assert rc4_crypt(rc4_crypt(probka, b"abc"), b"abc") == probka
assert rc4_crypt(b"", b"abc") == b""
print("Testy RC4: OK (wektor testowy, podwójne zastosowanie, puste dane)")

path = sys.argv[1] if len(sys.argv) > 1 else "rc4.bin"
cipher = read_file(path)
probe = cipher[:512]

start = time.perf_counter()
results = []
for letters in product(b"abcdefghijklmnopqrstuvwxyz", repeat=3):
    key = bytes(letters)
    results.append((entropy(rc4_crypt(probe, key)), key))
elapsed = time.perf_counter() - start

results.sort()
print(f"\nSprawdzono {len(results)} kluczy w {elapsed:.2f} s")
print("Top 5 kandydatów (entropia 512 B):")
for h, key in results[:5]:
    print(f"  {key.decode()}  {h:.4f}  {rc4_crypt(probe[:40], key)!r}")

best_key = results[0][1]
print(f"\nWybrany klucz: {best_key.decode()}")

plain = rc4_crypt(cipher, best_key)
write_file("rc4.txt", plain)
print("Zapisano rc4.txt, początek:", repr(plain[:80]))
print("Ponowne szyfrowanie == kryptogram:", rc4_crypt(plain, best_key) == cipher)
print(f"Entropia kryptogramu:   {entropy(cipher):.4f} bit/B")
print(f"Entropia odszyfrowania: {entropy(plain):.4f} bit/B")
