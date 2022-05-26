import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))
bg_img = pg.image.load('resources/backgrounds/background.png')
bg_img = pg.transform.scale(bg_img,(640,480))

all_sprites = pg.sprite.Group()

def main():
    clock = pg.time.Clock()
    image = pg.image.load('resources/creatures/other/cursorNORM.png')
    image = pg.transform.scale(image, (100, 100))
    player_rect = image.get_rect(topleft=(200, 200))
    # This pygame.Rect has the dimensions of the screen and
    # is used to clamp the player_rect to this area.
    screen_rect = screen.get_rect()
    speed = 7.5

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]:
            player_rect.y -= speed
        if pressed[pg.K_DOWN]:
            player_rect.y += speed
        if pressed[pg.K_LEFT]:
            player_rect.x -= speed
        if pressed[pg.K_RIGHT]:
            player_rect.x += speed
        if pressed[pg.MOUSEBUTTONUP]:
            image = pg.image.load('resources/creatures/other/cursorCLICK.png')
        # Clamp the rect to the dimensions of the screen_rect.
        player_rect.clamp_ip(screen_rect)
        bg_img = pg.image.load('resources/backgrounds/background.png')
        bg_img = pg.transform.scale(bg_img, (640, 480))
        screen.blit(bg_img, (0, 0))
        screen.blit(image, player_rect)

        #Update
        all_sprites.update()

        #Draw/render
        pg.display.flip()
        all_sprites.draw(screen)
        clock.tick(60)


if __name__ == '__main__':
    main()
    pg.quit()