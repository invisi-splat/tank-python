"""
Defines the updating process. Call update() to call the updating process.
All variables are defined in config.py and can be updated in there.
"""

import config
from config import tank1, tank2
import shutil
import sys
import time
import math
import random
import draw
import delete
sys.path.insert(0, r".")
import keyboard


def update_gridsize(snap):
    """Updates the size of the grid. Passes this to config.lines_to_delete.

    If "snap" is passed as a parameter, then the grid changes size dynamically.
    """
    if snap == "snap":
        terminal_size = shutil.get_terminal_size()
        # lines - 3 because of the 2 occupied by the box and the 1 occupied by
        # the cursor
        config.lines_to_delete = terminal_size.lines
        config.grid = (terminal_size.columns - 2, terminal_size.lines - 3)
    else:
        config.lines_to_delete = config.grid[1]
    tank1.update_start_pos()
    tank2.update_start_pos()


def keypress_mode0(grid):
    """Checks keypresses in mode 0 (the game)."""
    tank1_collision = tank1.check_collision(grid)
    tank2_collision = tank2.check_collision(grid)
    if not tank1_collision["y"]:
        if keyboard.is_pressed("w"):
            tank1.y -= (tank1.speed/2)/config.FPS  # halved to improve
        if keyboard.is_pressed("s"):               # consistency in movement
            tank1.y += (tank1.speed/2)/config.FPS
    else:
        tank1.y -= tank1_collision["y"]
    if not tank1_collision["x"]:
        if keyboard.is_pressed("a"):
            tank1.x -= tank1.speed/config.FPS
        if keyboard.is_pressed("d"):
            tank1.x += tank1.speed/config.FPS
    else:
        tank1.x -= tank1_collision["x"]

    if not tank2_collision["y"]:
        if keyboard.is_pressed("o"):
            tank2.y -= (tank2.speed/2)/config.FPS
        if keyboard.is_pressed("l"):
            tank2.y += (tank2.speed/2)/config.FPS
    else:
        tank2.y -= tank2_collision["y"]
    if not tank2_collision["x"]:
        if keyboard.is_pressed("k"):
            tank2.x -= tank2.speed/config.FPS
        if keyboard.is_pressed(";"):
            tank2.x += tank2.speed/config.FPS
    else:
        tank2.x -= tank2_collision["x"]

    def tank_stuff(tank):
        tank.direction %= 360
        tank.startd = time.time()

    if time.time() - tank1.startd > config.cooldown1:
        if keyboard.is_pressed("r"):
            tank1.direction -= 45
            tank_stuff(tank1)
        if keyboard.is_pressed("f"):
            tank1.direction += 45
            tank_stuff(tank1)

    if time.time() - tank2.startd > config.cooldown1:
        if keyboard.is_pressed("["):
            tank2.direction -= 45
            tank_stuff(tank2)
        if keyboard.is_pressed("'"):
            tank2.direction += 45
            tank_stuff(tank2)

    if time.time() - tank1.starts > config.cooldown2 and len(tank1.bullets) < 4:
        if keyboard.is_pressed("c"):
            tank1.shoot_bullet()
            tank1.starts = time.time()
    if time.time() - tank2.starts > config.cooldown2 and len(tank2.bullets) < 4:
        if keyboard.is_pressed("/"):
            tank2.shoot_bullet()
            tank2.starts = time.time()

    if time.time() - tank1.startb > config.cooldown2 and len(tank1.bombs) < 2:
        if keyboard.is_pressed("t"):
            tank1.place_bomb()
            tank1.startb = time.time()
    if time.time() - tank2.startb > config.cooldown2 and len(tank2.bombs) < 2:
        if keyboard.is_pressed("]"):
            tank2.place_bomb()
            tank2.startb = time.time()


def update_bullets(grid, *tanks):
    """Updates bullets, checks for collision with tanks, and the like."""
    allbullets = []
    for tank in tanks:
        bullets = tank.bullets
        for bullet in range(len(bullets)):
            # we use range(len()) so that we can modify the bullets
            # and not a copy of the bullets
            if bullets[bullet].y <= 2 or bullets[bullet].y >= grid[1] - 1:
                bullets[bullet].direction = 180 - bullets[bullet].direction
                # hit side walls

            if bullets[bullet].x <= 2 or bullets[bullet].x >= grid[0] - 1:
                bullets[bullet].direction = 360 - bullets[bullet].direction
                # hit top/bottom wall

            if bullets[bullet].x >= 1 and bullets[bullet].x <= grid[0]:
                bullets[bullet].x += bullets[bullet].speed \
                 * math.sin(math.radians(bullets[bullet].direction))
            if bullets[bullet].y >= 1 and bullets[bullet].y <= grid[1]:
                bullets[bullet].y -= bullets[bullet].speed \
                 * math.cos(math.radians(bullets[bullet].direction))
                # moves bullets

            if bullets[bullet].life <= 0:
                del bullets[bullet]
                break
                # removes bullets once life is over
                # their time has come. it is time for them to perish.

            bullets[bullet].life -= 1  # or if they haven't died, slowly kill
                                       # em off

        hit_bullet = tank.hit_bullet()
        if hit_bullet:
            collision_stuff(tank, hit_bullet[1])  # hit_bullet[1] is the bullet
        allbullets += bullets
    config.allbullets = allbullets


def update_bombs(grid, *tanks):
    allbombs = []
    for tank in tanks:
        bombs = tank.bombs
        for bomb in range(len(bombs)):
            try:
                if bombs[bomb].destruct <= 0:
                    del bombs[bomb]
                elif bombs[bomb].explode:
                    bombs[bomb].destruct -= 1
                elif bombs[bomb].life <= 0:
                    bombs[bomb].explode = True
                else:
                    bombs[bomb].life -= 1
            except IndexError:
                pass
        hit_bomb = tank.hit_bomb()
        if hit_bomb:
            collision_stuff(tank, hit_bomb[1])
        allbombs += bombs
    config.allbombs = allbombs


def collision_stuff(tank, object):
    """Does the stuff once a tank has been hit with an object."""
    for flash in range(8):
        draw.draw("flash", object.origin)
        time.sleep(random.randint(0, 1) / 20)
        delete.delete()
        draw.draw()
        time.sleep(random.randint(0, 1) / 20)
        delete.delete()
    config.reset_scored()
    if tank != object.origin:
        object.origin.score += 1


def pause():
    config.pause = True


def quit():
    config.quit = True


def initupdate():
    update_gridsize("snap")
    tank1.reposition()
    tank2.reposition()


def update():
    """Main update function. Call this to update and calculate. Epic.

    Define the variables used in update.py for the update() function in
    config.py.
    """
    keypress_mode0(config.grid)
    update_bullets(config.grid, tank1, tank2)
    update_bombs(config.grid, tank1, tank2)
    update_gridsize("snap")
