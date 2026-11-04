# Przygotowanie przed zajęciami
Środowisko: Apache/2.4.69, Python 3.14.10, Docker 29.9.2 (Docker Desktop 4.98.0, linux/arm64)
## Punkt 3.
```text
kinia@kawk2 pliki-dla-studentow % docker compose build web
 ✔ Image ochrona-danych-lab05:local Built                                2.5s
kinia@kawk2 pliki-dla-studentow % docker compose up -d web
[+] up 2/2
 ✔ Network pliki-dla-studentow_default Created                           0.0s
 ✔ Container pliki-dla-studentow-web-1 Started                           0.1s
kinia@kawk2 pliki-dla-studentow % docker compose exec web httpd -t
Syntax OK
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 07:45:21 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 06:04:00 GMT
ETag: "15f-65f6d252c5400"
Accept-Ranges: bytes
Content-Length: 351
Content-Type: text/html; charset=UTF-8

<!doctype html>
<html lang="pl"><meta charset="utf-8"><title>Laboratorium 5</title>
<h1>Laboratorium 5: serwer WWW działa</h1>
<p>Materiały ćwiczeniowe do konfiguracji dostępu w Apache.</p>
<ul><li><a href="/materialy/">Materiały</a></li>
<li><a href="/wewnetrzne/">Wewnętrzne</a></li>
<li><a href="/panel/raport.txt">Panel</a></li></ul></html>
kinia@kawk2 pliki-dla-studentow % docker compose logs --tail 30 web
web-1  | [Wed Nov 04 07:44:59.949393 2026] [mpm_event:notice] [pid 1:tid 1] AH00489: Apache/2.4.69 (Unix) configured -- resuming normal operations
web-1  | [Wed Nov 04 07:44:59.949415 2026] [core:notice] [pid 1:tid 1] AH00094: Command line: 'httpd -D FOREGROUND'
web-1  | 172.18.0.1 - - [04/Nov/2026:07:45:21 +0000] "GET / HTTP/1.1" 200 351
kinia@kawk2 pliki-dla-studentow % docker compose down
[+] down 2/2
 ✔ Container pliki-dla-studentow-web-1 Removed                           1.1s
 ✔ Network pliki-dla-studentow_default Removed                           0.1s
```

## Punkt 5.

| Test | Wynik                                                      |
|---|------------------------------------------------------------|
| curl -i /materialy/notatka.txt | 200: linia statusu, nagłówki, pusta linia, treść           |
| curl -i /materialy/ | 200: lista plików (Options Indexes)                        |
| curl -i /nie-ma-takiego | 404                                                        |
| /panel/raport.txt bez danych / złe hasło / dobre hasło | 401 / 401 / 200                                            |
| Authorization: Basic c3R1ZGVudDp6bGU= | base64 -d -> student:zle, czyli kodowanie, nie szyfrowanie |
| /cgi-bin/hello.cgi | 200, uid=2(daemon): CGI działa jako daemon                 |

```text
kinia@kawk2 pliki-dla-studentow % docker compose up -d --build web
 ✔ Image ochrona-danych-lab05:local    Built                             2.4s
 ✔ Network pliki-dla-studentow_default Created                           0.0s
 ✔ Container pliki-dla-studentow-web-1 Started                           0.1s
kinia@kawk2 pliki-dla-studentow % docker compose exec web python3 --version
Python 3.14.10
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/materialy/notatka.txt
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 08:04:35 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 06:04:00 GMT
ETag: "45-65f6d252c5400"
Accept-Ranges: bytes
Content-Length: 69
Content-Type: text/plain; charset=UTF-8

Publiczna notatka: ten plik ma pozostac dostepny pod znanym adresem.
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/materialy/
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 08:04:45 GMT
Server: Apache
Content-Length: 305
Content-Type: text/html;charset=ISO-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>Index of /materialy</title>
 </head>
 <body>
<h1>Index of /materialy</h1>
<ul><li><a href="/"> Parent Directory</a></li>
<li><a href="notatka.txt"> notatka.txt</a></li>
</ul>
</body></html>
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/nie-ma-takiego
HTTP/1.1 404 Not Found
Date: Wed, 04 Nov 2026 08:05:00 GMT
Server: Apache
Content-Length: 236
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
</body></html>
kinia@kawk2 pliki-dla-studentow % docker compose run --rm narzedzia -c -B /auth/uzytkownicy student
Container pliki-dla-studentow-narzedzia-run-14021a73fea7 Creating
Container pliki-dla-studentow-narzedzia-run-14021a73fea7 Created
New password:
Re-type new password:
Adding password for user student
kinia@kawk2 pliki-dla-studentow % cat auth/uzytkownicy
student:$2y$05$...
kinia@kawk2 pliki-dla-studentow % docker compose exec web httpd -t
Syntax OK
kinia@kawk2 pliki-dla-studentow % docker compose restart web
[+] restart 0/1
 ⠙ Container pliki-dla-studentow-web-1 Restarting                        1.2s
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/panel/raport.txt
HTTP/1.1 401 Unauthorized
Date: Wed, 04 Nov 2026 08:12:26 GMT
Server: Apache
WWW-Authenticate: Basic realm="Panel LAB05"
Content-Length: 421
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
</body></html>
kinia@kawk2 pliki-dla-studentow % curl -i -u student:zle http://127.0.0.1:8080/panel/raport.txt
HTTP/1.1 401 Unauthorized
Date: Wed, 04 Nov 2026 08:13:44 GMT
Server: Apache
WWW-Authenticate: Basic realm="Panel LAB05"
Content-Length: 421
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
</body></html>
kinia@kawk2 pliki-dla-studentow % curl -i -u student http://127.0.0.1:8080/panel/raport.txt
Enter host password for user 'student':
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 08:14:21 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 06:04:00 GMT
ETag: "3a-65f6d252c5400"
Accept-Ranges: bytes
Content-Length: 58
Content-Type: text/plain; charset=UTF-8

Raport cwiczeniowy: dostep po poprawnym uwierzytelnieniu.
kinia@kawk2 pliki-dla-studentow % docker compose logs --tail 10 web
web-1  | 172.18.0.1 - - [04/Nov/2026:08:04:35 +0000] "GET /materialy/notatka.txt HTTP/1.1" 200 69
web-1  | 172.18.0.1 - - [04/Nov/2026:08:04:45 +0000] "GET /materialy/ HTTP/1.1" 200 305
web-1  | 172.18.0.1 - - [04/Nov/2026:08:05:00 +0000] "GET /nie-ma-takiego HTTP/1.1" 404 236
web-1  | [Wed Nov 04 08:12:16.353111 2026] [mpm_event:notice] [pid 1:tid 1] AH00492: caught SIGWINCH, shutting down gracefully
web-1  | [Wed Nov 04 08:12:17.524083 2026] [mpm_event:notice] [pid 1:tid 1] AH00489: Apache/2.4.69 (Unix) configured -- resuming normal operations
web-1  | [Wed Nov 04 08:12:17.524098 2026] [core:notice] [pid 1:tid 1] AH00094: Command line: 'httpd -D FOREGROUND'
web-1  | 172.18.0.1 - - [04/Nov/2026:08:12:26 +0000] "GET /panel/raport.txt HTTP/1.1" 401 421
web-1  | [Wed Nov 04 08:13:44.673967 2026] [auth_basic:error] [pid 10:tid 19] [client 172.18.0.1:61000] AH01617: user student: authentication failure for "/panel/raport.txt": Password Mismatch
web-1  | 172.18.0.1 - student [04/Nov/2026:08:13:44 +0000] "GET /panel/raport.txt HTTP/1.1" 401 421
web-1  | 172.18.0.1 - student [04/Nov/2026:08:14:21 +0000] "GET /panel/raport.txt HTTP/1.1" 200 58
kinia@kawk2 pliki-dla-studentow % curl -v -u student:zle http://127.0.0.1:8080/panel/raport.txt 2>&1 | grep Authorization
> Authorization: Basic c3R1ZGVudDp6bGU=
kinia@kawk2 pliki-dla-studentow % echo 'c3R1ZGVudDp6bGU=' | base64 -d
student:zle%                                                                 kinia@kawk2 pliki-dla-studentow %
kinia@kawk2 pliki-dla-studentow % docker compose up -d --build web
 ✔ Image ochrona-danych-lab05:local    Built                             1.6s
 ✔ Container pliki-dla-studentow-web-1 Started                           1.2s
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/cgi-bin/hello.cgi
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 08:19:17 GMT
Server: Apache
Transfer-Encoding: chunked
Content-Type: text/plain; charset=utf-8

Witaj z CGI
uid=2(daemon) gid=2(daemon) groups=1(bin),2(daemon),2(daemon),4(adm)
kinia@kawk2 pliki-dla-studentow %
```

# Laboratorium 5

## Zadanie 1
### Przed dodaniem reguł
```text
kinia@kawk2 pliki-dla-studentow % docker compose up -d web
[+] up 2/2
 ✔ Network pliki-dla-studentow_default Created                              0.0s
 ✔ Container pliki-dla-studentow-web-1 Started                              0.1s
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/materialy/
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:27:15 GMT
Server: Apache
Content-Length: 305
Content-Type: text/html;charset=ISO-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>Index of /materialy</title>
 </head>
 <body>
<h1>Index of /materialy</h1>
<ul><li><a href="/"> Parent Directory</a></li>
<li><a href="notatka.txt"> notatka.txt</a></li>
</ul>
</body></html>
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/materialy/notatka.txt
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:27:25 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 06:04:00 GMT
ETag: "45-65f6d252c5400"
Accept-Ranges: bytes
Content-Length: 69
Content-Type: text/plain; charset=UTF-8

Publiczna notatka: ten plik ma pozostac dostepny pod znanym adresem.
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/wewnetrzne/
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:27:33 GMT
Server: Apache
Content-Length: 301
Content-Type: text/html;charset=ISO-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>Index of /wewnetrzne</title>
 </head>
 <body>
<h1>Index of /wewnetrzne</h1>
<ul><li><a href="/"> Parent Directory</a></li>
<li><a href="plan.txt"> plan.txt</a></li>
</ul>
</body></html>
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/wewnetrzne/plan.txt
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:27:41 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 06:04:00 GMT
ETag: "3a-65f6d252c5400"
Accept-Ranges: bytes
Content-Length: 58
Content-Type: text/plain; charset=UTF-8

Fikcyjny plan: ten katalog ma byc niedostepny przez HTTP.
kinia@kawk2 pliki-dla-studentow %
```
### Dodane reguły
```text
<Directory "/usr/local/apache2/htdocs/materialy">
    Options -Indexes
</Directory>

<Directory "/usr/local/apache2/htdocs/wewnetrzne">
    Require all denied
</Directory>
```


### Po dodaniu reguł
```text
kinia@kawk2 pliki-dla-studentow % docker compose exec web httpd -t
Syntax OK
kinia@kawk2 pliki-dla-studentow % docker compose restart web
[+] restart 0/1
 ⠙ Container pliki-dla-studentow-web-1 Restarting                           1.2s
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/materialy/
HTTP/1.1 403 Forbidden
Date: Wed, 04 Nov 2026 11:46:04 GMT
Server: Apache
Content-Length: 239
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
</body></html>
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/materialy/notatka.txt
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 11:46:30 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 06:04:00 GMT
ETag: "45-65f6d252c5400"
Accept-Ranges: bytes
Content-Length: 69
Content-Type: text/plain; charset=UTF-8

Publiczna notatka: ten plik ma pozostac dostepny pod znanym adresem.
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/wewnetrzne/
HTTP/1.1 403 Forbidden
Date: Wed, 04 Nov 2026 11:47:02 GMT
Server: Apache
Content-Length: 239
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
</body></html>
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/wewnetrzne/plan.txt
HTTP/1.1 403 Forbidden
Date: Wed, 04 Nov 2026 11:47:17 GMT
Server: Apache
Content-Length: 239
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
</body></html>
kinia@kawk2 pliki-dla-studentow %
```
### Logi
```text
kinia@kawk2 pliki-dla-studentow % docker compose logs --tail 30 web
web-1  | [Wed Nov 04 11:23:33.536496 2026] [mpm_event:notice] [pid 1:tid 1] AH00489: Apache/2.4.69 (Unix) configured -- resuming normal operations
web-1  | [Wed Nov 04 11:23:33.536518 2026] [core:notice] [pid 1:tid 1] AH00094: Command line: 'httpd -D FOREGROUND'
web-1  | 172.18.0.1 - - [04/Nov/2026:11:27:15 +0000] "GET /materialy/ HTTP/1.1" 200 305
web-1  | 172.18.0.1 - - [04/Nov/2026:11:27:25 +0000] "GET /materialy/notatka.txt HTTP/1.1" 200 69
web-1  | 172.18.0.1 - - [04/Nov/2026:11:27:33 +0000] "GET /wewnetrzne/ HTTP/1.1" 200 301
web-1  | 172.18.0.1 - - [04/Nov/2026:11:27:41 +0000] "GET /wewnetrzne/plan.txt HTTP/1.1" 200 58
web-1  | [Wed Nov 04 11:44:53.579610 2026] [mpm_event:notice] [pid 1:tid 1] AH00492: caught SIGWINCH, shutting down gracefully
web-1  | [Wed Nov 04 11:44:54.751914 2026] [mpm_event:notice] [pid 1:tid 1] AH00489: Apache/2.4.69 (Unix) configured -- resuming normal operations
web-1  | [Wed Nov 04 11:44:54.751928 2026] [core:notice] [pid 1:tid 1] AH00094: Command line: 'httpd -D FOREGROUND'
web-1  | [Wed Nov 04 11:46:04.496306 2026] [autoindex:error] [pid 9:tid 13] [client 172.18.0.1:59932] AH01276: Cannot serve directory /usr/local/apache2/htdocs/materialy/: No matching DirectoryIndex (index.html) found, and server-generated directory index forbidden by Options directive
web-1  | 172.18.0.1 - - [04/Nov/2026:11:46:04 +0000] "GET /materialy/ HTTP/1.1" 403 239
web-1  | 172.18.0.1 - - [04/Nov/2026:11:46:30 +0000] "GET /materialy/notatka.txt HTTP/1.1" 200 69
web-1  | [Wed Nov 04 11:47:02.751090 2026] [authz_core:error] [pid 10:tid 21] [client 172.18.0.1:58142] AH01630: client denied by server configuration: /usr/local/apache2/htdocs/wewnetrzne/
web-1  | 172.18.0.1 - - [04/Nov/2026:11:47:02 +0000] "GET /wewnetrzne/ HTTP/1.1" 403 239
web-1  | [Wed Nov 04 11:47:17.599491 2026] [authz_core:error] [pid 11:tid 28] [client 172.18.0.1:61128] AH01630: client denied by server configuration: /usr/local/apache2/htdocs/wewnetrzne/plan.txt
web-1  | 172.18.0.1 - - [04/Nov/2026:11:47:17 +0000] "GET /wewnetrzne/plan.txt HTTP/1.1" 403 239
kinia@kawk2 pliki-dla-studentow %
```

## Zadanie 2

### Tworzenie konta student z hasłem ćwiczeniowym
```text
kinia@kawk2 pliki-dla-studentow % docker compose run --rm --no-deps narzedzia -cB /auth/uzytkownicy student
Container pliki-dla-studentow-narzedzia-run-f9230163d3bd Creating
Container pliki-dla-studentow-narzedzia-run-f9230163d3bd Created
New password:
Re-type new password:
Adding password for user student
kinia@kawk2 pliki-dla-studentow %
```

### Dodane reguły
```text
<Directory "/usr/local/apache2/htdocs/panel">
    AuthType Basic
    AuthName "Laboratorium 5"
    AuthUserFile "/auth/uzytkownicy"
    Require valid-user
</Directory>
```

### Sprawdzenie syntax i restart
```text
kinia@kawk2 pliki-dla-studentow % docker compose exec web httpd -t
Syntax OK
kinia@kawk2 pliki-dla-studentow % docker compose restart web
[+] restart 0/1
 ⠙ Container pliki-dla-studentow-web-1 Restarting                                                                                                                                              1.2s
kinia@kawk2 pliki-dla-studentow %
```

### Testy
```text
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/panel/raport.txt
HTTP/1.1 401 Unauthorized
Date: Wed, 04 Nov 2026 12:06:41 GMT
Server: Apache
WWW-Authenticate: Basic realm="Laboratorium 5"
Content-Length: 421
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
</body></html>
kinia@kawk2 pliki-dla-studentow % curl -i -u student:zlehaslo http://127.0.0.1:8080/panel/raport.txt
HTTP/1.1 401 Unauthorized
Date: Wed, 04 Nov 2026 12:06:56 GMT
Server: Apache
WWW-Authenticate: Basic realm="Laboratorium 5"
Content-Length: 421
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
</body></html>
kinia@kawk2 pliki-dla-studentow % curl -i -u student http://127.0.0.1:8080/panel/raport.txt
Enter host password for user 'student':
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 12:07:11 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 06:04:00 GMT
ETag: "3a-65f6d252c5400"
Accept-Ranges: bytes
Content-Length: 58
Content-Type: text/plain; charset=UTF-8

Raport cwiczeniowy: dostep po poprawnym uwierzytelnieniu.
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 12:07:22 GMT
Server: Apache
Last-Modified: Wed, 04 Nov 2026 06:04:00 GMT
ETag: "15f-65f6d252c5400"
Accept-Ranges: bytes
Content-Length: 351
Content-Type: text/html; charset=UTF-8

<!doctype html>
<html lang="pl"><meta charset="utf-8"><title>Laboratorium 5</title>
<h1>Laboratorium 5: serwer WWW działa</h1>
<p>Materiały ćwiczeniowe do konfiguracji dostępu w Apache.</p>
<ul><li><a href="/materialy/">Materiały</a></li>
<li><a href="/wewnetrzne/">Wewnętrzne</a></li>
<li><a href="/panel/raport.txt">Panel</a></li></ul></html>
kinia@kawk2 pliki-dla-studentow %
```

## Zadanie 3
### Przed dopisaniem reguł
```text
kinia@kawk2 pliki-dla-studentow % docker compose up -d --build web
[+] Building 1.6s (14/14) FINISHED
 => [internal] load local bake definitions                                                                                                                                                    0.0s
 => => reading from stdin 595B                                                                                                                                                                0.0s
 => [internal] load build definition from Dockerfile                                                                                                                                          0.0s
 => => transferring dockerfile: 473B                                                                                                                                                          0.0s
 => [internal] load metadata for docker.io/library/httpd:2.4-alpine                                                                                                                           1.3s
 => [internal] load .dockerignore                                                                                                                                                             0.0s
 => => transferring context: 67B                                                                                                                                                              0.0s
 => [1/7] FROM docker.io/library/httpd:2.4-alpine@sha256:070da7661f0be8a05430b2c125c0cde9e53176b4048c813024021969a0e3893c                                                                     0.0s
 => => resolve docker.io/library/httpd:2.4-alpine@sha256:070da7661f0be8a05430b2c125c0cde9e53176b4048c813024021969a0e3893c                                                                     0.0s
 => [internal] load build context                                                                                                                                                             0.0s
 => => transferring context: 917B                                                                                                                                                             0.0s
 => CACHED [2/7] RUN apk add --no-cache python3                                                                                                                                               0.0s
 => CACHED [3/7] COPY httpd.conf /usr/local/apache2/conf/httpd.conf                                                                                                                           0.0s
 => CACHED [4/7] COPY www/ /usr/local/apache2/htdocs/                                                                                                                                         0.0s
 => CACHED [5/7] COPY dane/ /lab-data/                                                                                                                                                        0.0s
 => [6/7] COPY cgi-bin/ /usr/local/apache2/cgi-bin/                                                                                                                                           0.0s
 => [7/7] RUN chown -R root:daemon /lab-data     && chmod 755 /lab-data     && chmod 640 /lab-data/ogolny.txt     && chmod 600 /lab-data/poufny.txt     && find /usr/local/apache2/cgi-bin -  0.1s
 => exporting to image                                                                                                                                                                        0.1s
 => => exporting layers                                                                                                                                                                       0.0s
 => => exporting manifest sha256:b587d703c0730e9a0ddae873fc7d16551cdbbefaf933ec892fc7156cf1a46cb3                                                                                             0.0s
 => => exporting config sha256:49357d20e46317e31f7d2b32302aa12b9f35541e01a9642e067b00a0412bfd2e                                                                                               0.0s
 => => exporting attestation manifest sha256:95dd1ee2a303e94b11002d6f0214ce7c3bfcce259ebeb01cf2a4a52d929edd84                                                                                 0.0s
 => => exporting manifest list sha256:8beb6f81aa0af794fff2d3d6e1dc96f28fea167c0f2dde0d1b536c1b713a64b9                                                                                        0.0s
 => => naming to docker.io/library/ochrona-danych-lab05:local                                                                                                                                 0.0s
 => => unpacking to docker.io/library/ochrona-danych-lab05:local                                                                                                                              0.0s
 => resolving provenance for metadata file                                                                                                                                                    0.0s
[+] up 2/2
 ✔ Image ochrona-danych-lab05:local    Built                                                                                                                                                   1.6s
 ✔ Container pliki-dla-studentow-web-1 Started                                                                                                                                                 1.2s
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/cgi-bin/uprawnienia.cgi
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 12:19:46 GMT
Server: Apache
Transfer-Encoding: chunked
Content-Type: text/plain; charset=utf-8

Efektywny UID: 2
Efektywny GID: 2
REMOTE_USER: -

/lab-data/ogolny.txt: LAB05: dokument dostepny dla grupy procesu WWW.
/lab-data/poufny.txt: odmowa odczytu (brak uprawnien)
kinia@kawk2 pliki-dla-studentow % docker compose exec web ls -ln /lab-data/
total 8
-rw-r-----    1 0        2               48 Nov  4 06:04 ogolny.txt
-rw-------    1 0        2               61 Nov  4 06:04 poufny.txt
kinia@kawk2 pliki-dla-studentow %
```
### Dopisane reguły
```text
<Directory "/usr/local/apache2/cgi-bin">
    AuthType Basic
    AuthName "Laboratorium 5"
    AuthUserFile "/auth/uzytkownicy"
    Require valid-user
</Directory>
```
### Po dopisaniu reguł
```text
kinia@kawk2 pliki-dla-studentow % docker compose exec web httpd -t
Syntax OK
kinia@kawk2 pliki-dla-studentow % docker compose restart web
[+] restart 0/1
 ⠙ Container pliki-dla-studentow-web-1 Restarting
kinia@kawk2 pliki-dla-studentow % curl -i http://127.0.0.1:8080/cgi-bin/uprawnienia.cgi
HTTP/1.1 401 Unauthorized
Date: Wed, 04 Nov 2026 12:24:13 GMT
Server: Apache
WWW-Authenticate: Basic realm="Laboratorium 5"
Content-Length: 421
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
</body></html>
kinia@kawk2 pliki-dla-studentow % curl -i -u student http://127.0.0.1:8080/cgi-bin/uprawnienia.cgi
Enter host password for user 'student':
HTTP/1.1 200 OK
Date: Wed, 04 Nov 2026 12:24:43 GMT
Server: Apache
Transfer-Encoding: chunked
Content-Type: text/plain; charset=utf-8

Efektywny UID: 2
Efektywny GID: 2
REMOTE_USER: student

/lab-data/ogolny.txt: LAB05: dokument dostepny dla grupy procesu WWW.
/lab-data/poufny.txt: odmowa odczytu (brak uprawnien)
kinia@kawk2 pliki-dla-studentow %
```