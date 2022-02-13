####
import pygame
import sys
import os


class StartWindow:
    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    def draw(screen):
        font = pygame.font.Font(None, 24)
        text = font.render("Play", True, (100, 255, 100))
        text1 = font.render("Choose a world", True, (100, 255, 100))
        text2 = font.render("Rating", True, (100, 255, 100))
        screen.blit(text, (380, 100))
        pygame.draw.rect(screen, (0, 255, 0), (339, 99,
                                               120, 20), 1)
        screen.blit(text1, (339, 140))
        pygame.draw.rect(screen, (0, 255, 0), (339, 139,
                                               120, 20), 1)
        screen.blit(text2, (370, 180))
        pygame.draw.rect(screen, (0, 255, 0), (339, 179,
                                               120, 20), 1)

    def buttons(running):
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if pygame.mouse.get_pos()[0] >= 340 and pygame.mouse.get_pos()[1] >= 100:
                        if pygame.mouse.get_pos()[0] <= 460 and pygame.mouse.get_pos()[1] <= 120:
                            print('Play')
                        if pygame.mouse.get_pos()[0] >= 340 and pygame.mouse.get_pos()[1] >= 120:
                            if pygame.mouse.get_pos()[0] <= 460 and pygame.mouse.get_pos()[1] <= 180:
                                print('Choose a world')
                        if pygame.mouse.get_pos()[0] >= 340 and pygame.mouse.get_pos()[1] >= 180:
                            if pygame.mouse.get_pos()[0] <= 460 and pygame.mouse.get_pos()[1] <= 200:
                                print('Rating')
            pygame.display.flip()
        pygame.quit()

    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Snake')
    image = load_image("snake.jpg")
    image1 = pygame.transform.scale(image, (800, 400))
    screen.blit(image1, (0, 0))
    pygame.draw.rect(screen, (76, 187, 23), (340, 100, 120, 20))
    pygame.draw.rect(screen, (76, 187, 23), (340, 140, 120, 20))
    pygame.draw.rect(screen, (76, 187, 23), (340, 180, 120, 20))
    running = True
    draw(screen)
    buttons(running)
