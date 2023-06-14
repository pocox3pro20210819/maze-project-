from pygame import*

window = display.set_mode((700, 500))
display.set_caption("Maze")

background = transform.scale(image.load("джунглі_1.jpg"), (700, 500))
background_2 = transform.scale(image.load("джунглі_2.jpg"), (700, 500))
background_3 = transform.scale(image.load("джунглі_3.jpg"), (700, 500))
background_4 = transform.scale(image.load("джунглі_4.jpg"), (700, 500))
background_5 = transform.scale(image.load("джунглі_5.jpg"), (700, 500))
background_6 = transform.scale(image.load("чорний фон.jpg"), (700, 500))

font.init()
font = font.Font(None, 100)
win_font = font.render('YOU WIN', True, (255, 215, 0))
game_font = font.render('GAME OVER', True, (200, 50, 50))
lose_font = font.render('YOU LOSE', True, (255, 215, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= 5
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += 5
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += 5

class Enemy(GameSprite):
    left_fd = 'right'
    def update(self):
        if self.rect.x <= 480:
            self.left_fd = "right"
            self.image = transform.flip(self.image, True, False)
        if self.rect.x >= 650:
            self.left_fd = "left"
            self.image = transform.flip(self.image, True, False)
        if self.left_fd == "left":
            self.rect.x -= 3
        if self.left_fd == "right":
            self.rect.x += 3

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__() 
        self.color_1 = color_1 
        self.color_2 = color_2    
        self.color_3 = color_3   
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

game = True
game_2 = False
game_3 = False
game_4 = False
game_5 = False
game_6 = False

finish = False

player = Player("player.png", 60, 100, 2)


enemy = Enemy("enemy.png", 500, 330, 1)
enemy_2 = Enemy("enemy.png", 500, 150, 2)

gold = GameSprite("win_1.png", 640, 440, 0)
gold_2 = GameSprite("win_2.png", 40, 440, 0)
gold_3 = GameSprite("win_3.png", 50, 40, 0)
gold_4 = GameSprite("win_4.png", 640, 40, 0)
gold_5 = GameSprite("win_5.png", 640, 440, 0)

w_1_all1 = Wall(51, 51, 255, 100, 100, 10, 400)
w_1_all2 = Wall(51, 51, 255, 200, 0, 10, 400)
w_1_all3 = Wall(51, 51, 255, 300, 100, 10, 400)
w_1_all4 = Wall(51, 51, 255, 300, 200, 345, 10)

w_2_all1 = Wall(51, 51, 255, 100, 0, 10, 250)
w_2_all2 = Wall(51, 51, 255, 100, 250, 310, 10)
w_2_all3 = Wall(51, 51, 255, 400, 0, 10, 250)
w_2_all4 = Wall(51, 51, 255, 0, 340, 650, 10)
w_2_all5 = Wall(51, 51, 255, 510, 60, 10, 280)
w_2_all6 = Wall(51, 51, 255, 590, 230, 110, 10)

w_3_all1 = Wall(51, 51, 255, 0, 400, 490, 10)
w_3_all2 = Wall(51, 51, 255, 480, 240, 10, 160)
w_3_all3 = Wall(51, 51, 255, 330, 240, 300, 10)
w_3_all4 = Wall(51, 51, 255, 250, 140, 450, 10)
w_3_all5 = Wall(51, 51, 255, 250, 140, 10, 180)
w_3_all6 = Wall(51, 51, 255, 50, 320, 210, 10)

w_4_all1 = Wall(51, 51, 255, 0, 410, 340, 10)
w_4_all2 = Wall(51, 51, 255, 480, 0, 10, 250)
w_4_all3 = Wall(51, 51, 255, 100, 310, 600, 10)
w_4_all4 = Wall(51, 51, 255, 80, 0, 10, 210)
w_4_all5 = Wall(51, 51, 255, 170, 80, 10, 240)
w_4_all6 = Wall(51, 51, 255, 260, 0, 10, 230)
w_4_all7 = Wall(51, 51, 255, 350, 80, 10, 230)
w_4_all8 = Wall(51, 51, 255, 430, 130, 190, 10)

w_5_all1 = Wall(51, 51, 255, 100, 170, 10, 370)
w_5_all2 = Wall(51, 51, 255, 200, 50, 10, 290)
w_5_all3 = Wall(51, 51, 255, 300, 150, 10, 280)
w_5_all4 = Wall(51, 51, 255, 100, 420, 210, 10)
w_5_all5 = Wall(51, 51, 255, 50, 50, 260, 10)
w_5_all6 = Wall(51, 51, 255, 300, 150, 160, 10)
w_5_all7 = Wall(51, 51, 255, 460, 150, 10, 300)
w_5_all8 = Wall(51, 51, 255, 380, 80, 10, 70)
w_5_all9 = Wall(51, 51, 255, 460, 60, 240, 10)
w_5_all10 = Wall(51, 51, 255, 460, 220, 160, 10)
w_5_all11 = Wall(51, 51, 255, 650, 310, 50, 10)
w_5_all12 = Wall(51, 51, 255, 460, 380, 100, 10)

clock = time.Clock()

player.rect.x = 30
player.rect.y = 450

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if finish != True:
        window.blit(background, (0, 0))
        player.reset()
        player.update()
        gold.reset()
        w_1_all1.reset()
        w_1_all2.reset()
        w_1_all3.reset()
        w_1_all4.reset()
    if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w_1_all1) or sprite.collide_rect(player, w_1_all2) or sprite.collide_rect(player, w_1_all3) or sprite.collide_rect(player, w_1_all4):
        finish = True
        window.blit(game_font, (160, 200))
        window.blit(lose_font, (180, 300))
        

    if sprite.collide_rect(player, gold):
        game = False
        game_2 = True
        
    clock.tick(60)
    display.update()
        
player.rect.x = 10
player.rect.y = 50
        

while game_2:
    for e in event.get():
        if e.type == QUIT:
            game_2 = False
    if finish != True:
        window.blit(background_2, (0, 0))
        player.reset()
        player.update()
        gold_2.reset()
        w_2_all1.reset()
        w_2_all2.reset()
        w_2_all3.reset()
        w_2_all4.reset()
        w_2_all5.reset()
        w_2_all6.reset()
    if sprite.collide_rect(player, gold_2):
        game_3 = True
        game_2 = False
        
    if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w_2_all1) or sprite.collide_rect(player, w_2_all2) or sprite.collide_rect(player, w_2_all3) or sprite.collide_rect(player, w_2_all4) or sprite.collide_rect(player, w_2_all5) or sprite.collide_rect(player, w_2_all6):
        finish = True
        window.blit(game_font, (160, 200))
        window.blit(lose_font, (180, 300))
      
    clock.tick(60)
    display.update()

player.rect.x = 30
player.rect.y = 450

while game_3:
    for e in event.get():
        if e.type == QUIT:
            game_3 = False
    if finish != True:
        window.blit(background_3, (0, 0))
        player.reset()
        player.update()
        enemy.reset()
        enemy.update()
        gold_3.reset()
        w_3_all1.reset()
        w_3_all2.reset()
        w_3_all3.reset()
        w_3_all4.reset()
        w_3_all5.reset()
        w_3_all6.reset()
    if sprite.collide_rect(player, gold_3):
        game_4 = True
        game_3 = False
        
    if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w_3_all1) or sprite.collide_rect(player, w_3_all2) or sprite.collide_rect(player, w_3_all3) or sprite.collide_rect(player, w_3_all4) or sprite.collide_rect(player, w_3_all5) or sprite.collide_rect(player, w_3_all6):
        finish = True
        window.blit(game_font, (160, 200))
        window.blit(lose_font, (180, 300))
        
    clock.tick(60)
    display.update()

player.rect.x = 50
player.rect.y = 460

while game_4:
    for e in event.get():
        if e.type == QUIT:
            game_4 = False
    if finish != True:
        window.blit(background_4, (0, 0))
        player.reset()
        player.update()
        enemy_2.reset()
        enemy_2.update()
        gold_4.reset()
        w_4_all1.reset()
        w_4_all2.reset()
        w_4_all3.reset()
        w_4_all4.reset()
        w_4_all5.reset()
        w_4_all6.reset()
        w_4_all7.reset()
        w_4_all8.reset()

    if sprite.collide_rect(player, gold_4):
        game_5= True
        game_4 = False
        
    if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w_4_all1) or sprite.collide_rect(player, w_4_all2) or sprite.collide_rect(player, w_4_all3)  or sprite.collide_rect(player, w_4_all4) or sprite.collide_rect(player, w_4_all5) or sprite.collide_rect(player, w_4_all6) or sprite.collide_rect(player, w_4_all7) or sprite.collide_rect(player, w_4_all8):
        finish = True
        window.blit(game_font, (160, 200))
        window.blit(lose_font, (180, 300))
        
    clock.tick(60)
    display.update()

player.rect.x = 35
player.rect.y = 100

while game_5:
    for e in event.get():
        
        if e.type == QUIT:
            game_5 = False
    if finish != True:
        window.blit(background_5, (0, 0))
        player.reset()
        player.update()
        enemy.reset()
        enemy.update()
        enemy_2.reset()
        enemy_2.update()
        gold_5.reset()
        w_5_all1.reset()
        w_5_all2.reset()
        w_5_all3.reset()
        w_5_all4.reset()
        w_5_all5.reset()
        w_5_all6.reset()
        w_5_all7.reset()
        w_5_all8.reset()
        w_5_all9.reset()
        w_5_all10.reset()
        w_5_all11.reset()
        w_5_all12.reset()
    if sprite.collide_rect(player, gold_5):
        finish = True
        window.blit(game_font, (160, 200))
        window.blit(win_font, (180, 300))
        
        
    if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w_5_all1) or sprite.collide_rect(player, w_5_all2) or sprite.collide_rect(player, w_5_all3) or sprite.collide_rect(player, w_5_all4) or sprite.collide_rect(player, w_5_all5) or sprite.collide_rect(player, w_5_all6) or sprite.collide_rect(player, w_5_all7) or sprite.collide_rect(player, w_5_all8) or sprite.collide_rect(player, w_5_all9) or sprite.collide_rect(player, w_5_all10) or sprite.collide_rect(player, w_5_all11) or sprite.collide_rect(player, w_5_all12):
        finish = True
        window.blit(game_font, (160, 200))
        window.blit(lose_font, (180, 300))
        
    clock.tick(60)
    display.update()