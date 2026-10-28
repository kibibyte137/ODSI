import os
import hashlib
import hmac

def sha256_pliku(sciezka: str) -> str:
    with open(sciezka, "rb") as f:
        dane = f.read()
    return hashlib.sha256(dane).hexdigest()

def sprawdz_sumy(plik_sum: str) -> None:
    katalog = os.path.dirname(os.path.abspath(plik_sum))
    with open(plik_sum, "r", encoding="utf-8") as f:
        for linia in f:
            linia = linia.rstrip("\n")
            if not linia.strip():
                continue
            oczekiwany_hex, wzgledna = linia.split("  ", 1)
            sciezka = os.path.join(katalog, wzgledna)
            try:
                faktyczny_hex = sha256_pliku(sciezka)
            except (FileNotFoundError, IsADirectoryError):
                print(f"{wzgledna}: BRAK")
                continue
            if hmac.compare_digest(faktyczny_hex, oczekiwany_hex.lower()):
                print(f"{wzgledna}: OK")
            else:
                print(f"{wzgledna}: BŁĄD")

def roznica_bitow_ala_ola() -> None:
    a = hashlib.sha256(b"Ala ma kota.").digest()
    b = hashlib.sha256(b"Ola ma kota.").digest()
    rozne = sum(bin(x ^ y).count("1") for x, y in zip(a, b))
    print(f"\nSHA-256('Ala ma kota.') = {a.hex()}")
    print(f"SHA-256('Ola ma kota.') = {b.hex()}")
    print(f"Różniących się bitów: {rozne} / 256")

plik_sum = "SHA256SUMS.txt"
print(f"Sprawdzam: {plik_sum}\n")
sprawdz_sumy(plik_sum)
roznica_bitow_ala_ola()
