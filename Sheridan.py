import pygame, random

# if __name__ == '__main__':
pygame.init()
# try:
a, n = map(int, input().split())
screen = pygame.display.set_mode((a, a))

while pygame.event.wait().type != pygame.QUIT:
    side = a // n
    for i in range(n * n):
        row = i // n
        col = i % n
        rect = (col * side, row * side, side, side)
        # if row % 2 and not col % 2 or not row % 2 and col % 2:
        if row % 2 ^ col % 2:
            pygame.draw.rect(screen, 'white', rect)

    # for i in range(0, n):
    #     for j in range(0, n):
    #         if i + j < 2:
    #             pygame.draw.rect(screen, pygame.Color('white'), (i * a, j * a, (i + 1) * a, (j + 1) * a))
    #             pygame.display.flip()

# except Exception:
#     print('Неправильный формат ввода')
