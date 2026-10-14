import sys

def read_file(path: str) -> bytes:
    with open(path, "rb") as f:
        data = f.read()
    return data

def write_file(path: str, data: bytes) -> None:
    with open(path, "wb") as f:
        f.write(data)

def vigenere_encrypt(data: bytes, K: bytes) -> bytes:
    if not K:
        raise ValueError("Klucz nie może być pusty")
    m = len(K)
    return bytes((p + K[i % m]) % 256 for i, p in enumerate(data))

def vigenere_decrypt(data: bytes, K: bytes) -> bytes:
    if not K:
        raise ValueError("Klucz nie może być pusty")
    m = len(K)
    return bytes((c - K[i % m]) % 256 for i, c in enumerate(data))

def chunks_hex(data: bytes, size: int = 5) -> list:
    return [data[i:i + size].hex() for i in range(0, len(data), size)]

key = b"ZAMEK"
path = sys.argv[1] if len(sys.argv) > 1 else "tekst_pl.txt"
data = read_file(path)
wynik = vigenere_encrypt(data, key)
write_file("vigenere.bin", wynik)

odszyfrowane = vigenere_decrypt(read_file("vigenere.bin"), key)
print("Plik zgodny bajt po bajcie:", odszyfrowane == data)
print("Długość źródła:", len(data), "| długość kryptogramu:", len(wynik))

puste = b""
print("Puste dane:", vigenere_decrypt(vigenere_encrypt(puste, key), key) == puste)

skrajne = bytes([0, 255, 0, 255, 128, 1, 254])
zaszyfr = vigenere_encrypt(skrajne, key)
print("Bajty 0 i 255:", vigenere_decrypt(zaszyfr, key) == skrajne, "| kryptogram:", zaszyfr.hex())
assert vigenere_encrypt(b"\xff", b"A") == b"\x40"
assert vigenere_decrypt(b"\x00", b"A") == b"\xbf"

jawny = b"BRAMABRAMABRAMA"
for k in (b"SZYFR", b"KOD"):
    c = vigenere_encrypt(jawny, k)
    print(f"Klucz {k.decode()}: {' | '.join(chunks_hex(c))}")
