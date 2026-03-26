import pygame

WIDTH=1000
HEIGHT=600

WIN=pygame.display.set_mode((WIDTH,HEIGHT))
TITLE=pygame.display.set_caption('Space Marshal')
WHITE = (255,255,255)
FPS=60
SPACESHIP_WIDTH=55
SPACESHIP_HEIGHT=40

YELLOW_SPACESHIP_IMAGE=pygame.image.load("/Users/macbookair/Python/space_marshal/Assets/spaceship_yellow.png")
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE=pygame.image.load("/Users/macbookair/Python/space_marshal/Assets/spaceship_red.png")
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP,(100,HEIGHT/2))
    WIN.blit(RED_SPACESHIP,(900-SPACESHIP_WIDTH,HEIGHT/2))               ## Blit is used to display text and images on screen
    pygame.display.update()



def main():
    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()
    pygame.quit() 

if __name__=="__main__":
    main()

 