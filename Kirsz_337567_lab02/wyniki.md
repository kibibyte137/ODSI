# Zadanie 1
```
Top 5 kandydatów:
   k    ocena  początek odszyfrowania
 230   1.0000  b'Wkh#Qljkw#Ihuu|\r\rWkh#qljkw#ihuu|#ohiw#wkh#kduerxu#dw#hohyhq/'
 233   1.0000  b'The Night Ferry\n\nThe night ferry left the harbour at eleven,'
 228   0.9948  b'Ymj%Snlmy%Kjww~\x0f\x0fYmj%snlmy%kjww~%qjky%ymj%mfwgtzw%fy%jqj{js1'
 229   0.9948  b'Xli$Rmklx$Jivv}\x0e\x0eXli$rmklx$jivv}$pijx$xli$levfsyv$ex$ipizir0'
 231   0.9948  b'Vjg"Pkijv"Hgtt{\x0c\x0cVjg"pkijv"hgtt{"nghv"vjg"jctdqwt"cv"gngxgp.'

Podaj wybrane przesunięcie k (0-255): 233
Wybrane przesunięcie k = 233, ocena = 1.0000
Początek: b'The Night Ferry\n\nThe night ferry left the harbour at eleven, as it had done ever'
Zapisano cezar.txt
```
Wybrane przesunięcie to k = 233. Dwa przesunięcia (230 i 233) dają ocenę 1.0000, więc sama ocena drukowalności nie wystarcza - wybór rozstrzyga czytelność tekstu. Dla k = 233 otrzymujemy poprawny angielski tekst ("The Night Ferry...") z odstępami i znakami `\n`. Dla k = 230 każdy bajt jest o 3 większy: "Wkh" to "The" przesunięte o 3, spacja (32) staje się `#` (35), a `\n` (10) staje się `\r` (13) - wszystkie te znaki nadal są drukowalne, stąd remis.

Dlaczego entropia nie rozstrzyga: przesunięcie zamienia każdą wartość bajtu na inną, ale nie zmienia tego, ile razy każda wartość występuje - zmieniają się tylko "etykiety" w histogramie. Entropia liczy wyłącznie te liczby wystąpień, więc wychodzi taka sama dla każdego k. Nie mówi więc, który wynik wygląda jak tekst - do tego trzeba sprawdzić, jakie to są bajty (np. czy są drukowalne).

# Zadanie 2

```
Plik zgodny bajt po bajcie: True
Długość źródła: 2867 | długość kryptogramu: 2867
Puste dane: True
Bajty 0 i 255: True | kryptogram: 5a404d44cb5b3f
Klucz SZYFR: 95ac9a9393 | 95ac9a9393 | 95ac9a9393
Klucz KOD: 8da1859890 | 869d90918c | 91968c9c85
```

Tekst `BRAMA` powtarza się co 5 bajtów, więc przy kluczu `SZYFR` (m = 5) każde powtórzenie trafia na tę samą pozycję klucza (5 mod 5 = 0) i jest szyfrowane identycznymi bajtami, co daje identyczne fragmenty kryptogramu. Przy kluczu `KOD` (m = 3) każde powtórzenie zaczyna się od innej pozycji klucza (5 mod 3 = 2), a ta sama faza wróciłaby dopiero po NWW(5, 3) = 15 bajtach, czyli poza tym tekstem. Atakujący widzący powtórzone fragmenty wie, że tekst jawny się powtarza, a odległość powtórzeń jest wielokrotnością długości klucza.

# Zadanie 3

```
Testy RC4: OK (wektor testowy, podwójne zastosowanie, puste dane)

Sprawdzono 17576 kluczy w 1.32 s
Top 5 kandydatów (entropia 512 B):
  tat  4.3910  b"The Clockmaker's Apprentice\n\nOn his firs"
  neg  7.4304  b"\xe0m\x94\x94\xc5\xeb\xf6\x0b\xc8'\x91\x92\x08\xdd7\xd7\xabj \xc6\xad\xadn\xb8*\x91\xab5Hu\xcc<\xa4\x04\xba\xf9\x8aTn%"
  mcn  7.4512  b'V\xafMy\x04\xbb\x03_\xd8\xf1\xffq\x17\\\x01\xe4\x96h\xe7\x0e\xffH\xbb\xbbP\x90E\xf3\x07KF|@\x05\x80z`\x95\xfa5'
  oxo  7.4536  b'\xf4%Q\xa6\xb4\xbe\xec\x83\x7f\x0ecT\xda\x08\xa4?\xbc\xad\xbc\xa51\xb5\xaa\xd1\x02\x84\xaa\xa1\xa8\x98\xa6>e\x93\xd9MI\x08\xe6\xe9'
  tnx  7.4592  b'\xb3\x00f\xaen\xf3\xae\x98\xbb\xc0\x86\xa0p\xe8\xbbGHW\x0eA\xb6j(Bjp\x9b\xecP\xa21\xa0+u\xebxc\xd9/\x0c'

Wybrany klucz: tat
Zapisano rc4.txt, początek: b"The Clockmaker's Apprentice\n\nOn his first day in the workshop, Tomas was not all"
Ponowne szyfrowanie == kryptogram: True
Entropia kryptogramu:   7.9271 bit/B
Entropia odszyfrowania: 4.3259 bit/B
```

RC4 szyfruje i odszyfrowuje tą samą operacją (XOR z tym samym strumieniem bajtów), a dwukrotny XOR z tym samym strumieniem zawsze przywraca dane wejściowe. Dlatego ponowne szyfrowanie odtworzy kryptogram dla każdego klucza, także błędnego - ten test sprawdza tylko, czy kod działa spójnie, a nie czy klucz jest dobry. Ranking entropii mógłby zawieść, gdyby tekst jawny sam wyglądał losowo (np. plik skompresowany lub zaszyfrowany) albo gdyby próbka była za krótka, żeby odróżnić tekst od przypadkowych bajtów.

