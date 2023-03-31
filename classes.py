import pygame
from data import*
import random

class Classes(pygame.Rect):
    def __init__(self,x,y,width,height, image,step):
        super().__init__(x,y,width,height)
        self.image = image[0]
        self.step = step
        self.image_list = image
        self.image_move = 0

    def move_images(self):
        self.image = self.image_list[self.image_move // 10]
        self.image_move += 1
        if self.image_move == 20:
            self.image_move = 0


class Hero(Classes):
    def __init__(self,x, y, width, height, image,step):
        super().__init__(x, y, width, height,image,step)
        self.move = {"UP": False, "DOWN": False, "RIGHT": False, "LEFT": False}
        self.bullets = list()
        self.hp = 3
        self.points = 0
        self.bullet_counter = 0
        self.all_points = 0
        self.gun = 0

    def damage(self):
        if self.colliderect(Bot()):
            self.hp -= 1
            if self.hp == 0:
                game = False


    def hero_move(self):
        if self.move["UP"] and self.y > 0:
            self.y -= self.step
        elif self.move["DOWN"] and self.y < setting["HEIGHT"] - 75:
            self.y += self.step
        elif self.move["RIGHT"] and self.x < setting["WIDTH"] - 50:
            self.x += self.step
        elif self.move["LEFT"] and self.x > 0:
            self.x -= self.step     
        #if self.image_move == 0 or self.image_move == 10:
        #    self.image = self.image_list[self.image_move // 10]     
        #if self.image_move == 20:
        #    self.image_move = 0


class Bot(Classes):
    def __init__(self, x ,y ,width , height,image,step):
        super().__init__(x, y, width, height, image, step)
        self.make_shot = True


    def bot_move(self,find_bot, hero):
        self.y += self.step
        self.move_images()
        if self.y >= setting["HEIGHT"] + self.height:
            bot_list.remove(find_bot)
        if self.colliderect(hero):
            hero.hp -= 1
            bot_list.remove(find_bot)

class Boss(Classes):
    def __init__(self, x, y, width, height, step, image): #visiability):
        super().__init__(x, y, width, height, image, step)
        self.hp = 10
        #self.visiability = visiability

    def boss_move(self):
        if self.y < 200:
            self.y += self.step
        elif self.x < 100 or self.x > setting_boss["WIDTH"] - 100 - setting_boss["WIDTH"]:
            self.step *= -1 
        else:
            self.x += self.step

class Buff(pygame.Rect):
    def __init__(self, x, y, image,width = 50, height = 50, buff = None):
        super().__init__(x, y, width, height)
        self.buff = buff
        self.image = image
        self.step = 1
    def buff_move(self, find_buff):
        self.y += self.step
        if self.y >= setting["WIDTH"]:
            buff_list.remove(find_buff)


class Shot(pygame.Rect):
    def __init__(self, x , y, height, width, image, step, bot = None):
        super().__init__(x, y, height,width)
        self.image = image
        self.step = step
        self.bot = bot

    def move_bullet(self, hero, boss, find_bullet, who_shot = False, number_bullet = False):#hero, find_bullets, who_shot, bot):
        self.y += self.step
        temp_key = False
        if who_shot == "hero":
            for bot in bot_list:
                if self.colliderect(bot):
                    hero.points += 10
                    r = random.randint(1, 100)
                    if 1 <= r <= 20:
                        if r <= 10:
                            buff_list.append(Buff(bot.x, bot.y, image = heal_image, buff = "heal"))
                        elif r >= 10:
                            buff_list.append(Buff(bot.x, bot.y, image = gun_image, buff = "gun"))
                    bot_list.remove(bot)
                    hero.bullets.remove(find_bullet)
                    temp_key = True
            if temp_key:
                pass
            elif self.y < 0:
                hero.bullets.remove(find_bullet)
            elif self.colliderect(boss):
                boss.hp -= 1
                hero.bullets.remove(find_bullet)
        elif who_shot == "bot":
            if self.bot != False:
                if self.colliderect(hero):
                    hero.hp -= 1
                    bot_shot_list.remove(find_bullet)
                    self.bot.make_shot = True
                elif self.y > setting["HEIGHT"]:
                    bot_shot_list.remove(find_bullet)
                    self.bot.make_shot = True  
        elif who_shot == "boss":
            if self.colliderect(hero):
                hero.hp -= 1
                boss_shot_list[number_bullet].remove(find_bullet)
            elif self.y > setting["HEIGHT"]:
                boss_shot_list[number_bullet].remove(find_bullet)

           
        
        
        

        #if not who_shot:
        #    for bot in bot_list:
        #        if self.collidepoint(bot):   
        #            hero.points += 10
        #            bot_list.remove(bot)
        #            hero_bullet.remove(find_bullets)
        #else:
        #    if self.bot != False:
        #        if self.colliderect(hero):
        #            hero.hp -= 1
        #            bot_shot_list.remove(bot)
        #            self.bot.make_shot = True
        #        elif self.y > setting["HEIGHT"]:
        #            self.bot = False
        #            self.bot.make_shot = True
        #    #if self.collidepoint

        #if who_shot == True:
        #    if self.colliderect(hero):
        #        hero.hp -= 1
        #        hero.points += 10
        #        bot_shot_list.remove(bot)
        #        self.bot.make_shot = True 
        #    elif self.y > setting["HEIGHT"]:
        #        self.bot = False
        #        self.bot.make_shot = True
        #    if self.colliderect(bot):
        #        bot_list.remove(bot)
        #        hero.points += 10
        #else:
        #    for bot in bot_list:
        #        if self.collidepoint(bot):
        #            hero.points += 10
        #            bot_list.remove(bot)
        #            hero.bullet.remove(find_bullets)
def text(x, y, text,window, color = (0,0,0), size = 40):
    font = pygame.font.Font(None, size)
    mes = font.render(text, True, color)
    window.blit(mes, (x,y))
       