import random
from turtle import left
import pygame
pygame.init()
pygame.font.init()
pygame.font.get_init()
size = 900,800
screen = pygame.display.set_mode(size)
running = True
bg = pygame.image.load('bg.png')
pig = pygame.image.load('pig.png')
px = 200
py = 650
ispressed = False
isleft = False
coupon = pygame.image.load('coupon.png')
cx = random.randint(50,700)
cy = -10
fall = False
score = 0
clock = pygame.time.Clock()
icon = pygame.image.load('icon.png')
show = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    if event.type == pygame.KEYDOWN:
        ispressed = True
        if event.key == pygame.K_LEFT:
            isleft = True
        if event.key == pygame.K_RIGHT:
            isleft = False
        if ispressed:
            if isleft:
                px -= 20
            else:
                px += 20
    fall= True
    if fall:
        cy += 15
        screen.blit(bg,(0,0))
        time = pygame.time.get_ticks()
        screen.blit(pig,(px,py))
        prect = pig.get_rect(left = px, top = py)
        screen.blit(coupon,(cx,cy))
        crect = coupon.get_rect(left = cx, top = cy)
        if prect.colliderect(crect):
            cx = random.randint(50,700)
            cy = 100
            score += 1
        if cy >= 800:
            cx = random.randint(50,700)
            cy = -10
            score -= 1
        if pygame.font.get_init():
            print('initialized')
        if score >= 10:
            cy += 20
        if score >= 50:
            cy+=25
        if score >= 200:
            cy += 35
        pygame.display.set_caption("Musty Crusty's Coupon Catch")
        pygame.display.set_icon(icon)
        
        if show:
            timetxt = pygame.font.SysFont('comic sans ms',70,False,False)
            timetext = timetxt.render('Time Passed: {}'.format(time/1000),0,0)
            screen.blit(timetext,(0,100))
        
        if show:
            stxt = pygame.font.SysFont('comic sans ms', 70,False,False)
            stext = stxt.render('Coupons: {}'.format(score),0,0)
            screen.blit(stext,(0,0))
        if score <= -1:
            # show = False
            gtxt = pygame.font.SysFont('comic sans ms',70,False,False)
            gtext = gtxt.render('GAME OVER!',0,0)
            show = False
            screen.blit(gtext,(400,100))
            pygame.time.delay(1000)
            
            #quit()
            #pygame.quit()
            running = False
        clock.tick(60)
        pygame.display.flip()