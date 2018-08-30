from tkinter import *
from tkinter import messagebox
from time import time
import os
import math
from random import randint
from ball import Ball
from input import Input
from sound import Sound
from text import Text
os.system('xset r off')
radian = lambda x: x * math.pi / 180


def main_loop():
    global param, count_balls
    canvas.delete('all')
    param += 1
    count_balls = len(list(filter(lambda x: x.exist, balls)))

    make_fountain()
    playing_fountain_sound()

    fall_balls()
    update_balls()
    is_outWindow()

    draw_balls()
    flashing_text()
    if text.exist:
        text.draw()
    canvas.create_rectangle(0, canvas_h - 20, canvas_w, canvas_h - 40 + (count_balls / max_balls * 20), fill='#00f', outline='#09f')
    canvas.create_rectangle(0, canvas_h, canvas_w, canvas_h - 20, fill='#999')
    canvas.create_rectangle((canvas_w / 2) - 30, canvas_h - 20, (canvas_w / 2) + 30, canvas_h - 70, fill='#999')
    restore_text()
    canvas.after(fps, main_loop)


def make_balls(pos):
    length = randint(50, 110) / 10
    random = radian(randint(-950, -850)) / 10
    for b in balls:
        if not b.exist:
            b.set(pos, canvas_h, 2, '#00f')
            b.vy = math.sin(random) * length
            b.vx = math.cos(random) * length * randint(80, 120) / 100
            break


def draw_balls():
    for b in balls:
        if b.exist:
            b.draw(canvas)


def update_balls():
    for b in balls:
        if b.exist:
            b.update()


def fall_balls():
    for b in balls:
        if b.exist:
            b.vy += 0.1
            b.x += b.vx


def is_outWindow():
    for b in balls:
        if b.exist:
            b.outOfwindow()


def playing_fountain_sound():
    if input_keys.space:
        sound.play()
    else:
        sound.stop()


def flashing_text():
    color = math.floor(255 - abs(200 * math.sin(radian(param % 360))))
    text.color = '#{:02x}{:02x}{:02x}'.format(color, color, color)


def make_fountain():
    if input_keys.space:
        [make_balls(canvas_w / 2) for _ in range(8)]
        text.exist = False


def restore_text():
    if count_balls == 0:
        text.exist = True


def show_credit():
    messagebox.showinfo('Credit', '素材提供\n\n効果音ラボ様\nhttps://soundeffect-lab.info/')


#  フレームの宣言？
root = Tk()
f0 = Frame(root)
root.title('Healing fountain')

#  基礎パラメーター
fps = 1000 // 60
param = 0


#  canvasの設定
canvas = Canvas(root, width=1000, height=600, bg='#333')
canvas.pack()
canvas_w = canvas.winfo_reqwidth()
canvas_h = canvas.winfo_reqheight()

#  canvasで使う変数
balls = [Ball(canvas) for _ in range(1700)]
sound = Sound('waterfall-small2.mp3')
text = Text(canvas)
text.set(canvas_w / 2, canvas_h / 1.5, 'Push space key', '#fff', 30)
text.exist = False
input_keys = Input(root)

max_balls = len(balls)
count_balls = 0

#  canvasをループ
main_loop()

#  ボタンの配置
Button(f0, text='クレジット', bg='#fff', command=show_credit).pack(side=LEFT)
Button(f0, text='EXIT', bg='#fff', command=exit).pack()
root.bind_all('q', lambda x: root.quit())
f0.pack()

root.mainloop()

os.system('xset r on')
