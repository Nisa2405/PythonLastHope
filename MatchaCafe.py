from menu import matchakarte, kaffeekarte

def karte_zeigen(menu):
    karte=[]
    for getraenk,preis in menu.items():
        karte.append(f"- {getraenk}: {preis:.2f}")
    return "\n".join(karte)
    
while True: 
    willkommen= input("Willkommen in Nisas Matcha Cafe, was möchten Sie bestellen?\n    Matcha oder Kaffee?\n").strip().lower()
    if willkommen == "matcha": 
        print("Klaro, hier ist die Matchakarte: ")
        print(karte_zeigen(matchakarte))

        bestellung=input("Hast du dich schon entschieden? Oder möchtest du doch lieber die Kaffeekarte sehen?\n    Nein, ich möchte einen ...\n    Ja, Kaffeekarte bitte.\n").strip().lower()
    
        if bestellung == "Ja bitte":
            print(karte_zeigen(kaffeekarte))
        else: 
            #Aus dem Dictionary 
            print("Feature lädt noch...")
        
            
    elif willkommen == "kaffee":
        print("Klaro, hier ist die Kaffeekarte: ")
        print(karte_zeigen(kaffeekarte))

    else: 
        print("Btte beachte die zwei Antwortmöglichkeiten. Möchtest du wirklich keinen Kaffee oder einen Matcha????????????")
    if input("").strip().lower() == "nein":
        break
