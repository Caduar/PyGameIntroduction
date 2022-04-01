import pygame, random
pygame.init()

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/meteor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y +=1
        
        if self.rect.y > 600:
            self.rect.y = -10
            self.rect.x = random.randrange(900)

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/laser.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 5
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        
    def update(self):
        mouse_pos = pygame.mouse.get_pos()      
        player.rect.x = mouse_pos[0]
        #Codigo para centrar el cursos en el sprite
        player.rect.center = mouse_pos
        player.rect.y = 510

BLACK = (0,0,0)
WHITE = (255,255,255)
size = (900,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
score = 0

player = Player()
meteor_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

all_sprite_list.add(player)
done = False

for i in range(60):
    meteor = Meteor()
    meteor.rect.x = random.randrange(900)
    meteor.rect.y = random.randrange(600)

    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser = Laser()
            laser.rect.x = player.rect.x + 45
            laser.rect.y = player.rect.y - 20
            all_sprite_list.add(laser)
            laser_list.add(laser)
    all_sprite_list.update()
    
    for laser in laser_list:
        meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list,True)
        for meteor in meteor_hit_list:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
            score +=1
            print(score)
        if laser.rect.y < -10:
            all_sprite_list.remove(laser)
            laser_list.remove(laser)
        
    screen.fill(WHITE)
    all_sprite_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit() 