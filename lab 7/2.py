import pygame
import os

pygame.init()

s = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music")
mf = "music"  
d = [f for f in os.listdir(mf)]
n = len(d)
j = 0
def play():
    pygame.mixer.music.load(os.path.join(mf, d[j]))
    pygame.mixer.music.play()
p = True
f = True
play()
while f:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            f = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                if p:
                    pygame.mixer.music.pause()
                    p = False
                else:
                    p.mixer.music.unpause()
                    p = True

            elif i.key == pygame.K_s:
                     pygame.mixer.music.stop()

            elif i.key == pygame.K_a:
                j = (j + 1) % n
                play()

            elif i.key == pygame.K_b: 
                j = (j - 1) % n
                play()

pygame.quit()
                    
