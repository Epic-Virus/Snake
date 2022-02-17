# Snake
import pygame, sys, time, random

speed = 15

#windows sizes

frame_size_x = 720
frame_size_y = 480


check_errors = pygame.init()

if(check_errors[1] > 0):
  print("Error " + check_errors[1])
  else:
  print("Game Succesfully initialized")
  
  #initialise game window
  
  pygame.display.set_caption("Snake Game")
  game_window = pygame.display.set_mode(frame_size_x, frame_size_y)
  
  # colors
  black = pygame.color(0, 0, 0)
  white = pygame.color(255, 255, 255)
  red = pygame.color(255, 0, 0)
  green = pygame.color(0, 255, 0)
  blue = pygame.color(0, 0, 255)
  
  
  fps_controller = pygame.time.Clock()
  # one snake square size
  square_size = 20
  
  def init_vars():
    global head_pos,
