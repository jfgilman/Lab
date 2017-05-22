"""Trying to start learning python for reals."""
import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 175, 0)

display_width = 800
display_height = 600

block_size = 10

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)


def snake(snake_list):
    """Draw the snake."""
    for XnY in snake_list:
        pygame.draw.rect(gameDisplay, green,
                         [XnY[0], XnY[1], block_size, block_size])


def text_objects(text, color):
    """Set up text."""
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color):
    """Send text to the screen."""
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    """Loop through the game."""
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0
    snake_list = []
    snake_length = 1
    randAppleX = round(random.randrange(0, display_width - block_size)/10)*10
    randAppleY = round(random.randrange(0, display_height - block_size)/10)*10
    while not gameExit:

        while gameOver:
            gameDisplay.fill(white)
            message_to_screen("Gameover, C to play again, Q to Quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0

        if (lead_x >= display_width or
                lead_x < 0 or lead_y >= display_height or lead_y < 0):
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red,
                         [randAppleX, randAppleY, block_size, block_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for eachSeg in snake_list[:-1]:
            if eachSeg == snake_head:
                gameOver = True
        snake(snake_list)

        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            snake_length += 1
            randAppleX = round(random.randrange(0, display_width - block_size)/10)*10
            randAppleY = round(random.randrange(0, display_height - block_size)/10)*10

        clock.tick(10)

    pygame.quit()
    quit()


gameLoop()
