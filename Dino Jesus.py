from pygame import *
from time import sleep
from random import randint
isJump = False
jumpCount = 10
"""mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()"""


font.init()
font =  font.Font(None,70)
win = font.render("YOU WIN", True, (255,215,0))
lose = font.render ('YOU LOSE', True, (180,0,0))
finish = True
win_widht = 700
win_height = 500
game = True
clock = time.Clock()
FPS = 60
# Создание игрового окна
window = display.set_mode((win_widht, win_height))
display.set_caption("DINO JISUS")
background = transform.scale(image.load('backgrounde.png'), (win_widht, win_height))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,player_speed_y):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.speed_y = player_speed_y

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Dino(GameSprite):
    # Функция обновления обьекта
    def update(self):
        keys = key.get_pressed()
        global isJump
        global jumpCount
        if keys[K_d] and self.rect.x > 5:
            self.rect.x += self.speed
        if keys[K_SPACE]:
            isJump = True
            if jumpCount >= -10:
                self.rect.y -= (jumpCount * abs(jumpCount)) * 0.75
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False


dino = Dino('dinos.png', 10, 330, 65, 80,10,0) 
cactus = GameSprite('cactuses.png', 120, 320, 95,80, 10, 0)
cactus1 = GameSprite('cactuses.png', 370, 320, 95,80, 10, 0)
cactus2 = GameSprite('cactuses.png', 420, 320, 95,80, 10, 0)
treasure = GameSprite('treasure.png', win_widht-120,320 ,100,100,0,0 )
while game:
    # Сделать завешение игры по нажатию крестика
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish:
        window.blit(background, (0, 0))
    # Реализовать отрисовка спрайтов 

        dino.update ()
        dino.reset()
        cactus.update()
        cactus.reset()    
        cactus1.update()
        cactus1.reset()
        cactus2.update()
        cactus2.reset()
        treasure.update()
        treasure.reset()

        if sprite.collide_rect(dino, cactus) or sprite.collide_rect(dino, cactus1) or  sprite.collide_rect(dino, cactus2):
            finish = False
            window.blit(lose,(200,200))
        if sprite.collide_rect(dino, treasure):
            finish = False
            window.blit(win, (200,200))   
        display.update()
        time.delay(FPS)
        






