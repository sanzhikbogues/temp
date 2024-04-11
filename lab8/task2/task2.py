import random

import pygame

pygame.init()
WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (0 ,0 , 127)
FPS = 5
SCORE = 0
LEVEL = 1

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
LOSS_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 20
background_sound = pygame.mixer.Sound("Snake Game - Theme Song.mp3")
background_sound = pygame.mixer.music.load("Snake Game - Theme Song.mp3")
eat_sound = pygame.mixer.Sound("snake-hissing-6092.mp3")
pygame.display.set_caption('Snake')
score_font = pygame.font.SysFont('Verdana', 20)
level_font = pygame.font.SysFont('Verdana', 20)
running = True

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def update(self):
        pygame.draw.rect(
            SCREEN,
            YELLOW,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
class Poison:
    def __init__(self, x, y):
        self.location = Point(x, y)

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def update(self):
        pygame.draw.rect(
            SCREEN,
            GREEN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


class Snake:
    def __init__(self):
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
            Point(WIDTH // BLOCK_SIZE // 2 + 1, HEIGHT // BLOCK_SIZE // 2),
        ]

    def update(self):
        head = self.points[0]

        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.points[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )
    #function that will catch the movement of our snake and checks whether its head out of border 
    #if its head is out of the border then the game will be over 
    def move(self, dx, dy):
        global running
        # global SCORE
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y

        self.points[0].x += dx
        self.points[0].y += dy
        
        head = self.points[0]
        if head.x >= WIDTH // BLOCK_SIZE:
            running = False
        elif head.x < 0:
            running = False
        elif head.y >= HEIGHT // BLOCK_SIZE:
            running = False
        elif head.y < 0:
            running = False
    #function that checks a collision between food and snake
    def check_collision(self, food):
        if self.points[0].x != food.x:
            return False
        if self.points[0].y != food.y:
            return False
        return True
    def check_poison_collision(self, poison):
        if self.points[0].x != poison.x:
            return False
        if self.points[0].y != poison.y:
            return False
        return True
    # def self_collision(self):
    #     global running
    #     for i in self.points(self.points[0], len(self.points)):
    #         if self.points[0].x == i.x or self.points[0].y == i.y:
    #             running = False

#drawing a grid where we play our game
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, (0, y), (WIDTH, y), width=1)

def main():
    global SCORE
    global LEVEL
    global FPS
    global running
    snake = Snake()
    food = Food(5, 5)
    poison = Poison(10, 10)
    dx, dy = 0, 0
    pygame.mixer.music.play(-1)
    while running:
        SCREEN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, +1
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = +1, 0

        snake.move(dx, dy)
        if snake.check_collision(food):
            pygame.mixer.music.pause()
            eat_sound.play()
            eat_sound.stop()
            pygame.mixer.music.unpause()
            SCORE += 1
            # if SCORE % 5 == 0:
            #     LEVEL += 1
            #     # FPS += 3

            snake.points.append(Point(food.x, food.y))
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
        if snake.check_poison_collision(poison):
            SCORE -= 1
            # if SCORE % 5 == 0:
            #     LEVEL += 1
            #     # FPS += 3
            snake.points.remove(snake.points[len(snake.points)-1])
            poison.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            poison.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
        
        score = score_font.render(f" Your score: {SCORE}", True, (0, 0, 0))
        level = level_font.render(f" Level: {LEVEL}", True, (0, 0, 0))

        SCREEN.blit(score, (0, 0))
        SCREEN.blit(level, (20, 20))

        food.update()
        snake.update()
        poison.update()
        draw_grid()
        
        # if running == False:
        #     LOSS_SCREEN.fill(LIGHTBLUE)
        #     score = score_font.render(f" Your score: {SCORE}", True, (WHITE))
        #     LOSS_SCREEN.blit(score, (WIDTH // 2 - 80, HEIGHT // 2))
        #     pygame.time.wait(5000)
        pygame.display.flip()
        clock.tick(FPS)


# if __name__ == '__main__':
main()