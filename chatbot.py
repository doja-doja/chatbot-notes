#!//usr/bin/env python3
# -*- oding: utf-8 -*-

# auf allen Systemen wird die passende Environment für Python 3
# automat. gewählt

# Ein einfacher ChatBot
# (c) 2020 by me, Lizenz GPLv3

print("Willkommen beim ChatBot (v1)")
print("Worüber wollen Sie sprechen?")
print("Zum Beenden geben Sie bye ein....")
print("")

nutzereingabe = ""  # sauberer Stil: Variablentyp initialisieren
while nutzereingabe != "bye":
    nutzereingabe = ""  # Variable säubern: nichts bleibt übrig
    nutzereingabe = input("Ihre Frage oder Antwort: ")
    print(nutzereingabe)
print("Einen schönen Tag.")

