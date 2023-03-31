import pygame
import os

setting = {
    "HEIGHT": 720,
    "WIDTH": 1280,
    "FPS": 60,
    "NAME_GAME": "STAR WARS.exe"
}

abs_path = os.path.abspath(__file__+ "/..") + "\\image\\"

setting_boss = {
    "HEIGHT": 200,
    "WIDTH": 500
}
buff_list = list()

hero_image1 = pygame.image.load("image\\chort1.png")
hero_image2 = pygame.image.load("image\\chort2.png")
bot_image1 = pygame.image.load("image\\twicher.png")
hero_bullet = pygame.image.load("image\\hero_bullet.png")
image = ["image\\chort1.png", "image\\chort2.png"]
bot_image2 = pygame.image.load("image\\twicher2.png")
bullet_image = pygame.image.load("image\\hero_bullet.png")
boss_image = pygame.transform.scale(pygame.image.load("image\\boss.png"), (setting_boss["WIDTH"], setting_boss["HEIGHT"]))
heal_image = pygame.image.load("image\\heal.png")
gun_image = pygame.image.load('image\\gun.png')


image_hero = [hero_image1, hero_image2]
image_bot = list()
bot_list_image = [bot_image1, bot_image2]
boss_image_list = [boss_image]


bot_list = list()
time_list = list()
bot_shot_list = list()
boss_shot_list = list()
