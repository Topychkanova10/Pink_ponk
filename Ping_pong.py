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
    def update(self):
        keys = key.get_pressed()#список состояния всех клавиш клавиатуры

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 20)
        bullets.add(bullet)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    timer.tick(FPS)

