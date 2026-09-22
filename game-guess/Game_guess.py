import random

def play_game():
    #pesan selamat datang
    print("Welcome to the Game Number Guess By YANKI !")
    print("I'm thinking of a number between 1 and 100. sooooooo what i should choose.")

    #pemilihan levelnya
    print("\nPlease select a difficulty level stup*d: ")
    print("1. Noob (10 chances)")
    print("2. Normal (5 chances)")
    print("3. Expert (3 chances)")

    while True:
        choice = input("Enter your choice sh*t:")
        if choice == "1":
            chances = 10
            level = "Noob"
            break
        elif choice == "2":
            chances = 5
            level = "Normal"
            break
        elif choice == "3":
            chances = 3
            level = "Expert"
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    print(f"\nGreat! You have selected the {level} difficulty level.")
    print(f"You have {chances} chances to guess the correct number.")
    print("Let's start the fuck*ng game brooo")

    #computer memilih salah satu angka dari 1-100
    secret_number = random.randint(1, 100)
    attempts = 0

    #game loop
    while attempts < chances:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Congatulation you guessed the correct number in {attempts} attempt.")
            return attempts
        elif guess > secret_number:
            print(f"Incorrect! the number is less than {guess}.")
        else:
            print(f"Incorrect! the number is greater tham {guess}.")

        remaining = chances - attempts
        if remaining > 0:
            print(f"You have {remaining} attempts left.") 
    #chances habis
    print(f"\nGame over! the correct number was {secret_number} you stupid piece a sh*t.") 
    return None
#jalankan game nya
play_game()       
