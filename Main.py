import pygame
from pygame import Color as color
from random import randint
from Motion import MotionCircle
from Image import GetImage
from Rotation import Rotation


class Window:
    def __init__(self, screen):
        self.x_pos = 1
        self.screen = screen
        self.backgrounds = [('Sportcomplex_lofi.png', (2744, 1832), (0, 0))]

    def draw_headliner(self, pos_x, pos_y):
        screen.fill(color('white'))
        for elem in self.backgrounds:
            background = GetImage(elem[0], elem[1]).load_image()
            screen.blit(background, (elem[2][0] - pos_x, elem[2][1] - pos_y))

#    def draw(self):
#        if self.x_pos > 1024:
#            self.x_pos = 1
#        pygame.draw.circle(self.screen, (255, 0, 0), (self.x_pos, 200), 20)
#        self.x_pos += 1


if __name__ == '__main__':
    pygame.init()
    screen_size = width, height = 1920, 1080
    x_pos = 1
    circle_size = 90
    im_size = 60
    speed_ori = 10
    speed = speed_ori
    speed_cur = 0
    fps = 60
    last_scancode = -1
    last_event_keydown = False
    pos_back = (0, 0)
    last_pos = pos_back
    screen = pygame.display.set_mode(screen_size)
    Window(screen).draw_headliner(pos_back[0], pos_back[1])
    pos_ori = (width / 2 - im_size, height / 2 - im_size)
    key_w = 0
    key_s = 0
    key_a = 0
    key_d = 0
    right = False
    left = False

#    pygame.draw.circle(screen, color('blue'), pos_back, circle_size)

    clock = pygame.time.Clock()
    image = image_ori = GetImage('Dvornik3.png', (im_size, im_size), colorkey=-1).load_image()
    screen.blit(image, (pos_ori[0] - im_size // 2, pos_ori[1] - im_size // 2))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            speed = speed * 2
        if keys[pygame.K_w] and pos_ori[1] - speed > im_size:
            pos_back = (pos_back[0], pos_back[1] - speed)
            image = pygame.transform.rotate(image_ori, 90)
        elif keys[pygame.K_w]:
            pos_back = (pos_back[0], im_size)
            image = pygame.transform.rotate(image_ori, 90)
        if keys[pygame.K_s] and pos_ori[1] + speed < height - im_size:
            pos_back = (pos_back[0], pos_back[1] + speed)
            image = pygame.transform.rotate(image_ori, -90)
        elif keys[pygame.K_s]:
            pos_back = (pos_back[0], height - im_size)
            image = pygame.transform.rotate(image_ori, -90)
        if keys[pygame.K_a] and pos_ori[0] - speed > im_size / 2:
            pos_back = (pos_back[0] - speed, pos_back[1])
            image = pygame.transform.rotate(image_ori, -180)
        elif keys[pygame.K_a]:
            pos_back = (im_size / 2, pos_back[1])
            image = pygame.transform.rotate(image_ori, -180)
        if keys[pygame.K_d] and pos_ori[0] + speed < width - im_size / 2:
            pos_back = (pos_back[0] + speed, pos_back[1])
            image = pygame.transform.rotate(image_ori, 0)
        elif keys[pygame.K_d]:
            pos_back = (width - im_size / 2, pos_back[1])
            image = pygame.transform.rotate(image_ori, 0)
        speed = speed_ori

        Window(screen).draw_headliner(pos_back[0], pos_back[1])
        screen.blit(image, pos_ori)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
