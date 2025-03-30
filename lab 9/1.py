import pygame,sys,random,time

pygame.init()
fps=60
f=pygame.time.Clock()
c1=(50,168,82)
c2=(189,33,33)
c3=(78,80,210)
c4=(15,15,15)
c5=(240,240,240)
sp=5
sc=0
cc=0
cl=5
win=pygame.display.set_mode((400,600))
p=pygame.Rect(160,520,50,50)
e=pygame.Rect(random.randint(40,360),0,50,50)
c=pygame.Rect(random.randint(40,360),random.randint(40,400),30,30)
cv=random.choice([1,2,3])

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.fill(c5)
    pygame.draw.rect(win,c3,p)
    pygame.draw.rect(win,c2,e)
    pygame.draw.rect(win,c1,c)

    e.move_ip(0,sp)
    if e.top>600:
        sc+=1
        e.top=0
        e.center=(random.randint(40,360),0)
    k=pygame.key.get_pressed()
    if p.left>0 and k[pygame.K_LEFT]: p.move_ip(-5,0)
    if p.right<400 and k[pygame.K_RIGHT]: p.move_ip(5,0)
    if p.top>0 and k[pygame.K_UP]: p.move_ip(0,-5)
    if p.bottom<600 and k[pygame.K_DOWN]: p.move_ip(0,5)

    if p.colliderect(e):
        pygame.quit()
        sys.exit()
    if p.colliderect(c):
        cc+=cv
        c.topleft=(random.randint(40,360),random.randint(40,400))
        cv=random.choice([1,2,3])
        if cc%cl==0:
            sp+=1
    
    pygame.display.update()
    f.tick(fps)