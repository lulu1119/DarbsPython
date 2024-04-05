import random
import time

try:
    import colorama  # Mēģina importēt colorama moduli
    from colorama import Fore, Back, Style # Importē dažas no colorama funkcijām
    colorama.init() # Inicializē colorama, lai nodrošinātu krāsu atbalstu terminālī
    colorama_installed = True # Uzstāda mainīgo, kas norāda, ka colorama ir veiksmīgi instalēts
except ImportError:
    # Ja importēt colorama moduli neizdodas (piemēram, ja modulis nav instalēts), tad:
    colorama_installed = False # Uzstāda mainīgo, kas norāda, ka colorama nav pieejams

# Funkcija, kas izvēlas gadījuma slepeno vārdu no saraksta
def choose_slepenais_vards():
    vardi = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'blueberry', 'watermelon']
    return random.choice(vardi)

# Funkcija, kas pārbauda minējumu pret slepeno vārdu un atgriež pareizo burtu skaitu un to pozīcijas
def check_minejums(slepenais_vards, minejums):
    pareizas_pozicijas = sum(a == b for a, b in zip(slepenais_vards, minejums))
    pareizi_burti = sum(min(slepenais_vards.count(letter), minejums.count(letter)) for letter in set(minejums))
    return pareizas_pozicijas, pareizi_burti - pareizas_pozicijas

# Galvenā funkcija
def main():
    # Pārbauda, vai colorama ir instalēts
    if not colorama_installed:
        print("❗Lai šī spēle darbotos, jums jāaugšupielādē colorama. To varat izdarīt, ievadot terminālī 'pip install colorama' (bez pēdiņām) un nospiežot ENTER.")
        return

    # Sākuma ziņojums
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "Sveiki! Esam izvēlējušies slepeno vārdu. Mēģiniet to uzminēt!" + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "Ja vēlaties spēli pārtraukt, rakstiet 'beigt'!" + Style.RESET_ALL)
    print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "Iespējamie vārdi: apple, banana, orange, grape, pineapple, strawberry, blueberry, watermelon." + Style.RESET_ALL)
    
    # Izvēlas slepeno vārdu
    slepenais_vards = choose_slepenais_vards()
    meginajums = 0
    iespejamie_vardi = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'blueberry', 'watermelon']
    laika_limits = 30  # Laika ierobežojums sekundēs
    time.sleep(5) #uzgaida 5 sekundes pirms sākuma
    print(Fore.GREEN + "Spēle sākas!" + Style.RESET_ALL)
    start_laiks = time.time() # Sākuma laiks

    while True:
        minejums = input("Ievadiet savu minējumu: ").lower()

        # Ja minējums ir 'beigt', pārtrauc spēli
        if minejums == 'beigt':
            print(Fore.RED + "⛔ Spēle pārtraukta⛔" + Style.RESET_ALL)
            break

        if not minejums.isalpha():  # ja minējums nav burti, programma izvada tekstu ar lūgumu ievadīt burtus
            print(Fore.YELLOW + "❗Lūdzu, ievadiet tikai burtus vai izmantojiet 'beigt', lai pārtrauktu spēli.❗" + Style.RESET_ALL)
            continue

        # Pārbauda, vai minējums ir iespējamais vārds
        if minejums not in iespejamie_vardi:
            print("🤔 Šāds vārds nepastāv.")
            elapsed_time = time.time() - start_laiks # Pagājušais laiks
            atlikusais_laiks = laika_limits - elapsed_time #aprēķina atlikušo laiku spēlē, ņemot vērā laika ierobežojumu un pagājušo laiku kopš spēles sākuma.
            if atlikusais_laiks <= 0:
                print("⏰ " + Back.RED + "Laiks beidzies! Spēle pārtraukta." + Style.RESET_ALL)
                break
            else:
                print("🕑 Atlikušais laiks:", int(atlikusais_laiks), "sekundes🕑")
            continue

        # Palielina minējumu skaitu un pārbauda minējumu
        meginajums += 1
        pareizas_pozicijas, pareizi_burti = check_minejums(slepenais_vards, minejums)

        # Izvada rezultātu
        print("✅ Pareizi uzminētie burti un to pozīcijas:", pareizas_pozicijas)
        print("✅ Pareizi uzminētie burti, bet ❌ nepareizās pozīcijās:", pareizi_burti)

        # Ja ir uzminēts vārds, apsveic
        if pareizas_pozicijas == len(slepenais_vards):
            print(Fore.MAGENTA + "🏆 Apsveicam! Jūs uzminējāt vārdu ar", meginajums, "mēģinājumiem/-mu!🏆" + Style.RESET_ALL)
            break

        #Laiks
        elapsed_time = time.time() - start_laiks # Pagājušais laiks
        atlikusais_laiks = laika_limits - elapsed_time # Atlikušais laiks
        if atlikusais_laiks <= 0:
            print("⏰ Laiks beidzies! Spēle pārtraukta.")
            break
        else:
            print("🕑 Atlikušais laiks:", int(atlikusais_laiks), "sekundes🕑")

if __name__ == "__main__":
    main() # Šī izpildāmā rinda nodrošina, ka galvenā funkcija `main()` tiek izsaukta tikai tad, ja šis skripts tiek palaists tieši (nevis importēts citā skriptā).