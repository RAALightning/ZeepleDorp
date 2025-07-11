# Define actor and prop types
from entities.prop import Prop
from entities.actor import Actor, PlayerCharacter, NPC, Monster

ACTOR_TYPE = {
    "Test" : Actor("Test", "I am a test")
}

PROP_TYPE = {
    "Test" : Prop("Test", "It's a test! It might come in handy later.")
}
