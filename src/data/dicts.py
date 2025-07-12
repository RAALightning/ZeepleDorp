# Define dictionaries
from entities.prop import Prop
from entities.actor import Actor, PlayerCharacter, NPC, Monster
from entities.stage import Stage

ACTOR_DICT = {
    "Test" : Actor("Test", "I am a test")
}

PROP_DICT = {
    "Test" : Prop("Test", "It's a test! It might come in handy later.")
}

STAGE_DICT = {
    "Hallway" = Stage("Hallway","It's long and test-like.")
}
