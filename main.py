import pygame

WIDTH=1000
HEIGHT=600

WIN=pygame.display.set_mode((WIDTH,HEIGHT))
TITLE=pygame.display.set_caption('Space Marshal')
WHITE = (255,255,255)
FPS=60
VEL=5
SPACESHIP_WIDTH=55
SPACESHIP_HEIGHT=40

YELLOW_SPACESHIP_IMAGE=pygame.image.load("/Users/macbookair/Python/space_marshall/Assets/spaceship_yellow.png")
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE=pygame.image.load("/Users/macbookair/Python/space_marshall/Assets/spaceship_red.png")
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

def draw_window(yellow,red):                            ## draw fxn is used only to draw or u can say only to display it does not create any objects so we passed yellow and red
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))               ## Blit is used to display text and images on screen
    pygame.display.update()


def yellow_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL>=0 :         # left
            yellow.x -= VEL

    if keys_pressed[pygame.K_d] and yellow.x+VEL+SPACESHIP_HEIGHT<=WIDTH:  # Right
            yellow.x += VEL

    if keys_pressed[pygame.K_w] and yellow.y - VEL>=0:      # UP
            yellow.y -= VEL 

    if keys_pressed[pygame.K_s] and yellow.y +VEL+SPACESHIP_WIDTH<= HEIGHT:  # Down 
            yellow.y += VEL                   


def red_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL>=0 :         # left
            red.x -= VEL

    if keys_pressed[pygame.K_RIGHT] and red.x+VEL+SPACESHIP_HEIGHT<=WIDTH:  # Right
            red.x += VEL

    if keys_pressed[pygame.K_UP] and red.y - VEL>=0:      # UP
            red.y -= VEL 

    if keys_pressed[pygame.K_DOWN] and red.y +VEL+SPACESHIP_WIDTH<= HEIGHT:  # Down 
            red.y += VEL                 

def main():
    yellow=pygame.Rect(100,HEIGHT/2,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)                ## Rect fxn create your object it stores the posistion,width and height of ur object 
    red= pygame.Rect(900-SPACESHIP_WIDTH,HEIGHT/2,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    clock=pygame.time.Clock()                                            ## It is used to maintain a constant FPS in all systems
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed=pygame.key.get_pressed()
        yellow_movement(keys_pressed,yellow)
        red_movement(keys_pressed,red)
        
        draw_window(yellow,red)
    pygame.quit() 

if __name__=="__main__":
    main()

 