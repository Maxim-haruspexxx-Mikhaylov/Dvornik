import pygame


class MotionCircle:
    def __init__(self, screen, color, pos, width, speed, event, last_event_keydown, last_scancode):
        self.screen = screen
        self.color = color
        self.pos = pos
        self.width = width
        self.speed = speed
        self.event = event
        self.last_event_keydown = last_event_keydown
        self.last_scancode = last_scancode
        self.scancode_forth = 26
        self.scancode_back = 22
        self.scancode_right = 7
        self.scancode_left = 4

    def recalculation(self):
        if self.last_event_keydown and self.event.type != pygame.KEYUP:
            if self.last_scancode == self.scancode_forth:
                self.pos = (self.pos[0], self.pos[1] - self.speed)
            if self.last_scancode == self.scancode_back:
                self.pos = (self.pos[0], self.pos[1] + self.speed)
            if self.last_scancode == self.scancode_right:
                self.pos = (self.pos[0] + self.speed, self.pos[1])
            if self.last_scancode == self.scancode_left:
                self.pos = (self.pos[0] - self.speed, self.pos[1])
        elif self.event.type != pygame.KEYUP:
            if self.event.type == pygame.KEYDOWN and self.event.scancode == self.scancode_forth:
                self.pos = (self.pos[0], self.pos[1] - self.speed)
            if self.event.type == pygame.KEYDOWN and self.event.scancode == self.scancode_back:
                self.pos = (self.pos[0], self.pos[1] + self.speed)
            if self.event.type == pygame.KEYDOWN and self.event.scancode == self.scancode_right:
                self.pos = (self.pos[0] + self.speed, self.pos[1])
            if self.event.type == pygame.KEYDOWN and self.event.scancode == self.scancode_left:
                self.pos = (self.pos[0] - self.speed, self.pos[1])
        return self.pos

    def move(self):
        pygame.display.flip()
        pygame.draw.circle(self.screen, self.color, self.recalculation(), self.width)







