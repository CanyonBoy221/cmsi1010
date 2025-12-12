import pygame
import random
import requests
from datetime import datetime
import os

pygame.init()

WIDTH, HEIGHT = 800, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (135, 206, 235)

GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_WIDTH = 80
PIPE_GAP = 150
PIPE_SPEED = -5


class Bird:
    def __init__(self):
        self.x = WIDTH // 4
        self.y = HEIGHT // 2
        self.radius = 10
        self.velocity = 0
        self.alive = True

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.alive = False

    def draw(self, surface):
        pygame.draw.circle(
            surface, YELLOW, (int(self.x), int(self.y)), self.radius)

    def collides_with(self, pipe):
        if self.x + self.radius >= pipe.x and self.x - self.radius <= pipe.x + PIPE_WIDTH:
            if self.y - self.radius <= pipe.top or self.y + self.radius >= pipe.bottom:
                return True
        return False


class Pipe:
    def __init__(self, x):
        self.x = x
        self.top = random.randint(50, HEIGHT - PIPE_GAP - 50)
        self.bottom = self.top + PIPE_GAP
        self.passed = False

    def update(self):
        self.x += PIPE_SPEED

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN, (self.x, 0, PIPE_WIDTH, self.top))
        pygame.draw.rect(surface, GREEN, (self.x, self.bottom,
                         PIPE_WIDTH, HEIGHT - self.bottom))
        pygame.draw.rect(surface, (0, 200, 0), (self.x - 5,
                         self.top - 10, PIPE_WIDTH + 10, 10))
        pygame.draw.rect(surface, (0, 200, 0), (self.x - 5,
                         self.bottom, PIPE_WIDTH + 10, 10))

    def is_off_screen(self):
        return self.x + PIPE_WIDTH < 0


MESSAGES = [
    "womp womp",
    "Nice try, keep practicing, maybe one day you will be good enough!",
    "You flew too close to the sun, and got burnt like toast",
    "The pipes changed you",
    "You are so buns",
    "UNNNNNFORTUNATE",
    "Watch yo jet bro watch yo jet",
    "*Worlds Smallest Violin plays*",
    "is ts pmo?",
]


def get_random_message():
    return random.choice(MESSAGES)


def save_score(score):
    with open("scores.txt", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - Score: {score}\n")


def game():
    bird = Bird()
    pipes = [Pipe(WIDTH + PIPE_WIDTH)]
    score = 0
    game_over = False
    quote = ""

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not game_over:
                    bird.flap()
                if event.key == pygame.K_SPACE and game_over:
                    return game()

        if not game_over:
            bird.update()

            for pipe in pipes:
                pipe.update()

                if bird.collides_with(pipe):
                    game_over = True
                    quote = get_random_message()
                    save_score(score)

                if pipe.x + PIPE_WIDTH < bird.x and not pipe.passed:
                    pipe.passed = True
                    score += 1

            pipes = [p for p in pipes if not p.is_off_screen()]

            if len(pipes) == 0 or pipes[-1].x < WIDTH - 200:
                pipes.append(Pipe(WIDTH + PIPE_WIDTH))

        screen.fill(SKY_BLUE)

        for pipe in pipes:
            pipe.draw(screen)

        bird.draw(screen)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        if game_over:
            game_over_text = large_font.render("GAME OVER", True, RED)
            screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 100))

            final_score_text = font.render(
                f"Final Score: {score}", True, WHITE)
            screen.blit(final_score_text, (WIDTH // 2 - 80, HEIGHT // 2))

            quote_lines = quote.split(" ")
            words_per_line = 8
            for i, line_start in enumerate(range(0, len(quote_lines), words_per_line)):
                line = " ".join(
                    quote_lines[line_start:line_start + words_per_line])
                quote_text = font.render(line, True, YELLOW)
                screen.blit(quote_text, (20, HEIGHT // 2 + 60 + i * 30))

            restart_text = font.render("Press SPACE to restart", True, WHITE)
            screen.blit(restart_text, (WIDTH // 2 - 130, HEIGHT - 50))

        pygame.display.flip()


if __name__ == "__main__":
    game()
    pygame.quit()
