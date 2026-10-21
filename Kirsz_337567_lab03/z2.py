from pathlib import Path

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

PASSWORD = "test-haslo-123"
ITERATIONS = 200_000
KEY_LEN = 32
SALT_LEN = 16
IV_LEN = 16
BLOCK = AES.block_size

def derive_key(password: str, salt: bytes) -> bytes:
    return PBKDF2(password.encode("utf-8"), salt, dkLen=KEY_LEN, count=ITERATIONS, hmac_hash_module=SHA256)

def encrypt(password: str, data: bytes) -> tuple[bytes, bytes, bytes]:
    salt = get_random_bytes(SALT_LEN)
    iv = get_random_bytes(IV_LEN)
    key = derive_key(password, salt)
    ct = AES.new(key, AES.MODE_CBC, iv=iv).encrypt(pad(data, BLOCK, style="pkcs7"))
    return salt, iv, ct

def decrypt(password: str, salt: bytes, iv: bytes, ct: bytes) -> bytes:
    key = derive_key(password, salt)
    return unpad(AES.new(key, AES.MODE_CBC, iv=iv).decrypt(ct), BLOCK, style="pkcs7")

def expected_ct_len(n: int) -> int:
    return (n // BLOCK + 1) * BLOCK

def run_test(name: str, data: bytes) -> bytes:
    salt, iv, ct = encrypt(PASSWORD, data)
    recovered = decrypt(PASSWORD, salt, iv, ct)
    same = recovered == data
    len_ok = len(ct) == expected_ct_len(len(data))
    print(f"[{name}] wejście: {len(data)} B, kryptogram: {len(ct)} B "
          f"(oczekiwano {expected_ct_len(len(data))}) -> "
          f"bajty równe: {same}, długość OK: {len_ok}")
    assert same and len_ok
    return ct

run_test("puste dane", b"")
run_test("16 B ASCII", b"0123456789ABCDEF")
message = Path("wiadomosc.txt").read_bytes()
run_test("wiadomosc.txt", message)

salt1, iv1, ct1 = encrypt(PASSWORD, message)
salt2, iv2, ct2 = encrypt(PASSWORD, message)
print("\nSzyfrowanie 1: sól", salt1.hex(), "IV", iv1.hex())
print("  kryptogram:", ct1.hex())
print("Szyfrowanie 2: sól", salt2.hex(), "IV", iv2.hex())
print("  kryptogram:", ct2.hex())
print("Kryptogramy równe:", ct1 == ct2)
print("Oba odszyfrowują się poprawnie:", decrypt(PASSWORD, salt1, iv1, ct1) == message == decrypt(PASSWORD, salt2, iv2, ct2))