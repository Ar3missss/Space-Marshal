import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()


WIDTH=1000
HEIGHT=600
HEALTH_FONT=pygame.font.SysFont('comicsans',40)
WINNER_FONT=pygame.font.SysFont('comicsans',100)
BORDER= pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
RED_HIT=pygame.USEREVENT+2
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
BULLET_HIT_SOUND=pygame.mixer.Sound("/Users/macbookair/Python/space_marshall/Assets/Grenade+1.mp3")
BULLET_FIRE_SOUND=pygame.mixer.Sound("/Users/macbookair/Python/space_marshall/Assets/Gun+Silencer.mp3")
YELLOW_SPACESHIP_IMAGE=pygame.image.load("/Users/macbookair/Python/space_marshall/Assets/spaceship_yellow.png")
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE=pygame.image.load("/Users/macbookair/Python/space_marshall/Assets/spaceship_red.png")
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
SPACE=pygame.transform.scale(pygame.image.load("/Users/macbookair/Python/space_marshall/Assets/space.png"),(WIDTH,HEIGHT))



## DRAW
def draw_window(yellow,red,red_bullets,yellow_bullets,red_health,yellow_health):   ## draw fxn is used only to draw or u can say only to display it does not create any objects so we passed yellow and red
    WIN.blit(SPACE,(0,0)) 
    pygame.draw.rect(WIN,BLACK,BORDER )
    red_health_text=HEALTH_FONT .render("Health :" +str(red_health),1,WHITE)
    yellow_health_text=HEALTH_FONT.render("Health :" +str(yellow_health),1,WHITE)
    WIN.blit(red_health_text,(WIDTH-red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text,(10,10))
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


def draw_winner(text):
      draw_text=WINNER_FONT.render(text,1,WHITE)
      WIN.blit(draw_text,(WIDTH/2-draw_text.get_width()/2,HEIGHT/2-draw_text.get_height()/2))
      pygame.display.update()
      pygame.time.delay(5000)
      

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
    red_health=3
    yellow_health=3
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
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets)<MAX_BULLETS:
                    Bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,3)
                    yellow_bullets.append(Bullet)
                    BULLET_FIRE_SOUND.play()
              
                if event.key == pygame.K_SPACE and len(red_bullets)<MAX_BULLETS:
                    Bullet=pygame.Rect(red.x,red.y+red.height//2-2,10,3)
                    red_bullets.append(Bullet)  
                    BULLET_FIRE_SOUND.play()

            if event.type==RED_HIT:
                  red_health-=1
                  BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                  yellow_health-=1 
                  BULLET_HIT_SOUND.play()    

        winner_text=""
        if red_health<=0:
            winner_text="Yellow Wins!"
        if yellow_health<=0:  
            winner_text="Red Wins!"
        if winner_text !="":
              draw_winner(winner_text)
              break        
        
        keys_pressed=pygame.key.get_pressed()
        yellow_movement(keys_pressed,yellow)
        red_movement(keys_pressed,red)
        
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        draw_window(yellow,red,red_bullets,yellow_bullets,red_health,yellow_health)
    main() 

if __name__=="__main__":
    main()

 