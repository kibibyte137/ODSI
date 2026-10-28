import hmac
import hashlib
import secrets

ITERACJE_DOMYSLNE = 600_000
DLUGOSC_WYNIKU = 32
DLUGOSC_SOLI = 16

def pbkdf2(haslo: str, sol: bytes, iteracje: int) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", haslo.encode("utf-8"), sol, iteracje, DLUGOSC_WYNIKU)

def wczytaj_baze(sciezka: str) -> dict:
    baza = {}
    with open(sciezka, "r", encoding="utf-8") as f:
        for linia in f:
            linia = linia.strip()
            if not linia:
                continue
            login, iteracje, sol_hex, skrot_hex = linia.split(":")
            baza[login] = (int(iteracje), bytes.fromhex(sol_hex), bytes.fromhex(skrot_hex))
    return baza

def weryfikuj(baza: dict, login: str, haslo: str) -> bool:
    if login not in baza:
        return False
    iteracje, sol, zapisany = baza[login]
    policzony = pbkdf2(haslo, sol, iteracje)
    return hmac.compare_digest(policzony, zapisany)

def dodaj(login: str, haslo: str) -> str:
    sol = secrets.token_bytes(DLUGOSC_SOLI)
    skrot = pbkdf2(haslo, sol, ITERACJE_DOMYSLNE)
    return f"{login}:{ITERACJE_DOMYSLNE}:{sol.hex()}:{skrot.hex()}"

def wczytaj_baze_z_linii(linie) -> dict:
    baza = {}
    for linia in linie:
        login, iteracje, sol_hex, skrot_hex = linia.strip().split(":")
        baza[login] = (int(iteracje), bytes.fromhex(sol_hex), bytes.fromhex(skrot_hex))
    return baza

baza = wczytaj_baze("hasla.txt")

print("=== Weryfikacja ===")
testy = [
    ("anna", "Kasztan-2026"),
    ("anna", "kasztan-2026"),
    ("piotr", "Żółw na łące"),
    ("kasia", "Kasztan-2026"),
]
for login, haslo in testy:
    print(f"  weryfikuj({login!r}, ...) -> {weryfikuj(baza, login, haslo)}")

print("\n=== Nowe konta (dodaj) ===")
wspolne_haslo = "To samo haslo 123"
rek1 = dodaj("test1", wspolne_haslo)
rek2 = dodaj("test2", wspolne_haslo)

_, _, sol1, skrot1 = rek1.split(":")
_, _, sol2, skrot2 = rek2.split(":")
print(f"  sól test1 == sól test2 ? {sol1 == sol2}")
print(f"  skrót test1 == skrót test2 ? {skrot1 == skrot2}")

nowa = wczytaj_baze_z_linii([rek1, rek2])
print(f"  weryfikuj('test1', wspólne hasło) -> {weryfikuj(nowa, 'test1', wspolne_haslo)}")
print(f"  weryfikuj('test2', wspólne hasło) -> {weryfikuj(nowa, 'test2', wspolne_haslo)}")



