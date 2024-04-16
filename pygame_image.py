import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2=pg.image.load("fig/pg_bg.jpg")
    tori=pg.image.load("fig/3.png")#2
    tori=pg.transform.flip(tori,True,False)#2
    x=0
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%800
        screen.blit(bg_img, [-x, 0])#5
        screen.blit(tori,[300,200])#4
        pg.display.update()
        tmr += 1        
        clock.tick(200)#5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()