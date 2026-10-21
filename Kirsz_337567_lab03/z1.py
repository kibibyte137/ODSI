from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK = 16

plaintext = b"0123456789ABCDEF" * 4
key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
assert len(plaintext) == 64 and len(key) == 16

def blocks(data: bytes) -> list[bytes]:
    return [data[i:i + BLOCK] for i in range(0, len(data), BLOCK)]

def report(name: str, data: bytes) -> None:
    bl = blocks(data)
    print(f"\n{name}:")
    for i, b in enumerate(bl):
        print(f"  blok {i}: {b.hex()}")
    pairs = [(i, j) for i in range(len(bl)) for j in range(i + 1, len(bl)) if bl[i] == bl[j]]
    if pairs:
        print("  równe bloki:", ", ".join(f"{i}={j}" for i, j in pairs))
    else:
        print("  równe bloki: brak")

ct_ecb = AES.new(key, AES.MODE_ECB).encrypt(plaintext)

iv = get_random_bytes(16)
ct_cbc = AES.new(key, AES.MODE_CBC, iv=iv).encrypt(plaintext)

print("Tekst jawny:", plaintext.decode())
print("Klucz:", key.hex())
print("IV (CBC):", iv.hex())
report("ECB", ct_ecb)
report("CBC", ct_cbc)

pt_ecb = AES.new(key, AES.MODE_ECB).decrypt(ct_ecb)
pt_cbc = AES.new(key, AES.MODE_CBC, iv=iv).decrypt(ct_cbc)

print("\nOdszyfrowanie ECB == wejście:", pt_ecb == plaintext)
print("Odszyfrowanie CBC == wejście:", pt_cbc == plaintext)