'''from pygame import *
 
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
 
#класс-наследник для игрока (управляется стрелками)
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 
#класс-наследник для второго игрока (управляется клавишами W,S)
class Player_two(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

  
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
 
 
#Персонажи игры:
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
 
 
game = True
finish = False
clock = time.Clock()
FPS = 60'''


'''
Import-ы

class Player и GameSprite
спрайты

цикл While
'''