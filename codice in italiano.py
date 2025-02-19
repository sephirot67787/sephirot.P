import random
 
def MenuClienti():
    print("\nBenvenuto al Radiant Cow Steak House!")
    print("----------------------------------------")
    print("|           MENU PRINCIPALE            |")
    print("----------------------------------------")
    print("|  ANTIPASTI                           |")
    print("| 1. Carpaccio di manzo      €15.00    |")
    print("| 2. Tartare di manzo        €16.00    |")
    print("| 3. Bruschette miste        €8.00     |")
    print("----------------------------------------")
    print("|  PRIMI PIATTI                        |")
    print("| 4. Tagliatelle al ragù     €14.00    |")
    print("| 5. Risotto ai funghi       €13.00    |")
    print("| 6. Gnocchi al gorgonzola  €12.00     |")
    print("----------------------------------------")
    print("|  SECONDI DI CARNE                    |")
    print("| 7. Ribeye Steak (300g)     €28.00    |")
    print("| 8. Filetto (250g)          €32.00    |")
    print("| 9. T-Bone (500g)           €35.00    |")
    print("| 10. Tomahawk (800g)        €45.00    |")
    print("----------------------------------------")
    print("|  CONTORNI                            |")
    print("| 11. Patate arrosto         €5.00     |")
    print("| 12. Verdure grigliate      €6.00     |")
    print("| 13. Insalata mista         €4.00     |")
    print("----------------------------------------")
    print("|  BEVANDE                             |")
    print("| 14. Vino della casa        €18.00    |")
    print("| 15. Birra artigianale      €6.00     |")
    print("| 16. Acqua minerale         €2.50     |")
    print("----------------------------------------")
    print("|  DESSERT                             |")
    print("| 17. Tiramisù               €6.00     |")
    print("| 18. Panna cotta            €5.00     |")
    print("| 19. Cheesecake             €6.00     |")
    print("----------------------------------------")
    print("|  POST CENA                           |")
    print("| -1- caffè                €1.00       |")
    print("| -2- digestivo            €4.00       |")
    print("----------------------------------------")
    print ("")
    conto = 0
    while True:
        try:
            scelta = input("\nInserisci il numero del piatto che desideri ordinare (0 per terminare): ")
            scelta = int(scelta)

            if 1 <= scelta <= 19:
                print(f"Hai selezionato il piatto numero {scelta}")
            else:
                print("Per favore, seleziona un numero valido dal menu (1-19)")

            if scelta == 1:
                conto += 15
            if scelta == 2:
                conto += 16
            if scelta == 3:
                conto += 8
            if scelta == 4:
                conto += 14
            if scelta == 5:
                conto += 13
            if scelta == 6:
                conto += 12
            if scelta == 7:
                conto += 28
            if scelta == 8:
                conto += 32
            if scelta == 9:
                conto += 35
            if scelta == 10:
                conto += 45
            if scelta == 11:
                conto += 5
            if scelta == 12:
                conto += 6
            if scelta == 13:
                conto += 4
            if scelta == 14:
                conto += 18
            if scelta == 15:
                conto += 6
            if scelta == 16:
                conto += 2.50
            if scelta == 17:
                conto += 6
            if scelta == 18:
                conto += 5
            if scelta == 19:
                conto += 6
            if scelta == 0:
                print("Grazie per aver ordinato!")
                for i in range(5):
                    print("")

                luck = random.randint(0, 1)
                print(f"Spero sia stato tutto di tuo gradimento, in ogni caso il conto è di €{conto}")
                print("")
                print("Gradisci il caffè -1- oppure il nostro digestivo -2-? (altro numero no)")
                cafettuccio = input()
                if cafettuccio == "1":
                    print("Ecco a te il caffè")
                    if luck == 0:
                        conto += 1
                        print("")
                        print(f"Incluso il caffè il conto è di €{conto:}")
                    else:
                        print("Il caffè lo offre la casa")
                        print("")
                        print(f"Quindi sono €{conto:}")
                elif cafettuccio == "2":
                    print("Ecco a te il digestivo")
                    if luck == 0:
                        conto += 4
                        print()
                        print(f"Incluso il digestivo il conto è di €{conto}")
                    else:
                        print("Il digestivo lo offre la casa")
                        print("")

                break
        except ValueError:
            print("Per favore, inserisci un numero valido.")

def tavoli():
    return random.randint(1, 21)


   
def selruolo():
    print("Benvenuto nel programma, inserire modalità 1 - 'Cliente' oppure 2 - 'Dipendente' oppure 3 - Esci")
    while True:
        choice = input()

        if choice == '1' or '2' or '3':
            return choice
        else: 
           
            print("Scelta non valida. Per favore, inserire un opzione valida. . .")
    
def codice():
    cod = random.randint(1000000, 99999999)

def main():
    
    
    while True:
        
        n = selruolo()

        if n == '1':
            numero = tavoli()
            print("Benvenuto cliente alla Radiant Cow Steak House")
            print("")
            print(f"Accomodati pure al tavolo {numero}")
            print("Bene, ed ora ecco a te il menù! Scegli pure con calma.")
            MenuClienti()

        if n == '2':
            while True:
                print("Ciao! Ti ho già visto da qualche parte? (1 - Si, 2 - No)")
                lOrR = input()

                if lOrR == "2":
                    print("Ah, ecco! Mi pareva di non averti mai visto in giro... sei nuovo? Come ti chiami?")
                    nome = input()
                    print(f"{nome}, eh? Bellissimo nome! Quanti anni hai?")
                    età = input()
                    print(f"Quindi hai {età} anni, eh? Te li porti benissimo.")
                    print("")
                    print("Bhe ora ti darò il tuo codice ti chiederei di non perderlo")
                    print("")
                    cod = codice()
                    print(f"Ecco il tuo codice {cod}")

                if lOrR == "1":
                    print("Inserisci il tuo codice così posso essere sicuro di conoscerti.")
                    while True:
                        insCode = input()
                        if insCode == str(cod):
                          print(f"Ah si ora mi ricordo di te sei {nome} e hai {età} anni")
                          oreLavoro = random.randint(1,9) 
                          ora = random.randint(0,23)
                          minuti = random.randint(0,59)
                          orarioInizio = ora,minuti
                          oraFinale = ora + oreLavoro
                          orarioFine = oraFinale,minuti
                          print(f"Il tuo turno è di {oreLavoro} ore di lavoto quindi dalle {orarioInizio} alle {orarioFine}")
                          break
                        else:
                            print("Codice non valido, riprova.")

        if n == "3":
            print("Buona giornata !")
            break
       

if __name__ == "__main__":
    main()
