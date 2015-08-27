#!/usr/bin/env python2

#http://www.roguebasin.com/index.php?title=Complete_Roguelike_Tutorial,_using_python%2Blibtcod,_part_1
import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20


def handle_keys():
    global playerx, playery

    key = libtcod.console_check_for_keypress()
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game

    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        playery -=1
    if libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        playery +=1
    if libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        playerx -=1
    if libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        playerx +=1

# INIT and game loop

libtcod.console_set_custom_font(
       'arial12x12.png',
       # 'terminal12x12_gs_ro.png',
        libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD
        )

libtcod.console_init_root(
        SCREEN_WIDTH, 
        SCREEN_HEIGHT, 
        'python/libtcod tutorial', False
        )

con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

libtcod.sys_set_fps(LIMIT_FPS)

playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(con, playerx, playery, '@', libtcod.BKGND_NONE)
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()
    libtcod.console_put_char(con, playerx, playery, ' ', libtcod.BKGND_NONE)

    exit = handle_keys()
    if exit:
        break
