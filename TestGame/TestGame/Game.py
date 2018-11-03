import pygame

WIDTH = 800
HEIGHT = 600
FPS = 60

BLUE = (60, 60, 120)
GREEN = (0, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Test")
clock = pygame.time.Clock()

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/platform.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = 4*HEIGHT / 5

class Player(pygame.sprite.Sprite):

    forward = pygame.image.load("images/forwardg.png").convert_alpha()
    forwardrun = pygame.image.load("images/forwardrun.png").convert_alpha()
    forwardj = pygame.image.load("images/forwardj.png").convert_alpha()
    backward = pygame.image.load("images/backwardg.png").convert_alpha()
    backwardrun = pygame.image.load("images/backwardrun.png").convert_alpha()
    backwardj = pygame.image.load("images/backwardj.png").convert_alpha()


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Player.forward
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.canJump = True
        self.facingforward = True
        self.speedx = 0
        self.speedy = 0

    def update(self):
        Player.acceleratex(self)
        Player.acceleratey(self)

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = 0
            self.canJump = True
        if self.rect.top < 0:
            self.rect.top = 0

    def acceleratex(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.facingforward = False
            self.speedx += -1
            if self.canJump:
                self.image = Player.backwardrun
            else:
                self.image = Player.backwardj
            if self.speedx < -10:
                self.speedx = -10
        if keystate[pygame.K_d]:
            self.speedx += 1
            self.facingforward = True
            if self.canJump:
                self.image = Player.forwardrun
            else:
                self.image = Player.forwardj
            if self.speedx > 10:
                self.speedx = 10
        if (not keystate[pygame.K_a] and not keystate[pygame.K_d]) or (keystate[pygame.K_a] and keystate[pygame.K_d]):
            if self.canJump:
                if self.facingforward:
                    self.image = Player.forward
                else:
                    self.image = Player.backward
            else:
                if self.facingforward:
                    self.image = Player.forwardj
                else:
                    self.image = Player.backwardj
            self.speedx = 0

    def acceleratey(self):
        keystate = pygame.key.get_pressed()
        if self.canJump:
            self.speedy = 0
        if keystate[pygame.K_SPACE] and self.canJump:
            self.speedy = -11
            self.canJump = False
        self.speedy += .4
        if self.speedy > 25:
            self.speedy = 25

all_sprites = pygame.sprite.Group()
plats = pygame.sprite.Group()
player = Player()
platform = Platform()
all_sprites.add(player)
all_sprites.add(platform)
plats.add(platform)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    onplat = pygame.sprite.spritecollide(player, plats, False)
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()