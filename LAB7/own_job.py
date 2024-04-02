import pygame
import time 
import sys

pygame.init()
size = (1080,960)
screen = pygame.display.set_mode((size))

screen = pygame.display.set_mode(size)
back = pygame.image.load("lab7/myjob/back.jpg")
seconds = pygame.image.load("lab7/myjob/seconds.png")
minutes = pygame.image.load("lab7/myjob/minutes.png")

finish = True
while finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = False

    screen.blit(back, (0,0))

    now = time.localtime()

    minute_angle = 360 - (now.tm_min * 6)
    min_rotate = pygame.transform.rotate(minutes, minute_angle)
    min_pos = ((size[0] - min_rotate.get_width())/2, (size[1] - min_rotate.get_width())/2)
    screen.blit(min_rotate, min_pos)

    second_angle = 360 - (now.tm_sec * 6)
    sec_rotate = pygame.transform.rotate(seconds, second_angle)
    sec_pos = ((size[0] - sec_rotate.get_width())/2, (size[1] - sec_rotate.get_width())/2)
    screen.blit(sec_rotate, sec_pos)

    pygame.display.flip()

clock_timer.tick(144)
pygame.quit()
sys.exit()