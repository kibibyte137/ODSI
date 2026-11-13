```text
kinia@kawk2 pliki-dla-studentow % docker compose up -d
failed to connect to the docker API at unix:///Users/kinia/.docker/run/docker.sock; check if the path is correct and if the daemon is running: dial unix /Users/kinia/.docker/run/docker.sock: connect: no such file or directory
kinia@kawk2 pliki-dla-studentow % docker compose up -d
[+] up 1/1
 ✘ Image ochrona-danych-lab06:local Error pull access denied for ochron...  2.2s
[+] Building 7.5s (9/9) FINISHED
 => [internal] load local bake definitions                                 0.0s
 => => reading from stdin 595B                                             0.0s
 => [internal] load build definition from Dockerfile                       0.0s
 => => transferring dockerfile: 229B                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.12-alpine      1.8s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 81B                                           0.0s
 => [1/3] FROM docker.io/library/python:3.12-alpine@sha256:c5ba3deef00c77  2.0s
 => => resolve docker.io/library/python:3.12-alpine@sha256:c5ba3deef00c77  0.0s
 => => sha256:8ab1992027dfd42035e1028c42f93c50180a2b01b89a264 251B / 251B  0.1s
 => => sha256:9cee687b648e8e2f38b10079e58e752f383ebe19b 13.92MB / 13.92MB  1.5s
 => => sha256:6d356b48c1c56cccd22e48f043c1e8ac8d79ef8 415.54kB / 415.54kB  0.7s
 => => sha256:b90627b8f4292fd3cb63f0f27f0b11c37f04ba88ef3 4.19MB / 4.19MB  1.7s
 => => extracting sha256:b90627b8f4292fd3cb63f0f27f0b11c37f04ba88ef3b78d4  0.1s
 => => extracting sha256:6d356b48c1c56cccd22e48f043c1e8ac8d79ef86f9e625b5  0.1s
 => => extracting sha256:9cee687b648e8e2f38b10079e58e752f383ebe19bea21c5a  0.2s
 => => extracting sha256:8ab1992027dfd42035e1028c42f93c50180a2b01b89a2645  0.0s
 => [2/3] RUN pip install --no-cache-dir flask==3.1.3 werkzeug==3.1.9 jin  2.9s
 => [3/3] WORKDIR /app                                                     0.0s
 => exporting to image                                                     0.6s
 => => exporting layers                                                    0.2s
 => => exporting manifest sha256:f3c4a6dcf08e2b3ba68a4dbd13c47b5793a24e00  0.0s
 => => exporting config sha256:976f76feb7ef1ab514515e79c779fcf7e702be2ca1  0.0s
 => => exporting attestation manifest sha256:7daf27f2827021fef513ae4b01db  0.0s
 => => exporting manifest list sha256:15c85d0a187848ebad493636ce3045595b5  0.0s
 => => naming to docker.io/library/ochrona-danych-lab06:local              0.0s
 => => unpacking to docker.io/library/ochrona-danych-lab06:local           0.4s
 => resolving provenance for metadata file                                 0.0s
[+] up 4/4
 ✔ Image ochrona-danych-lab06:local         Built                           9.9s
 ✔ Network pliki-dla-studentow_default      Created                         0.0s
 ✔ Container pliki-dla-studentow-zbieracz-1 Started                         0.2s
 ✔ Container pliki-dla-studentow-web-1      Started                         0.2s
kinia@kawk2 pliki-dla-studentow % curl -s "http://127.0.0.1:8080/szukaj?q=<script>x</script>"
<!doctype html><meta charset='utf-8'><title>Szukaj</title><h1>Wyniki wyszukiwania dla: <script>x</script></h1><ul></ul><p><a href='/'>Powrót</a></p>%           kinia@kawk2 pliki-dla-studentow % docker compose restart web
[+] restart 0/1
 ⠙ Container pliki-dla-studentow-web-1 Restarting                           3.2s
kinia@kawk2 pliki-dla-studentow % curl -s "http://127.0.0.1:8080/szukaj?q=<script>x</script>"
<!doctype html><meta charset='utf-8'><title>Szukaj</title><h1>Wyniki wyszukiwania dla: &lt;script&gt;x&lt;/script&gt;</h1><ul></ul><p><a href='/'>Powrót</a></p>kinia@kawk2 pliki-dla-studentow % docker compose logs zbieracz
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
kinia@kawk2 pliki-dla-studentow % curl -i -d "login=anna&haslo=***" http://127.0.0.1:8080/logowanie | grep -i set-cookie
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   215  100   189  100    26  50199   6905 --:--:-- --:--:-- --:--:-- 71666
Set-Cookie: session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb7TA.gjFm5X6V19mBppljVqW2vGlCpcs; Path=/
kinia@kawk2 pliki-dla-studentow % curl -i -b "session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA" http://127.0.0.1:8080/notatka
HTTP/1.1 200 OK
Server: Werkzeug/3.1.9 Python/3.12.16
Date: Fri, 13 Nov 2026 11:58:36 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 481
Vary: Cookie
Connection: close

<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Notatka</title>
<link rel="stylesheet" href="/static/styl.css"></head>
<body>
<nav><a href="/">Tablica</a> | <a href="/szukaj?q=">Szukaj</a> | <a href="/podglad">Podgląd</a> |
<a href="/notatka">Moja notatka</a> | <a href="/logowanie">Logowanie</a> | <a href="/wyloguj">Wyloguj</a></nav>

<h1>Notatka użytkownika anna</h1>
<p>Prywatna notatka Anny: kod do szafki w pracowni 4721 (fikcyjny).</p>

</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % curl -i -b "session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA" http://127.0.0.1:8080/notatka
HTTP/1.1 200 OK
Server: Werkzeug/3.1.9 Python/3.12.16
Date: Fri, 13 Nov 2026 12:00:36 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 481
Vary: Cookie
Connection: close

<!doctype html>
<html lang="pl">
<head><meta charset="utf-8"><title>Notatka</title>
<link rel="stylesheet" href="/static/styl.css"></head>
<body>
<nav><a href="/">Tablica</a> | <a href="/szukaj?q=">Szukaj</a> | <a href="/podglad">Podgląd</a> |
<a href="/notatka">Moja notatka</a> | <a href="/logowanie">Logowanie</a> | <a href="/wyloguj">Wyloguj</a></nav>

<h1>Notatka użytkownika anna</h1>
<p>Prywatna notatka Anny: kod do szafki w pracowni 4721 (fikcyjny).</p>

</body>
</html>%                                                                        kinia@kawk2 pliki-dla-studentow % docker compose restart web
[+] restart 0/1
 ⠙ Container pliki-dla-studentow-web-1 Restarting                           3.2s
kinia@kawk2 pliki-dla-studentow % docker compose logs zbieracz
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
kinia@kawk2 pliki-dla-studentow % curl -i -d "login=anna&haslo=***" http://127.0.0.1:8080/logowanie | grep -i set-cookie
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   215  100   189  100    26  77079  10603 --:--:-- --:--:-- --:--:--  104k
Set-Cookie: session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb-TQ.681nsHnWZ64Xa3ZzGzlvOQcxxRE; HttpOnly; Path=/
kinia@kawk2 pliki-dla-studentow % docker compose restart zbieracz
[+] restart 0/1
 ⠙ Container pliki-dla-studentow-zbieracz-1 Restarting                      3.2s
kinia@kawk2 pliki-dla-studentow % docker compose logs zbieracz
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
kinia@kawk2 pliki-dla-studentow % docker compose logs zbieracz
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
kinia@kawk2 pliki-dla-studentow % docker compose restart web
[+] restart 0/1
 ⠙ Container pliki-dla-studentow-web-1 Restarting                           3.1s
kinia@kawk2 pliki-dla-studentow % docker compose restart zbieracz
[+] restart 0/1
 ⠙ Container pliki-dla-studentow-zbieracz-1 Restarting                      3.1s
kinia@kawk2 pliki-dla-studentow % docker compose logs zbieracz
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
kinia@kawk2 pliki-dla-studentow % docker compose restart zbieracz
[+] restart 0/1
 ⠙ Container pliki-dla-studentow-zbieracz-1 Restarting                      3.2s
kinia@kawk2 pliki-dla-studentow % docker compose logs zbieracz
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoic3R1ZGVudCJ9.avb5MQ.RkCWdN_C1Ina-KRadVYU0pmACuc
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=session=eyJ1enl0a293bmlrIjoiYW5uYSJ9.avb5uw.XsVRmVhKDtHkfo7t0hCYD4uDBbA
zbieracz-1  | ZEBRANO: /?c=
kinia@kawk2 pliki-dla-studentow % docker compose restart web```