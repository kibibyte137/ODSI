import hashlib

LICZBA_WIERSZY = 13
LICZBA_WARIANTOW = 1 << LICZBA_WIERSZY

def wczytaj_wiersze(sciezka: str) -> list[bytes]:
    with open(sciezka, "rb") as f:
        dane = f.read()
    wiersze = dane.split(b"\n")
    if wiersze and wiersze[-1] == b"":
        wiersze = wiersze[:-1]
    if len(wiersze) != LICZBA_WIERSZY:
        raise ValueError(f"{sciezka}: oczekiwano {LICZBA_WIERSZY} wierszy, jest {len(wiersze)}")
    return wiersze

def zbuduj_wariant(wiersze: list[bytes], v: int) -> bytes:
    czesci = []
    for i in range(LICZBA_WIERSZY):
        spacja = b" " if (v >> i) & 1 else b""
        czesci.append(wiersze[i] + spacja + b"\n")
    return b"".join(czesci)

def h24(dane: bytes) -> str:
    return hashlib.sha256(dane).digest()[:3].hex()

oryg = wczytaj_wiersze("oryginal.txt")
zmien = wczytaj_wiersze("zmieniony.txt")

mapa_oryg = {}
for v in range(LICZBA_WARIANTOW):
    klucz = h24(zbuduj_wariant(oryg, v))
    mapa_oryg.setdefault(klucz, v)

h24_oryg0 = h24(zbuduj_wariant(oryg, 0))
para = None
trafienia_w_oryginal0 = 0

for v in range(LICZBA_WARIANTOW):
    klucz = h24(zbuduj_wariant(zmien, v))
    if para is None and klucz in mapa_oryg:
        para = (mapa_oryg[klucz], v, klucz)
    if klucz == h24_oryg0:
        trafienia_w_oryginal0 += 1

print(f"h24 niezmienionego oryginału (wariant 0): {h24_oryg0}")
if para:
    v_o, v_z, klucz = para
    print(f"\nZnaleziona para o równym h24:")
    print(f"  wariant oryginału v={v_o}")
    print(f"  wariant zmienionego v={v_z}")
    print(f"  wspólny h24 = {klucz}")
else:
    print("\nNie znaleziono pary.")

print(f"\nIle wariantów zmienionego ma h24 == h24(oryginał v=0): {trafienia_w_oryginal0}")

