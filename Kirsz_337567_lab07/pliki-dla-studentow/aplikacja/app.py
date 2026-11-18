"""Sejf sekretow i kalkulator - celowo podatna aplikacja do laboratorium 7.

Uruchamiaj wylacznie lokalnie, w kontenerze z pakietu. Dane sa fikcyjne.
"""
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)
BAZA = "file:/dane/sekrety.db?mode=ro"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sekret")
def sekret():
    klucz = request.args.get("klucz", "")
    zapytanie = "SELECT wlasciciel, sekret FROM sekrety WHERE klucz = ?"
    wiersze, blad = [], None
    try:
        with sqlite3.connect(BAZA, uri=True) as db:
            wiersze = db.execute(zapytanie, (klucz,)).fetchall()
    except sqlite3.Error:
        app.logger.exception("Blad zapytania SQL")
        blad = "Nieprawidlowe dane"
    return render_template("sekret.html", klucz=klucz, zapytanie=zapytanie, wiersze=wiersze, blad=blad)

import re
WZORZEC = re.compile(r'\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*')

def policz(wyrazenie: str):
    if len(wyrazenie) > 100:
        raise ValueError("za dlugie wejscie")
    m = re.fullmatch(WZORZEC, wyrazenie)   # fullmatch = caly napis musi pasowac
    if not m:
        raise ValueError("niedozwolone wejscie")
    a = float(m.group(1))
    op = m.group(2)
    b = float(m.group(3))
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if b == 0:
        raise ZeroDivisionError
    return a / b

@app.route("/kalkulator")
def kalkulator():
    wyrazenie = request.args.get("wyrazenie")
    if wyrazenie is None:
        return render_template("kalkulator.html", wyrazenie="", wynik=None)
    try:
        wynik = policz(wyrazenie)
    except ZeroDivisionError:
        return "Dzielenie przez zero", 400
    except Exception:
        app.logger.exception("kalkulator")
        return "Nieprawidlowe dane", 400
    return render_template("kalkulator.html", wyrazenie=wyrazenie, wynik=wynik)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
