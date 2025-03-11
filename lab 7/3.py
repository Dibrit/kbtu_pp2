import pygame

pygame.init()
c = pygame.display.set_mode(600, 700)
pygame.display.set_caption("ball")
x, y = 300, 350
f = True
while f:
    c.fill(255, 255, 255)
    pygame.draw.circle(c, (255, 0, 0), (x, y), 25)
    pygame.display.flip() 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            f = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT and x - 25 - 20 >= 0:
                x -= 20
            elif i.key == pygame.K_RIGHT and x + 25 + 20 <= 600:
                x += 20
            elif i.key == pygame.K_UP and y - 25 - 20 >= 0:
                y -= 20
            elif i.key == pygame.K_DOWN and y + 25 + 20 <= 700:
                y += 20

pygame.quit()
