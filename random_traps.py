#!/usr/bin/env python3


"""Return a random trap.
   
   Trap content copyright belongs to 
   [Sky Flourish](https://skyflourish.com).

   Support Sky Flourish by purchasing the 
   [Return of the Lazy DM](https://slyflourish.com/returnofthelazydm/).

"""

import os
import sys
import argparse
import timeit
from copy import copy
from random import shuffle

trap_types = [
    "bolts",
    "spears",
    "scythes",
    "bolos",
    "spiked chains",
    "pit",
    "rolling ball",
    "crushing pillars",
    "darts",
    "glyphs",
    "swords",
    "axes",
    "tendrils",
    "whips",
    "nets",
    "hunting",
    "cages",
    "beams",
    "hammers",
    "shurikens",
    "gas",
]

trap_flavors = [
    "A fiery",
    "A freezing",
    "A necrotic",
    "A poisonous",
    "An acidic",
    "A thunderous",
    "A lightning",
    "A forceful",
    "A diseased",
    "A stunning",
    "A blinding",
    "A deafening",
    "A weakening",
    "A draining",
    "A sleep-inducing",
    "A binding",
    "A dominating",
    "A psychic",
    "A maddening",
    "A confusing",
]

trap_triggers = [
    "a door",
    "a floor plate",
    "a tripwire",
    "a throne",
    "a corpse",
    "a chest",
    "a old book",
    "a child's toy",
    "a jeweled skull",
    "beams of light",
    "a golden angelic statue",
    "a crystal goblet on a pedestal",
    "an onyx demonic skull",
    "a jeweled pillar",
    "a steep stair",
    "a jeweled crown",
    "a gilded sarcophagus",
    "a bound prisoner",
    "a weapon on an altar",
    "a idol on a pedestal",
]


def generate_traps(trap_types, trap_flavors, trap_triggers, length=1):
    _trap_types = copy(trap_types)
    _trap_flavors = copy(trap_flavors)
    _trap_triggers = copy(trap_triggers)
    memo = []

    for _ in range(length):
        shuffle(_trap_types)
        shuffle(_trap_flavors)
        shuffle(_trap_triggers)

        memo.append((_trap_types[0], _trap_flavors[0], _trap_triggers[0]))

    return memo


def main(argv, trap_types, trap_flavors, trap_triggers):
    start_time = timeit.default_timer()
    description = __doc__
    formatter_class = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(
        description=description, formatter_class=formatter_class
    )

    parser.add_argument("-l", "--length", default=10, type=int)

    args = parser.parse_args(argv)
    length = args.length
    traps = generate_traps(trap_types, trap_flavors, trap_triggers, length)

    for type, flavor, trigger in traps:
        print(f"{flavor}, {type} trap triggered by {trigger}")

    time_elapsed = timeit.default_timer() - start_time
    print(f"\nReturned {length} results in {time_elapsed:.4f} seconds!")


if __name__ == "__main__":
    argv = sys.argv[1:]
    sys.exit(main(argv, trap_types, trap_flavors, trap_triggers))
