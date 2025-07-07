# Maddox the WizKid & Ronan the Barbarian's awesome game!
# Start Date - 7/7/2025

#imports
from room import Room
from player import Player
from actor import Actor

def main():

    # Declare initial rooms
    roomInfo = [
        [0, "Bridge", ""]
        [1, "North Hallway", ""]
        [2, "South Hallway", ""]
        [3, "Cryobay", ""]
        [4, "Mess Hall", ""]
        [5, "Medbay", ""]
        [6, "North Engine", ""]
        [7, "South Engine", ""]
        [8, "Electrical Room", ""]
        [9, "Laboratory", ""]
        [10, "Dormitory", ""]
        [11, "Security Office", ""]
        [12, "Cargo Hold", ""]
    ]

    
    for room_id, name, description in roomInfo:
        room = Room(room_id, name, description)
        rooms[name] = room


if __name__ == "__main__":
    main()
