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
        if keys[K_s] and self.rect.y < 330:#опускаемся вниз если по Y меньше 330
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()#список состояния всех клавиш клавиатуры

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 330:#опускаемся вниз если по Y меньше 330
            self.rect.y += self.speed

player_left = Player('racket.png', 35, 250, 35, 170, 5)
player_right = Player('racket.png', 650, 250, 35, 170, 5)
tenis_ball = GameSprite('tenis_ball.png', 400, 200, 45, 45, 5)

game = True
finish = False
speed_X = 3
speed_Y = 3
font.init()
font = font.Font(None, 70)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((227, 1, 254))
        player_left.update_l()
        player_right.update_r()
        tenis_ball.rect.y += speed_X
        tenis_ball.rect.x += speed_Y

        if sprite.collide_rect(player_left, tenis_ball) or sprite.collide_rect(player_right, tenis_ball):
            speed_X *= 1            
            speed_Y *= -1 

        if tenis_ball.rect.y > 455  or tenis_ball.rect.y < 0:
            speed_X *= -1

        if tenis_ball.rect.x < 0:
            lose_1 = font.render('PLAYER1 LOSE!', True, (255, 0, 0))
            window.blit(lose_1, (150, 230))
            finish = True

        if tenis_ball.rect.x > 655:
            lose_2 = font.render('PLAYER2 LOSE!', True, (255, 0, 0))
            window.blit(lose_2, (150, 230))
            finish = True

        player_left.reset()
        player_right.reset()
        tenis_ball.reset()

    display.update()
    timer.tick(FPS)
