# SPDX-FileCopyrightText: 2021 Sandy Macdonald
#
# SPDX-License-Identifier: MIT

# This example demonstrates how to light keys when pressed.

# Drop the `pmk` folder
# into your `lib` folder on your `CIRCUITPY` drive.

import random
from pmk import PMK
# from pmk.platform.keybow2040 import Keybow2040 as Hardware          # for Keybow 2040
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware  # for Pico RGB Keypad Base

# Set up Keybow
keybow = PMK(Hardware())
keys = keybow.keys

# Use cyan as the colour.
rgb = (0, 255, 255)

def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))

while True:
    # Always remember to call keybow.update() on every iteration of your loop!
    keybow.update()

    # Loop through the keys and set the LED to cyan if pressed, otherwise turn
    # it off (set it to black).
    for key in keys:
        if key.pressed:
            key.set_led(*rgb)
        else:
            key.set_led(0, 0, 0)
