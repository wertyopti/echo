import sys
import os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
import pygame
pygame.mixer.init()
pygame.mixer.music.load(resource_path('gta-4-loading-screen-theme.mp3'))
pygame.mixer.music.play()
print('WERTY GAMES COMPANY')
import time
time.sleep(2)
print('present echo(эхо)')
time.sleep(2)
print('developers:wertyopti')
time.sleep(2)
print('thanks deepseek for dark theme in idle')
time.sleep(2)
print('sral v rot exec')
time.sleep(2)
import random
b=0
c=0
def echo2():
    print('через месяц полицейский вошел в храм его ноги перестали его слушаться когда он вошел в храм когда его ноги повели из храма назад он упал и умер но его тело взяли под управление 3 демона теперь он стал демоном')
    print('он пошел к тому самому каньону и его увидел экзарцист и началась битва')
    d = 0
    f = 3
    while True:
        e = random.randint(1, 3)
        print('1-exit demons 2-damage demons 3-destroy demons')
        print(e)
        j = input()
        if (j == 'exit demons' and e == 1) or (j == 'damage demons' and e == 2) or (j == 'destroy demons' and e == 3):
            print('хорош ты нанес урон')
            f -= 1
        else:
            print('не то заклинание')
            d += 1
        if f == 0:
            print('ты уничтожил демонов')
            print('хорошая концовка')
            print('показать экстра? (да нет)')
            l=input()
            if l=='да':
                print('ЭКСТРА:')
                print('следущая игра от этого разроботчика:windows 13 on scratch')
                break
            else:
                break
        elif d == 3:
            print('тебя захватили демоны')
            print('плохая концовка')
            break
print('говори в каньон')
time.sleep(2)
pygame.mixer.music.load(resource_path('Dungeons_Dragons_Po_Tu_Storonu_Stranic_-_Dark_Fantasy_Dungeons_Caves_Ambience._Muzyka_dlya_DnD_A_(SkySound.cc).mp3'))
pygame.mixer.music.play()
while True:
    if b==3:
        print('О ДА Я СТАЛ СИЛЬНЕЕ.Тебя поглотил каньон')
        print('полицейский: 3 дня назад здесь нашли вокруг пиктограмы три человека.По словам экзарциста они прокляли каньон заклинанием close demon.Где то в глубине головы полицейского: ТЫ ДОЛЖЕН СКАЗАТЬ ТРИ РАЗА В КАНЬОН.После этих слов он не управлял своим телом')
        print('средняя концовка')
        break
    elif b==2 and c==0:
        print('ПРОДОЛЖАЙ')
        c+=1
    else:
        a=input()
        if a=='open demon':
            time.sleep(2)
            print('ты освободил каньон от 3 демонов теперь он не проклят теперь ты проклят')
            print('полицейский: 3 дня назад здесь нашли вокруг пиктограмы три человека.По словам экзарциста они прокляли каньон заклинанием close demon.Где то в глубине головы полицейского: ТЫ ДОЛЖЕН СКАЗАТЬ ТРИ РАЗА В КАНЬОН.После этих слов он не управлял своим телом')
            echo2()
            break
        else:
            time.sleep(2)
            print (a)
            b+=1
