from pygame import *
 
#  класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    #    self.size_x = size_x
    #    self.size_y = size_y

 
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
 
#  класс-наследник для игроков 
class Player(GameSprite):
    #  управляется стрелками
    def update_one(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed 
    #  управляется клавишами W, S
    def update_two(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    # отрисовка
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



 
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")
background = (200, 255, 255)
clock = time.Clock()

# Герои игровой сцены
player_one = Player('stick.png', 20, win_height - 100, 22, 98, 10)
player_two = Player('stick.png', 630, win_height - 100, 22, 98, 10)
ball = Player('ball_for_pin.png',40 , 20, 64, 64, 10)
game_over = transform.scale(image.load("game_over.png"), (365, 365))

# Дополнительные параметры
game = True
finish = False
clock = time.Clock()
FPS = 100
speed_x = 3
speed_y = 3



#---------Цикл игры--------- 
while game:
    window.fill(background)
    for e in event.get():
        if e.type == QUIT:
           game = False


    # Запуск спрайтов
    if finish != True:
        player_one.update_two()
        player_two.update_one()
        player_one.reset() 
        player_two.reset()
        ball.reset()

    # Физика мяча
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.y < 0 or ball.rect.y > 450:
        speed_y *= -1
    if ball.rect.colliderect(player_one.rect):
        speed_x *= -1
    if ball.rect.colliderect(player_two.rect):
        speed_x *= -1
    if ball.rect.x > 630 or ball.rect.x < 20:
        finish = True
        window.blit(game_over,(150, 50))

    
    display.update()
    clock.tick(FPS)
