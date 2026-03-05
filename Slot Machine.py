# Voglio creare una slot machine consolo tre rulli. Questi rulli saranno formati da:
# [Uva, Arancia, Limone, BAR, 7].
# Il giocatore, una volta inserita la moneta, potrà giocare.
# Se vince otterrà 10 monete, se perde non otterrà nulla.
# Se escono tre simboli uguali, il giocatore vince.

import random as rm

def slot():
    moneta = 1
    print(f"Benvenuto straniero. Inizi con una moneta. Vuoi giocare (sì/no)")
    risposta = str(input().lower())
    if risposta == "sì":
        lista = ["Uva", "Arancia", "Limone", "BAR", "7"]
        rullo1 = rm.choice(lista)
        rullo2 = rm.choice(lista)
        rullo3 = rm.choice(lista)
        if rullo1 == rullo2 == rullo3:
            print(f"Hai vinto! I rulli hanno mostrato: {rullo1}, {rullo2} e {rullo3}. Hai guadagnato 10 monete.")
            moneta = moneta + 10
        else:
            print(f"Hai perso! I rulli hanno mostrato: {rullo1}, {rullo2} e {rullo3}.")
            moneta = 0
        print(f"Ti rimangono {moneta} monete.")
        if moneta == 0:
            print("Non hai più monete e non puoi più giocare.")
    else:
        print("Va bene, alla prossima!")