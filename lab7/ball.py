import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ball_radius = 25
ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
ball_speed = 20
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - ball_speed, ball_radius)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + ball_speed, SCREEN_HEIGHT - ball_radius)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - ball_speed, ball_radius)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + ball_speed, SCREEN_WIDTH - ball_radius)
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
