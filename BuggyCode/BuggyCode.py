###############################################
# Author: Daniel Leftley       File: Pong_Leftley_Daniel.py
#Date: 12/19/2023
#Description: A recreation of the clasic Arcade game Pong, Player 1 uses W & S to move while Player 2 uses ^ and v to move.
################################################
import pgzrun, pgzero, random

WIDTH = 800
HEIGHT = 600

background = Actor('board')
background.x = 400
background.y = 300

def draw():
    background.draw()

pgzrun.go()