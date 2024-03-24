import random
import time

def choose_secret_word():
    #Funkcija, lai izvēlētos gadījuma vārdu no saraksta.
    words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'blueberry', 'watermelon']
    return random.choice(words)

def check_guess(secret_word, guess):
    #Funkcija, lai pārbaudītu lietotāja minējumu pret slepeno vārdu.
    correct_positions = sum(a == b for a, b in zip(secret_word, guess))
    correct_letters = sum(min(secret_word.count(letter), guess.count(letter)) for letter in set(guess))
    return correct_positions, correct_letters - correct_positions

def main():
    print("Sveiki! Esam izvēlējušies slepeno vārdu. Mēģiniet to uzminēt!")
    print("Ja vēlaties spēli pārtraukt, rakstiet 'beigt'!")
    print("Iespējamie vārdi: apple, banana, orange, grape, pineapple, strawberry, blueberry, watermelon")
    secret_word = choose_secret_word()
    attempts = 0
    possible_words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'blueberry', 'watermelon']
    time_limit = 30  # Laika ierobežojums sekundēs
    start_time = time.time()
    
    while True:
        guess = input("Ievadiet savu minējumu: ").lower()
        
        if guess == 'beigt':
            print("Spēle pārtraukta.")
            break
        
        if not guess.isalpha():
            print("❗Lūdzu, ievadiet tikai burtus vai izmantojiet 'beigt', lai pārtrauktu spēli.❗")
            continue

        if guess not in possible_words:
            print("🤔 Šāds vārds nepastāv.")
            continue
        
        attempts += 1
        correct_positions, correct_letters = check_guess(secret_word, guess)
        
        print("Pareizi uzminētie burti un to pozīcijas:", correct_positions)
        print("Pareizi uzminētie burti, bet nepareizās pozīcijās:", correct_letters)
        
        if correct_positions == len(secret_word):
            print("🏆 Apsveicam! Jūs uzminējāt vārdu ar", attempts, "mēģinājumiem!🏆")
            break
        
        elapsed_time = time.time() - start_time
        remaining_time = time_limit - elapsed_time
        if remaining_time <= 0:
            print("Laiks beidzies! Spēle pārtraukta.")
            break
        else:
            print("🕑 Atlikušais laiks:", int(remaining_time), "sekundes🕑")

if __name__ == "__main__":
    main()