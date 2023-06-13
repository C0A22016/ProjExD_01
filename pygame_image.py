import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    
    kt_img = pg.image.load("ex01/fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)
    
    tmr = 0
    kt_mv = 0
    mv_num = 0.5
    flipFlag = True
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img2,[-tmr+1600, 0])
        screen.blit(pg.transform.rotozoom(kt_img, kt_mv, 1.0), [300, 200])
        pg.display.update()
        tmr += 1
        kt_mv += mv_num
        
        if(kt_mv > 10 or kt_mv < -5):
            mv_num *= -1
        
        if(tmr > 1600):
            tmr = 0
            bg_img = pg.transform.flip(bg_img, flipFlag, False)
            bg_img2 = pg.transform.flip(bg_img, -flipFlag, False)
            flipFlag = -flipFlag 
                   
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()