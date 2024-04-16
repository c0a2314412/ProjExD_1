import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2=pg.transform.flip(bg_img,True,False)#7-1
    tori=pg.image.load("fig/3.png")#2
    tori=pg.transform.flip(tori,True,False)#2
    x=0#6
    tmr = 0
    tori_rct=tori.get_rect()#8-1
    tori_rct.center=300,200#8-2
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%3199#6 #7-2
        screen.blit(bg_img2,[-x+1600,0])#7-1
        screen.blit(bg_img, [-x, 0])#6
        screen.blit(bg_img,[-x+3200,0])#7-2
        tori_rct.move_ip((-1,0))#e1
        key_lst = pg.key.get_pressed()#8-3
        if key_lst[pg.K_UP]:#8-4
            tori_rct.move_ip((0,-1))#8-4
        if key_lst[pg.K_DOWN]:#8-4
            tori_rct.move_ip((0,1))#8-4
        if key_lst[pg.K_RIGHT]:#8-4
            tori_rct.move_ip((2,0))#8-4 #e1 
        if key_lst[pg.K_LEFT]:#8-4
            tori_rct.move_ip((-1,0))#8-4
        screen.blit(tori,tori_rct)#4 #8-5 #e1
        pg.display.update()
        tmr += 1        
        clock.tick(200)#5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()