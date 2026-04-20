import random
import json

def ladda_highscore(filnamn="highscore.json"):
    try:
        with open(filnamn, "r", encoding="utf-8") as fil:
            return json.load(fil)
    except FileNotFoundError:
        return []

def spara_highscore(highscore_lista, filnamn="highscore.json"):
    with open(filnamn, "w", encoding="utf-8") as fil:
        json.dump(highscore_lista, fil, indent=4, ensure_ascii=False)

def spela_omgang():
    hemligt_tal = random.randint(1, 100)
    antal = 0
    
    while True:
        gissa = int(input("Gissa ett tal mellan 1 och 100: "))
        antal += 1
        
        if gissa < hemligt_tal:
            print("För lågt!")
        elif gissa > hemligt_tal:
            print("För högt!")
        else:
            print(f"Rätt! Du gissade på {antal} gissningar!")
            return antal
        
def visa_highscore(highscore_lista):
    if len(highscore_lista) == 0:
        print("Inga resultat ännu!")
    else: 
        print("\n--- HIGHSCORE ---")
        sorterad = sorted(highscore_lista, key=lambda x: x["gissningar"])
        for index, spelare in enumerate(sorterad):
            print(f"{index + 1}. {spelare['namn']} - {spelare['gissningar']} gissningar")
def huvudprogram():
    highscore_lista = ladda_highscore()
    
    while True:
        print("\n--- HÖGT / LÅGT ---")
        print("1. Starta spel")
        print("2. Visa highscore")
        print("3. Avsluta")
        
        val = input("\nVälj: ")
        
        if val == "1":
            antal = spela_omgang()
            namn = input("Skriv ditt namn: ")
            spelare = {"namn": namn, "gissningar": antal}
            highscore_lista.append(spelare)
            spara_highscore(highscore_lista)
            print(f"Bra jobbat {namn}! Resultatet sparat!")
        elif val == "2":
            visa_highscore(highscore_lista)
        elif val == "3":
            print("Hejdå!")
            break
        else:
            print("Ogiltigt val, försök igen!")

if __name__ == "__main__":
    huvudprogram()