from pygame import*

window = display.set_mode((700,500))#создаем окно 700 на 500
display.set_caption("Ping pong")#создаем название окна
window.fill((227, 1, 254))#залить окно цветом

FPS = 45
timer = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))#отобразить фон картинку в окне

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()#список состояния всех клавиш клавиатуры

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 330:#опускаемся вниз если по Y меньше 420
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()#список состояния всех клавиш клавиатуры

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 330:#опускаемся вниз если по Y меньше 420
            self.rect.y += self.speed
player_left = Player('racket.png', 35, 250, 35, 170, 5)
player_right = Player('racket.png', 650, 250, 35, 170, 5)
tenis_ball = GameSprite('tenis_ball.png', 370, 200, 45, 45, 5)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((227, 1, 254))
        player_left.update_l()
        player_right.update_r()
        tenis_ball.rect.y += 3
        tenis_ball.rect.x += 3

        if sprite.collide_rect(player_left, tenis_ball) or sprite.collide_rect(player_right, tenis_ball):
            tenis_ball.rect.y *= -1 
            tenis_ball.rect.x *= -1  
        player_left.reset()
        player_right.reset()
        tenis_ball.reset()

    display.update()
    timer.tick(FPS)
