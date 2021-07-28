#!/usr/bin/env python3


"""Return a random item.
   
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

ITEM_TYPE_WEAPON = "weapon"
ITEM_TYPE_ARMOR = "armor"
ITEM_TYPE_MUNDANE = "mundane"

weapon_items = [
    "dagger",
    "mace",
    "quarterstaf",
    "spear",
    "light crossbow",
    "shortbow",
    "battleaxe",
    "flail",
    "glaive",
    "greataxe",
    "greatsword",
    "longsword",
    "maul",
    "morningstar",
    "rapier",
    "scimitar",
    "shortsword",
    "warhammer",
    "heavy crossbow",
    "longbow",
]

armor_items = [
    "leather armor",
    "studded leather armor",
    "hide armor",
    "chain shirt armor",
    "scale mail armor",
    "breastplate armor",
    "half plate armor",
    "ring mail armor",
    "chain mail armor",
    "splint armor",
    "plate armor",
    "shield",
]

mundane_items = [
    "amulet",
    "arrowhead",
    "bell",
    "bird skull",
    "bone",
    "bowl",
    "box",
    "bracelet",
    "brooch",
    "buckle",
    "candle",
    "coin",
    "crown",
    "cup",
    "dagger",
    "disc",
    "earring",
    "figurine",
    "finger bone",
    "flute",
    "forked rod",
    "gemstone",
    "glove",
    "goblet",
    "hammer",
    "idol",
    "jewelry box",
    "key",
    "lamp",
    "mask",
    "medallion",
    "mirror",
    "necklace",
    "opal",
    "orb",
    "pipe",
    "quill",
    "ring",
    "rod",
    "skull",
    "sphere",
    "spike",
    "statue",
    "stone",
    "string of beads",
    "symbol",
    "tiara",
    "tooth",
    "vial",
    "wand",
]

item_origins = [
    "Draconic",
    "Dwarven",
    "Elven",
    "Primeval",
    "Divine",
    "Unholy",
    "Abyssal",
    "Otherworldly",
    "Orcish",
    "Undead",
    "Goblinoid",
    "Ghoulish",
    "Vampiric",
    "Dark elven",
    "Astral",
    "Ethereal",
    "Hellish",
    "Demonic",
    "Elemental",
    "Gnomish",
]

item_conditions = [
    "grimy",
    "chipped",
    "rough",
    "smooth",
    "ancient",
    "crumbling",
    "pristine",
    "cool",
    "ornate",
    "plain",
    "rune-scribed",
    "carved",
    "decorated",
    "delicate",
    "burned",
    "oily",
    "pulsing",
    "glowing",
    "shining",
    "smoldering",
]

item_spell_effects = [
    "Light",
    "Bane",
    "Bless",
    "Cure wounds",
    "Detect evil and good",
    "Detect magic",
    "Guiding bolt",
    "Inflict wounds",
    "Shield of faith",
    "Blindness/deafness",
    "Silence",
    "Bestow curse",
    "Dispel magic",
    "Flame strike",
    "Insect plague",
    "Acid splash",
    "Shocking grasp",
    "True strike",
    "Burning hands",
    "Charm person",
    "Color spray",
    "Comprehend languages",
    "Detect magic",
    "Fog cloud",
    "Jump",
    "Sleep",
    "Thunderwave",
    "Acid arrow",
    "Invisibility",
    "Misty step",
    "Ray of enfeeblement",
    "Scorching ray",
    "Shatter",
    "Web ",
    "Fear",
    "Fly",
    "Gaseous form",
    "Haste",
    "Lightning bolt",
    "Slow",
    "Stinking cloud",
    "Banishment",
    "Black tentacles",
    "Blight",
    "Fire shield",
    "Ice storm",
    "Stoneskin",
    "Cloudkill",
    "Cone of cold",
    "Disintegrate",
]


def generate_items(items, item_origins, item_conditions, item_spell_effects, length=1):
    _items = copy(items)
    _item_origins = copy(item_origins)
    _item_conditions = copy(item_conditions)
    _item_spell_effects = copy(item_spell_effects)

    # Guard against a length arg > than the shortest list
    max_len = min(
        (
            len(_items),
            len(_item_origins),
            len(_item_conditions),
            len(_item_spell_effects),
        )
    )
    length = min(max_len, length)

    shuffle(_items)
    shuffle(_item_origins)
    shuffle(_item_conditions)
    shuffle(_item_spell_effects)

    return zip(
        _items[:length],
        _item_origins[:length],
        _item_conditions[:length],
        _item_spell_effects[:length],
    )


def main(
    argv,
    weapon_items,
    armor_items,
    mundane_items,
    item_origins,
    item_conditions,
    item_spell_effects,
):
    description = __doc__
    formatter_class = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(
        description=description, formatter_class=formatter_class
    )

    parser.add_argument(
        "-t",
        "--item_type",
        choices=[ITEM_TYPE_WEAPON, ITEM_TYPE_ARMOR, ITEM_TYPE_MUNDANE],
        required=True,
        type=str,
    )
    parser.add_argument("-l", "--length", default=10, type=int)

    args = parser.parse_args(argv)
    item_type = args.item_type
    is_weapons = item_type == ITEM_TYPE_WEAPON
    is_armor = item_type == ITEM_TYPE_ARMOR
    is_mundane = item_type == ITEM_TYPE_MUNDANE
    shared_args = (item_origins, item_conditions, item_spell_effects, args.length)

    if is_weapons:
        items = generate_items(weapon_items, *shared_args)
    if is_armor:
        items = generate_items(armor_items, *shared_args)
    if is_mundane:
        items = generate_items(mundane_items, *shared_args)

    for item, origin, condition, spell_effect in items:
        print(
            f"A {condition}, {origin}, {item} that can convey a single use of {spell_effect}"
        )


if __name__ == "__main__":
    argv = sys.argv[1:]
    sys.exit(
        main(
            argv,
            weapon_items,
            armor_items,
            mundane_items,
            item_origins,
            item_conditions,
            item_spell_effects,
        )
    )
