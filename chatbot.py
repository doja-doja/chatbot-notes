#!//usr/bin/env python3
# -*- oding: utf-8 -*-

# auf allen Systemen wird die passende Environment für Python 3
# automat. gewählt

# Ein einfacher ChatBot
# (c) 2020 by me, Lizenz GPLv3

import random

# zufällige Antworten
zufallsantworten = ["Oh wirklich...", "Interessant", "Das kann man so sehen.", "Ich verstehe..."]
# ELIZA: eigtl. in externer Datei speichern und dann in main
# einem initialisierten Array zuweisen

# Stopwörter
reaktionen = {"hallo": "aber hallo",
              "geht": "Was verstehst du darunter",
              "schmeckt": "Ich habe keinen Geschmackssinn"
              }

# Ausgabe Head
print("Willkommen beim ChatBot (v1)")
print("Worüber wollen Sie sprechen?")
print("Zum Beenden geben Sie bye ein....")
print("")

# main
nutzereingabe = ""  # sauberer Stil: Variablentyp initialisieren
while nutzereingabe != "bye":
    nutzereingabe = ""  # Variable säubern: nichts bleibt übrig
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Frage oder Antwort: ")

    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()

    intelligentAntworten = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionen:
            print(reaktionen[einzelwoerter])
            intelligentAntworten = True

    if not intelligentAntworten:
        print(random.choice(zufallsantworten))  # Nachteil an Laufvariable (zufallsantworten[i] (mit i = random.randint(1,4) )): ist auf Länge der zufallsanworten angewiesen
print("Einen schönen Tag.")
