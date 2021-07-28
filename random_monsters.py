#!/usr/bin/env python3


"""Return a random monster.
   
   Monster content copyright belongs to 
   [Sky Flourish](https://skyflourish.com).

   Support Sky Flourish by purchasing the 
   [Return of the Lazy DM](https://slyflourish.com/returnofthelazydm/).
"""

import os
import sys
import argparse
from copy import copy
from random import shuffle

CR_18_14 = "1/8-1/4"
CR_14_1 = "1/4-1"
CR_1_2 = "1-2"
CR_2_3 = "2-3"
CR_3_4 = "3-4"
CR_4_5 = "4-5"
CR_5_8 = "5-8"
CR_8_12 = "8-12"
CR_12_16 = "12-16"
CR_16_24 = "16-24"
CR_CHOICES = [
    CR_18_14,
    CR_14_1,
    CR_1_2,
    CR_2_3,
    CR_3_4,
    CR_4_5,
    CR_5_8,
    CR_8_12,
    CR_12_16,
    CR_16_24,
]


creatures_cr_18_14 = [
    "Bandit",
    "Cultist",
    "Flying snake",
    "Giant crab",
    "Giant rat",
    "Kobold",
    "Poisonous snake",
    "Stirge",
    "Tribal warrior",
    "Axe beak",
    "Blink dog",
    "Dretch",
    "Drow",
    "Giant bat",
    "Giant frog",
    "Giant wolf spider",
    "Goblin",
    "Skeleton",
    "Swarm of bats",
    "Swarm of rats",
]
creatures_cr_14_1 = [
    "Wolf",
    "Zombie",
    "Cockatrice",
    "Darkmantle",
    "Gnoll",
    "Gray ooze",
    "Hobgoblin",
    "Lizardfolk",
    "Magmin",
    "Orc",
    "Rust monster",
    "Sahuagin",
    "Scout",
    "Shadow",
    "Swarm of insects",
    "Thug",
    "Worg",
    "Animated armor",
    "Bugbear",
    "Death dog",
]
creatures_cr_1_2 = [
    "Dire wolf",
    "Duergar",
    "Ghoul",
    "Giant spider",
    "Giant toad",
    "Harpy",
    "Imp",
    "Specter",
    "Spy",
    "Ankheg",
    "Bandit captain",
    "Berserker",
    "Black dragon wyrmling",
    "Cult fanatic",
    "Ettercap",
    "Gargoyle",
    "Gelatinous cube",
    "Ghast",
    "Giant constrictor snake",
    "Gibbering mouther",
]
creatures_cr_2_3 = [
    "Azer",
    "Green dragon wyrmling",
    "Grick",
    "Grifon",
    "Merrow",
    "Mimic",
    "Minotaur skeleton",
    "Ochre jelly",
    "Ogre",
    "Ogre zombie",
    "Priest",
    "Rug of smothering",
    "Sea hag",
    "Swarm of poisonous snakes",
    "Wererat",
    "White dragon wyrmling",
    "Will-o’-wisp",
    "Basilisk",
    "Bearded devil",
    "Blue dragon wyrmling",
]
creatures_cr_3_4 = [
    "Doppelganger",
    "Giant scorpion",
    "Green hag",
    "Hell hound",
    "Knight",
    "Manticore",
    "Minotaur",
    "Mummy",
    "Nightmare",
    "Owlbear",
    "Phase spider",
    "Veteran",
    "Werewolf",
    "Wight",
    "Winter wolf",
    "Black pudding",
    "Chuul",
    "Couatl",
    "Ettin",
    "Ghost",
]
creatures_cr_4_5 = [
    "Lamia",
    "Red dragon wyrmling",
    "Succubus/incubus",
    "Wereboar",
    "Air elemental",
    "Barbed devil",
    "Bulette",
    "Earth elemental",
    "Fire elemental",
    "Flesh golem",
    "Giant crocodile",
    "Gladiator",
    "Gorgon",
    "Half-red dragon veteran",
    "Hill giant",
    "Night hag",
    "Otyugh",
    "Roper",
    "Shambling mound",
    "Troll",
]
creatures_cr_5_8 = [
    "Salamander",
    "Vampire spawn",
    "Water elemental",
    "Wraith",
    "Xorn",
    "Chimera",
    "Drider",
    "Invisible stalker",
    "Mage",
    "Medusa",
    "Vrock",
    "Wyvern",
    "Young white dragon",
    "Oni",
    "Shield guardian",
    "Stone giant",
    "Young black dragon",
    "Assassin",
    "Chain devil",
    "Cloaker",
]
creatures_cr_8_12 = [
    "Frost giant",
    "Hezrou",
    "Hydra",
    "Spirit naga",
    "Young green dragon",
    "Bone devil",
    "Clay golem",
    "Cloud giant",
    "Fire giant",
    "Glabrezu",
    "Young blue dragon",
    "Aboleth",
    "Guardian naga",
    "Stone golem",
    "Young red dragon",
    "Behir",
    "Ereeti",
    "Horned devil",
    "Remorhaz",
    "Archmage",
]
creatures_cr_12_16 = [
    "Erinyes",
    "Adult white dragon",
    "Nalfeshnee",
    "Rakshasa",
    "Storm giant",
    "Vampire",
    "Adult black dragon",
    "Ice devil",
    "Adult green dragon",
    "Mummy lord",
    "Purple worm",
    "Adult blue dragon",
]
creatures_cr_16_24 = [
    "Iron golem",
    "Marilith",
    "Adult red dragon",
    "Balor",
    "Ancient white dragon",
    "Pit fiend",
    "Ancient black dragon",
    "Lich",
    "Ancient blue dragon",
    "Ancient red dragon",
]


def generate_monsters(creatures, length=1):
    _creatures = copy(creatures)
    # Guard against a length arg > than the shortest list
    length = min(len(creatures), length)

    shuffle(creatures)
    return creatures[:length]


def main(argv):
    description = __doc__
    formatter_class = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(
        description=description, formatter_class=formatter_class
    )

    parser.add_argument("-cr", choices=CR_CHOICES, default=CR_18_14, type=str)
    parser.add_argument("-l", "--length", default=10, type=int)

    args = parser.parse_args(argv)
    cr = args.cr
    length = args.length

    if cr == CR_18_14:
        monsters = generate_monsters(creatures_cr_18_14, length)
    if cr == CR_14_1:
        monsters = generate_monsters(creatures_cr_14_1, length)
    if cr == CR_1_2:
        monsters = generate_monsters(creatures_cr_1_2, length)
    if cr == CR_2_3:
        monsters = generate_monsters(creatures_cr_2_3, length)
    if cr == CR_3_4:
        monsters = generate_monsters(creatures_cr_3_4, length)
    if cr == CR_4_5:
        monsters = generate_monsters(creatures_cr_4_5, length)
    if cr == CR_5_8:
        monsters = generate_monsters(creatures_cr_5_8, length)
    if cr == CR_8_12:
        monsters = generate_monsters(creatures_cr_8_12, length)
    if cr == CR_12_16:
        monsters = generate_monsters(creatures_cr_12_16, length)
    if cr == CR_16_24:
        monsters = generate_monsters(creatures_cr_16_24, length)

    for monster in monsters:
        print(monster)


if __name__ == "__main__":
    argv = sys.argv[1:]
    sys.exit(main(argv))
