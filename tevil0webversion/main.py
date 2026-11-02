import pygame
import random
import asyncio  # Added for browser compatibility
from tevil0Enemys import Zombie
from tevil0Enemys import ScaredZombie
from tevil0Enemys import Bigboy
from tevil0Enemys import BrokenBubb
from tevil0Enemys import Pixi

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('T-evil 0')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
fontbigboy = pygame.font.Font(None, 10)

def resetgame():
    global x, y, zombie, scaredzombie, pixi, xb, yb, raduis, facing, bulletmove, score, bigboy, spawnzomb, chanceszom, randozombie, brokenbubb
    x, y = 250, 250
    zombie = Zombie(x, y)
    scaredzombie = ScaredZombie(x, y)
    pixi = Pixi(x, y)
    xb = x
    yb = y
    raduis = 1
    facing = 'north'
    bulletmove = False
    score = 0
    bigboy = Bigboy(x, y)
    spawnzomb = True
    chanceszom = [1, 1, 1, 1, 2, 2, 3, 4, 4, 5]
    randozombie = random.choice(chanceszom)
    brokenbubb = BrokenBubb(x, y)

def randomzombie():
    if randozombie == 1:
        zombie.gotoplayer(x, y)
        zombie.drawme(screen)
        spawnzomb = False
    if randozombie == 2:
        scaredzombie.gotoplayer(x, y)
        scaredzombie.drawme(screen)
        spawnzomb = False
    if randozombie == 3:
        bigboy.gotoplayer(x, y)
        bigboy.drawme(screen)
        spawnzomb = False
    if randozombie == 4:
        brokenbubb.gotoplayer(x, y)
        brokenbubb.drawme(screen)
        spawnzomb = False
    if randozombie == 5:
        pixi.gotoplayer(x, y)
        pixi.drawme(screen)
        spawnzomb = False

# Wrap the execution in an async function for PyScript compatibility
async def main():
    global x, y, zombie, scaredzombie, pixi, xb, yb, raduis, facing, bulletmove, score, bigboy, spawnzomb, chanceszom, randozombie, brokenbubb
    
    running = True
    resetgame()
    player = pygame.Rect(0, 0, raduis * 10, raduis * 10)
    bullet = pygame.Rect(0, 0, raduis * 5, raduis * 5)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_SPACE:
                    continue
                if bulletmove:
                    continue
                xb = x
                yb = y
                bulletface = facing
                bulletmove = True
                
        clock.tick(30)
        screen.fill((20, 40, 25))
        pygame.draw.circle(screen, (100, 50, 50), (x, y), 20)
        x = max(10, min(x, 490))
        y = max(10, min(y, 490))
        randomzombie()
        titleincorner = font.render('T-evil 0', True, (255, 255, 255))
        screen.blit(titleincorner, (10, 10))
        titleincornere = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(titleincornere, (10, 250))
        titleincornerb = font.render('Version 0.5 No Cowboy yet', True, (255, 255, 255))
        screen.blit(titleincornerb, (10, 450))
        titleincornerc = font.render('DevenWebsite', True, (255, 255, 255))
        screen.blit(titleincornerc, (320, 10))
        player.center = x, y
        bullet.center = xb, yb
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            running = False
        if keys[pygame.K_LEFT]:
            x -= 5
            facing = 'west'
        if keys[pygame.K_RIGHT]:
            x += 5
            facing = 'east'
        if keys[pygame.K_UP]:
            y -= 5
            facing = 'north'
        if keys[pygame.K_DOWN]:
            facing = 'south'
            y += 5
        if keys[pygame.K_m]:
            pygame.mixer.music.pause()
        if keys[pygame.K_l]:
            resetgame()
            
        if bulletmove:
            pygame.draw.circle(screen, (200, 200, 0), (xb, yb), 10)
            if bulletface == 'north':
                yb -= 15
                if yb < 0:
                    bulletmove = False
            if bulletface == 'south':
                yb += 15
                if yb > 500:
                    bulletmove = False
            if bulletface == 'west':
                xb -= 15
                if xb < 0:
                    bulletmove = False
            if bulletface == 'east':
                xb += 15
                if xb > 500:
                    bulletmove = False
                    
        if bulletmove and randozombie == 1 and bullet.colliderect(zombie.rect):
            bulletmove = False
            spawnzomb = True
            zombie = Zombie(x, y)
            score += 1
            randozombie = random.choice(chanceszom)
        if bulletmove and randozombie == 2 and bullet.colliderect(scaredzombie.rect):
            bulletmove = False
            spawnzomb = True
            scaredzombie = ScaredZombie(x, y)
            score += 1
            randozombie = random.choice(chanceszom)
        if bulletmove and randozombie == 3 and bullet.colliderect(bigboy.rect):
            bulletmove = False
            spawnzomb = True
            bigboy = Bigboy(x, y)
            score += 2
            randozombie = random.choice(chanceszom)
        if bulletmove and randozombie == 4 and bullet.colliderect(brokenbubb.rect):
            bulletmove = False
            spawnzomb = True
            brokenbubb = BrokenBubb(x, y)
            score += 2
            randozombie = random.choice(chanceszom)
        if bulletmove and randozombie == 5 and bullet.colliderect(pixi.rect):
            bulletmove = False
            spawnzomb = True
            pixi = Pixi(x, y)
            score += 4
            randozombie = random.choice(chanceszom)
            
        if randozombie == 1 and player.colliderect(zombie.rect):
            resetgame()
        elif randozombie == 2 and player.colliderect(scaredzombie.rect):
            resetgame()
        elif randozombie == 3 and player.colliderect(bigboy.rect):
            resetgame()
        elif randozombie == 4 and player.colliderect(brokenbubb.rect):
            resetgame()
        elif randozombie == 5 and player.colliderect(pixi.rect):
            resetgame()
            
        pygame.display.flip()
        
        # Give control back to the browser for a split second to keep it responsive
        await asyncio.sleep(0)
        
    pygame.quit()

# Run the game wrapper
asyncio.run(main())
