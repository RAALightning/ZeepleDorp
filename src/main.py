# Maddox the WizKid & Ronan the Barbarian's awesome game!
# Start Date - 7/7/2025

#imports
from room import Room
from player import Player

def main():
    print("AAAAAAGGGGHHHHHHHH!")
    medbay = Room(1,"Medbay","There's like medical equipment and stuff")
    shredder = Room(2,"Shredder","This is where failed paitients go to get better")
    medbay.connect(shredder)
    print(shredder.neighbors)
    print(medbay.neighbors)


if __name__ == "__main__":
    main()
