import pygame
import random
def get_safe_spawn(x, y, min_distance=120):
    while True:
        spawn_x = random.randint(50, 450)
        spawn_y = random.randint(50, 450)
        dist_sq = (spawn_x - x) ** 2 + (spawn_y - y) ** 2
        if dist_sq >= min_distance ** 2:
            return spawn_x, spawn_y

class Zombie:
    def __init__(self, x, y):
        self.x, self.y = get_safe_spawn(x, y)
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.rect.center = self.x, self.y

    def gotoplayer(self, x, y):
        self.rect.center = self.x, self.y
        self.x = max(10, min(self.x, 490))
        self.y = max(10, min(self.y, 490))
        if self.x < x:
            self.x += 2
        elif self.x > x:
            self.x -= 2
        if self.y < y:
            self.y += 2
            return
        if self.y > y:
            self.y -= 2

    def drawme(self, screen):
        pygame.draw.circle(screen, (60, 150, 0), (self.x, self.y), 20)


class ScaredZombie:
    def __init__(self, x, y):
        self.x, self.y = get_safe_spawn(x, y)
        self.rect = pygame.Rect(0, 0, 30, 30)
        self.rect.center = self.x, self.y

    def gotoplayer(self, x, y):
        self.rect.center = self.x, self.y
        self.x = max(50, min(self.x, 450))
        self.y = max(50, min(self.y, 450))
        if self.x < x:
            self.x -= 1
        elif self.x > x:
            self.x += 1
        if self.y < y:
            self.y -= 1
            return
        if self.y > y:
            self.y += 1

    def drawme(self, screen):
        pygame.draw.circle(screen, (60, 150, 60), (self.x, self.y), 20)


class Bigboy:
    def __init__(self, x, y):
        fontbigboy = pygame.font.Font(None, 10)
        self.x, self.y = get_safe_spawn(x, y)
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.rect.center = self.x, self.y

    def gotoplayer(self, x, y):
        self.rect.center = self.x, self.y
        self.x = max(10, min(self.x, 490))
        self.y = max(10, min(self.y, 490))
        if self.x < x:
            self.x += 1
        elif self.x > x:
            self.x -= 1
        if self.y < y:
            self.y += 1
            return
        if self.y > y:
            self.y -= 1

    def drawme(self, screen):
        yad = self.y - 20
        fontbigboy = pygame.font.Font(None, 20)
        pygame.draw.circle(screen, (90, 150, 0), (self.x, self.y), 50)
        titleincornerj = fontbigboy.render('Jim', True, (255, 255, 255))
        screen.blit(titleincornerj, (self.x, yad))


class BrokenBubb:
    def __init__(self, x, y):
        self.x, self.y = get_safe_spawn(x, y)
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.rect.center = self.x, self.y

    def gotoplayer(self, x, y):
        self.rect.center = self.x, self.y
        self.x = max(10, min(self.x, 490))
        self.y = max(10, min(self.y, 490))
        if self.x < x:
            self.x += 2
        elif self.x > x:
            self.x -= 2
        if self.y < y:
            self.y += 2
            return
        if self.y > y:
            self.y -= 2

    def drawme(self, screen):
        pygame.draw.circle(screen, (90, 10, 60), (self.x, self.y), 20)


class Pixi:
    def __init__(self, x, y):
        self.x, self.y = get_safe_spawn(x, y)
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.rect.center = self.x, self.y
        self.seteleportime = pygame.time.get_ticks()
        self.teleporttime = 2000

    def gotoplayer(self, x, y):
        current_time = pygame.time.get_ticks()
        if current_time - self.seteleportime >= self.teleporttime:
            self.x, self.y = get_safe_spawn(x, y)
            self.seteleportime = current_time
        self.rect.center = self.x, self.y
        self.x = max(10, min(self.x, 490))
        self.y = max(10, min(self.y, 490))
        if self.x < x:
            self.x += 2
        elif self.x > x:
            self.x -= 2
        if self.y < y:
            self.y += 2
            return
        if self.y > y:
            self.y -= 2

    def drawme(self, screen):
       pygame.draw.circle(screen, (150, 0, 150), (self.x, self.y), 20)


