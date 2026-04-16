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
        