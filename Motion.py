import pygame


class MotionCircle:
    def __init__(self, event, key_w, key_s, key_a, key_d, speed, pos):
        self.key_w = key_w
        self.key_s = key_s
        self.key_a = key_a
        self.key_d = key_d
        self.event = event
        self.speed = speed
        self.pos_x = pos[0]
        self.pos_y = pos[1]

    def recalculation(self):
        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_w:
                self.key_w = 1
        elif self.event.type == pygame.KEYUP:
            if self.event.key == pygame.K_w:
                self.key_w = 0

        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_s:
                self.key_s = 1
        elif self.event.type == pygame.KEYUP:
            if self.event.key == pygame.K_s:
                self.key_s = 0

        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_a:
                self.key_a = 1
        elif self.event.type == pygame.KEYUP:
            if self.event.key == pygame.K_a:
                self.key_a = 0

        if self.event.type == pygame.KEYDOWN:
            if self.event.key == pygame.K_d:
                self.key_d = 1
        elif self.event.type == pygame.KEYUP:
            if self.event.key == pygame.K_d:
                self.key_d = 0

        if self.key_w:
            self.pos_y -= self.speed
        if self.key_s:
            self.pos_y += self.speed
        if self.key_a:
            self.pos_x -= self.speed
        if self.key_d:
            self.pos_x += self.speed

        return self.pos_x, self.pos_y, self.key_w, self.key_s, self.key_a, self.key_d
