import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    asteroidfield = AsteroidField()


    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawab in drawable:
            drawab.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for updat in updatable:
            updat.update(dt)
        for asteroid in asteroids:
            if (player.collision_check(asteroid)):
                print("Game over!")
                return
            for shot in shots:
                if (asteroid.collision_check(shot)):
                    shot.kill()
                    asteroid.split()

if __name__ == "__main__":
    main()