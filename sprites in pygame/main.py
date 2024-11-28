import pygame
pygame.init()

pygame.display.set_caption("Sprites in pygame")
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

bkg = pygame.image.load("bkg.jpg")
bkg = pygame.transform.scale(bkg, (700,500))

#player class
class Player(pygame.sprite.Sprite):
    #attribute
    def __init__(self):
        #super extracts attributes of sprite class which is the parent class
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect()


#create a group 
sprites = pygame.sprite.Group()

def gameStart():
    rocket = Player()
    #add sprite to the group
    sprites.add(rocket)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                
        screen.blit(bkg, (0,0))
        sprites.draw(screen)
        pygame.display.update()

gameStart()