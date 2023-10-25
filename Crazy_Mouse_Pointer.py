# Crazy_Mouse_Pointer

# 🖱️ Move the mouse cursor to random positions within the screen dimensions. 
# Stop the script by pressing Ctrl+C in your terminal.

# Copyright (C) 2023, Sourceduty - All Rights Reserved.
# THE CONTENTS OF THIS PROJECT ARE PROPRIETARY.

import pyautogui
import time
import random

# Define the screen dimensions
screen_width, screen_height = pyautogui.size()

try:
    while True:
        # Generate random coordinates within the screen dimensions
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)

        # Move the mouse cursor to the random position
        pyautogui.moveTo(x, y, duration=1)

        # Pause for a random duration before moving again
        time.sleep(random.uniform(1, 3))

except KeyboardInterrupt:
    print("Mouse drifting stopped.")
