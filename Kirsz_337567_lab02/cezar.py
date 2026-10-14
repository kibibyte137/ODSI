import sys

def read_file(path: str) -> bytes:
    with open(path, "rb") as f:
        data = f.read()
    return data

def write_file(path: str, data: bytes) -> None:
    with open(path, "wb") as f:
        f.write(data)

def caesar_decrypt(data: bytes, k: int) -> bytes:
    return bytes((c - k) % 256 for c in data)

PRINTABLE = set(range(32, 127)) | {9, 10, 13}

def printable_score(data: bytes) -> float:
    if not data:
        return 0.0
    return sum(b in PRINTABLE for b in data) / len(data)

def rank_shifts(data: bytes):
    results = []
    for k in range(256):
        plain = caesar_decrypt(data, k)
        results.append((printable_score(plain), k, plain))
    results.sort(key=lambda r: (-r[0], r[1]))
    return results

path = sys.argv[1] if len(sys.argv) > 1 else "cezar.bin"
data = read_file(path)
rankings = rank_shifts(data)

print("Top 5 kandydatów:")
print(f"{'k':>4}  {'ocena':>7}  początek odszyfrowania")
for score, k, plain in rankings[:5]:
    preview = plain[:60]
    print(f"{k:>4}  {score:7.4f}  {preview!r}")

while True:
    wybor = input("\nPodaj wybrane przesunięcie k (0-255): ").strip()
    if wybor.isdigit() and 0 <= int(wybor) <= 255:
        k = int(wybor)
        break
    print("Niepoprawna wartość, podaj liczbę 0-255.")
plain = caesar_decrypt(data, k)
write_file("cezar.txt", plain)
print(f"Wybrane przesunięcie k = {k}, ocena = {printable_score(plain):.4f}")
print("Początek:", repr(plain[:80]))
print("Zapisano cezar.txt")