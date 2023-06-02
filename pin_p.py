from pygame import *
 
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
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
    def update_one(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed 

    def update_two(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

 
 
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")
background = (200, 255, 255)
clock = time.Clock()
window.fill(background)

player_one = Player('bamboo-stick.png', 20, win_height - 100, 50, 100, 10)
player_two = Player('bamboo-stick.png', 630, win_height - 100, 50, 100, 10)

game = True
finish = False
clock = time.Clock()
FPS = 100


   

 
while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    if finish != True:
         
        player_one.update_one()
        player_one.reset()
        player_two.update_two()
        player_two.reset()




    display.update()
    clock.tick(FPS)
