
import random



poledogry = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]



def tablica():
    global lista
    lista = print("\n", poledogry[0], poledogry[1], poledogry[2], "\n",
                  poledogry[3], poledogry[4], poledogry[5], "\n",
                  poledogry[6], poledogry[7], poledogry[8])


def wprowadzkol():
    global gracz
    global gra
    gra = 1

    if (gra == 1):
        wygralkrzyzyk()
        remis()
        global ruchkolka
        ruchkolka = int(input("Podaj pole w, które wprowadzić kółko"))
        kolko()
    if (gra == 0):
        print("Koniec gry")


def wprowadzkrz():
    wygralokolko()
    remis()
    if (gra == 1):
        global ruchkrzyzyk
        # dla dwóch graczy
        #ruchkrzyzyk = int(input("Podaj pole w, które wprowadzić krzyżyk"))
        #dla komputera

        ruchkrzyzyk = random.randint(0,8)
        krzyzyk()
    if (gra == 0):
        print("Koniec gry")


def kolko():
    if (poledogry[ruchkolka] == '[o]' or poledogry[ruchkolka] == '[x]'):
        print("To pole jest zajęte wybierz inne")
        wprowadzkol()
    elif (ruchkolka < 10 and ruchkolka >= 0 and gra != 0):
        poledogry[ruchkolka] = '[o]'
        tablica()
        wprowadzkrz()
    else:
        print("wprowadź poprawne pole")
        wprowadzkol()


def krzyzyk():
    if (poledogry[ruchkrzyzyk] == '[o]' or poledogry[ruchkrzyzyk] == '[x]'):
        #dla 2 graczy
        #print("To pole jest zajęte wybierz inne")
        wprowadzkrz()
    elif (ruchkrzyzyk < 10 and ruchkrzyzyk >= 0 and gra != 0):
        poledogry[ruchkrzyzyk] = '[x]'
        tablica()
        wprowadzkol()
    else:
        print("wprowadź poprawne pole")
        wprowadzkrz()


def wygralokolko():
    if (poledogry[0] == '[o]' and poledogry[1] == '[o]' and poledogry[2] == '[o]'
            or poledogry[3] == '[o]' and poledogry[4] == '[o]' and poledogry[5] == '[o]' or
            poledogry[6] == '[o]' and poledogry[7] == '[o]' and poledogry[8] == '[o]' or
            poledogry[0] == '[o]' and poledogry[3] == '[o]' and poledogry[6] == '[o]' or
            poledogry[1] == '[o]' and poledogry[4] == '[o]' and poledogry[7] == '[o]' or
            poledogry[2] == '[o]' and poledogry[5] == '[o]' and poledogry[8] == '[o]' or
            poledogry[2] == '[o]' and poledogry[4] == '[o]' and poledogry[6] == '[o]' or
            poledogry[0] == '[o]' and poledogry[4] == '[o]' and poledogry[8] == '[o]'):
        print("Wygrało kółko")
        exit()


def wygralkrzyzyk():
    if (poledogry[0] == '[x]' and poledogry[1] == '[x]' and poledogry[2] == '[x]'
            or poledogry[3] == '[x]' and poledogry[4] == '[x]' and poledogry[5] == '[x]' or
            poledogry[6] == '[x]' and poledogry[7] == '[x]' and poledogry[8] == '[x]' or
            poledogry[0] == '[x]' and poledogry[3] == '[x]' and poledogry[6] == '[x]' or
            poledogry[1] == '[x]' and poledogry[4] == '[x]' and poledogry[7] == '[x]' or
            poledogry[2] == '[x]' and poledogry[5] == '[x]' and poledogry[8] == '[x]' or
            poledogry[2] == '[x]' and poledogry[4] == '[x]' and poledogry[6] == '[x]' or
            poledogry[0] == '[x]' and poledogry[4] == '[x]' and poledogry[8] == '[x]'):
        print("Wygrał krzyzyk")
        exit()


def remis():
    if(poledogry[0] != '[ ]' and poledogry[1] != '[ ]' and poledogry[2] != '[ ]' and poledogry[3] != '[ ]' and poledogry[4] != '[ ]' and poledogry[5] != '[ ]'
    and poledogry[6] != '[ ]' and poledogry[7] != '[ ]' and poledogry[8] != '[ ]'):
       print("Remis")
       exit()


tablica()
wprowadzkol()

