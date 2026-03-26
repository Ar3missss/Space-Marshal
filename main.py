import pygame
pygame.init()
WIDTH=1000
HEIGHT=600
BORDER= pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
TITLE=pygame.display.set_caption('Space Marshal')
WHITE = (255,255,255)
BLACK =(0 ,0 ,0)
RED=(255,0,0)
YELLOW=(255,255,0)
FPS=60
VEL=5
BULLET_VEL=7
MAX_BULLETS=5
SPACESHIP_WIDTH=55
SPACESHIP_HEIGHT=40
YELLOW_HIT=pygame.USEREVENT+1
RED_HIT=pygame.USEREVENT+2
YELLOW_SPACESHIP_IMAGE=pygame.image.load("/Users/macbookair/Python/space_marshall/Assets/spaceship_yellow.png")
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE=pygame.image.load("/Users/macbookair/Python/space_marshall/Assets/spaceship_red.png")
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
SPACE=pygame.transform.scale(pygame.image.load("/Users/macbookair/Python/space_marshall/Assets/space.png"),(WIDTH,HEIGHT))


## DRAW
def draw_window(yellow,red,red_bullets,yellow_bullets):   ## draw fxn is used only to draw or u can say only to display it does not create any objects so we passed yellow and red
    WIN.blit(SPACE,(0,0)) 
    pygame.draw.rect(WIN,BLACK,BORDER )
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))               ## Blit is used to display text and images on screen

    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)      
   
    pygame.display.update()


## BULLETS
def handle_bullets(yellow_bullets,red_bullets,yellow,red):
            for bullet in yellow_bullets:
                bullet.x +=BULLET_VEL

                if red.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(RED_HIT))
                    yellow_bullets.remove(bullet)

                elif bullet.x > WIDTH:
                      yellow_bullets.remove(bullet) 

            for bullet in red_bullets:
                bullet.x -=BULLET_VEL
                
                if yellow.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(YELLOW_HIT))
                    red_bullets.remove(bullet)          

                elif bullet.x <0:
                      red_bullets.remove(bullet)  

## SPACESHIPS MOVEMENTS
def yellow_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL>=0 :         # left
            yellow.x -= VEL

    if keys_pressed[pygame.K_d] and yellow.x+VEL+SPACESHIP_HEIGHT<=BORDER.x:  # Right
            yellow.x += VEL

    if keys_pressed[pygame.K_w] and yellow.y - VEL>=0:      # UP
            yellow.y -= VEL 

    if keys_pressed[pygame.K_s] and yellow.y +VEL+SPACESHIP_WIDTH<= HEIGHT:  # Down 
            yellow.y += VEL                   


def red_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x -VEL>=BORDER.x+BORDER.width :         # left
            red.x -= VEL

    if keys_pressed[pygame.K_RIGHT] and red.x+VEL+SPACESHIP_HEIGHT<=WIDTH:  # Right
            red.x += VEL

    if keys_pressed[pygame.K_UP] and red.y - VEL>=0:      # UP
            red.y -= VEL 

    if keys_pressed[pygame.K_DOWN] and red.y +VEL+SPACESHIP_WIDTH<= HEIGHT:  # Down 
            red.y += VEL                 


## MAIN LOOP
def main():
    yellow=pygame.Rect(100,HEIGHT/2,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)                ## Rect fxn create your object it stores the posistion,width and height of ur object 
    red= pygame.Rect(900-SPACESHIP_WIDTH,HEIGHT/2,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    
    yellow_bullets=[]
    red_bullets=[]
    
    clock=pygame.time.Clock()                                            ## It is used to maintain a constant FPS in all systems
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets)<MAX_BULLETS:
                    Bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,3)
                    yellow_bullets.append(Bullet)
              
                if event.key == pygame.K_SPACE and len(red_bullets)<MAX_BULLETS:
                    Bullet=pygame.Rect(red.x,red.y+red.height//2-2,10,3)
                    red_bullets.append(Bullet)    

        
        keys_pressed=pygame.key.get_pressed()
        yellow_movement(keys_pressed,yellow)
        red_movement(keys_pressed,red)
        
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(yellow,red,red_bullets,yellow_bullets)
    pygame.quit() 

if __name__=="__main__":
    main()

 