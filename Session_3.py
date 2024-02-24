import pygame
pygame.init() #initialise phase

#screen set up
SCREENX = 500
SCREENY = 500
DELAY_MS= 50
window = pygame.display.set_mode((SCREENX,SCREENY))
pygame.display.set_caption('YASSS')
x=50
y=50
width=50
height=50
vel=5
COL=(250,0,0)
jump = False
JUMP_COUNT_MAX = 5
jumpcount=JUMP_COUNT_MAX 

run=True
pygame.display.set_caption('First window')

while run:
    pygame.time.delay(DELAY_MS)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
            x-=vel
    elif keys[pygame.K_RIGHT]:   
            x+=vel
    elif keys[pygame.K_UP]:
            y-=vel
    elif keys[pygame.K_DOWN]:
            y+=vel
    elif keys[pygame.K_SPACE]:
            jump=True
    if jump:
         if jumpcount >= -JUMP_COUNT_MAX:
            if jumpcount < 0:
                    sign = -1
            else:
                sign = 1
            y-=sign * jumpcount**2
            jumpcount-=1
         else:
                jump=False
                jumpcount = JUMP_COUNT_MAX
            
 
    window.fill('Black')    
    pygame.draw.rect(window,COL,(x,y,width,height))
    pygame.display.update()

pygame.quit()
