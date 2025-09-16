import random

def russian_roulette():
    chambers = [0, 0, 0, 0, 0, 1]
    random.shuffle(chambers)
    for i in range(6):
        input("Press Enter to pull the trigger...")
        if chambers[i] == 1:
            print("Bang! You're dead.")
            return
        else:
            print("Click! You're safe.")
    print("You survived Russian Roulette!")

russian_roulette()