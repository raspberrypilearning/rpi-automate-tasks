## Code to automate

If you do not have a Python script you would like to use, then this one will play a sound.

--- task ---

Download this sound file: <a href="resources/start.mp3" download>start.mp3</a>

--- /task ---

--- task ---

Move the sound file to your `/home/username/` folder.

**Note**: Change `username` to your username!

--- /task ---

--- task ---
Open Thonny.
--- /task ---

--- task ---
Add this code.

```python
import pygame
import time

time.sleep(3)
pygame.init()
my_sound = pygame.mixer.Sound('/home/username/start.mp3')

my_sound.play()

while pygame.mixer.get_busy():
    time.sleep(0.1)
```
**Note**: Change `username` to your username.
--- /task ---

--- task ---
Save the Python file to `/home/username/start.py` 

**Note**: Change `username` to your username.
--- /task ---