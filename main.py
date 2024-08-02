import pygame as pg

print('Setup Start')
pg.init()
screen = pg.display.set_mode((800, 600))
print('Setup End')


print('Game Loop Start')
while True:
    # check for all events

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
