import random
import time

try:
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    colorama_installed = True
except ImportError:
    colorama_installed = False

def choose_slepenais_vards():
    vardi = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'blueberry', 'watermelon']
    return random.choice(vardi)

def check_minejums(slepenais_vards, minejums):
    pareizas_pozicijas = sum(a == b for a, b in zip(slepenais_vards, minejums))
    pareizi_burti = sum(min(slepenais_vards.count(letter), minejums.count(letter)) for letter in set(minejums))
    return pareizas_pozicijas, pareizi_burti - pareizas_pozicijas

def main():
    if not colorama_installed:
        print("Lai šī programma darbotos pareizi, jums jāielādē colorama. To varat ielādēt, izmantojot komandu 'pip install colorama' (bez pēdiņām).")
        return

    print(Back.LIGHTBLUE_EX + Fore.BLACK + "Sveiki! Esam izvēlējušies slepeno vārdu. Mēģiniet to uzminēt!" + Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "Ja vēlaties spēli pārtraukt, rakstiet 'beigt'!" + Style.RESET_ALL)
    print(Back.LIGHTMAGENTA_EX + Fore.BLACK + "Iespējamie vārdi: apple, banana, orange, grape, pineapple, strawberry, blueberry, watermelon." + Style.RESET_ALL)
    
    slepenais_vards = choose_slepenais_vards()
    meginajums = 0
    iespejamie_vardi = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'blueberry', 'watermelon']
    laika_limits = 30  # Laika ierobežojums sekundēs
    time.sleep(5)
    print(Fore.GREEN + "Spēle sākas!" + Style.RESET_ALL)
    start_laiks = time.time()

    while True:
        minejums = input("Ievadiet savu minējumu: ").lower()

        if minejums == 'beigt':
            print(Fore.RED + "⛔ Spēle pārtraukta⛔" + Style.RESET_ALL)
            break

        if not minejums.isalpha():
            print(Fore.YELLOW + "❗Lūdzu, ievadiet tikai burtus vai izmantojiet 'beigt', lai pārtrauktu spēli.❗" + Style.RESET_ALL)
            continue

        if minejums not in iespejamie_vardi:
            print("🤔 Šāds vārds nepastāv.")
            elapsed_time = time.time() - start_laiks
            atlikusais_laiks = laika_limits - elapsed_time
            if atlikusais_laiks <= 0:
                print("⏰ " + Back.RED + "Laiks beidzies! Spēle pārtraukta." + Style.RESET_ALL)
                break
            else:
                print("🕑 Atlikušais laiks:", int(atlikusais_laiks), "sekundes🕑")
            continue

        meginajums += 1
        pareizas_pozicijas, pareizi_burti = check_minejums(slepenais_vards, minejums)

        print("✅ Pareizi uzminētie burti un to pozīcijas:", pareizas_pozicijas)
        print("✅ Pareizi uzminētie burti, bet ❌ nepareizās pozīcijās:", pareizi_burti)

        if pareizas_pozicijas == len(slepenais_vards):
            print(Fore.MAGENTA + "🏆 Apsveicam! Jūs uzminējāt vārdu ar", meginajums, "mēģinājumiem!🏆" + Style.RESET_ALL)
            break

        elapsed_time = time.time() - start_laiks
        atlikusais_laiks = laika_limits - elapsed_time
        if atlikusais_laiks <= 0:
            print("⏰ Laiks beidzies! Spēle pārtraukta.")
            break
        else:
            print("🕑 Atlikušais laiks:", int(atlikusais_laiks), "sekundes🕑")

if __name__ == "__main__":
    main()