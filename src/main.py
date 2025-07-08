# Maddox the WizKid & Ronan the Barbarian's awesome game!
# Start Date - 7/7/2025

#imports
from room import Room
from player import Player
from actor import Actor

def main():

    # Declare initial rooms and connect them
    rooms = {
        "Bridge" : Room(0,"Bridge","The main control centre of the ship."),
        "NHall" : Room(1,"North Hallway","A long corridor."),
        "SHall" : Room(2,"South Hallway","A long corridor."),
        "Cryo" : Room(3,"Cryobay","Many cryo-sleep pods line the walls."),
        "Medbay" : Room(4,"Medbay",""),
        "Security" : Room(5,"Security Office",""),
        "EngN" : Room(6,"North Engine Room",""),
        "EngS" : Room(7,"South Engine Room",""),
        "Breaker" : Room(8,"Breaker Room",""),
        "Lab" : Room(9,"Laboratory",""),
        "Cargo" : Room(10,"Cargo Hold",""),
        "Dorm" : Room(11,"Dormitory",""),
        "Mess" : Room(12,"Mess Hall",""),
        "Kitchen" : Room(13,"Kitchen",""),
        "Freezer" : Room(14,"Kitchen Freezer",""),
        "Incinerator" : Room(15,"Incinerator",""),
        "Hydroponics" : Room(16,"Hyrdroponics Bay",""),
        "Airlock1" : Room(17,"Airlock 1",""),
        "Airlock2" : Room(18,"Airlock 2",""),
        "Showers" : Room(19,"Shower Room",""),
        "Brig" : Room(20,"The Brig","")
    }
    connect_rooms(rooms)


def connect_rooms(rooms):
    # tells each object to connect to it's  neighbors
    rooms["Bridge"].connect(rooms["Medbay"])
    rooms["Bridge"].connect(rooms["SHall"])
    rooms["Bridge"].connect(rooms["Dorm"])
    rooms["Medbay"].connect(rooms["Cryo"])
    rooms["Medbay"].connect(rooms["NHall"])
    rooms["NHall"].connect(rooms["Security"])
    rooms["NHall"].connect(rooms["Mess"])
    rooms["NHall"].connect(rooms["Breaker"])
    rooms["NHall"].connect(rooms["EngN"])
    rooms["SHall"].connect(rooms["Lab"])
    rooms["SHall"].connect(rooms["Hydroponics"])
    rooms["SHall"].connect(rooms["Airlock1"])
    rooms["SHall"].connect(rooms["Mess"])
    rooms["SHall"].connect(rooms["EngS"])
    rooms["Dorm"].connect(rooms["Showers"])
    rooms["Dorm"].connect(rooms["Mess"])
    rooms["Showers"].connect(rooms["Brig"])
    rooms["Brig"].connect(rooms["Security"])
    rooms["Kitchen"].connect(rooms["Mess"])
    rooms["Kitchen"].connect(rooms["Freezer"])
    rooms["Kitchen"].connect(rooms["Incinerator"])
    rooms["Lab"].connect(rooms["Hydroponics"])
    rooms["EngN"].connect(rooms["Breaker"])
    rooms["Cargo"].connect(rooms["EngN"])
    rooms["Cargo"].connect(rooms["EngS"])
    rooms["Cargo"].connect(rooms["Airlock2"])
    rooms["Cargo"].connect(rooms["Incinerator"])


if __name__ == "__main__":
    main()
