import pygame, pyautogui
WIDTH, HEIGHT= pyautogui.size()
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket")
space=pygame.image.load("pictures/space.png")
city=pygame.transform.scale(pygame.image.load("pictures/city.png"), (WIDTH, HEIGHT))
cop=pygame.transform.scale(pygame.image.load("pictures/cop.png"), (300, 300))
rob=pygame.transform.scale(pygame.image.load("pictures/robber.png"), (400, 400))
fence=pygame.transform.scale(pygame.image.load("pictures\electricfence.webp"), (20, HEIGHT))
cblt=pygame.transform.scale(pygame.image.load("pictures/bulletc.png"), (80, 30))
rblt=pygame.transform.scale(pygame.image.load("pictures/bulletr.png"), (80, 30))
cop=pygame.transform.flip(cop, True, False)
border=pygame.Rect(WIDTH//2-10, 0, 20, HEIGHT)
def draw(cr, rc, cbullets, rbullets, chealth, rhealth):
    screen.blit(city, (0,0))
    #pygame.draw.rect(screen, "red", rc)
    screen.blit(cop, (cr.x, cr.y))
    screen.blit(rob, (rc.x-70, rc.y-70))
    screen.blit(fence, (border.x, border.y))
    for i in cbullets:
        screen.blit(cblt, (i.x, i.y))
    for i in rbullets:
        screen.blit(rblt, (i.x, i.y))

def handlemovement(cr, rc, keys):
    if keys[pygame.K_a] and cr.x>0:
        cr.x-=10
    if keys[pygame.K_d] and cr.x+cr.width<border.x:
        cr.x+=10
    if keys[pygame.K_w] and cr.y>0:
        cr.y-=10
    if keys[pygame.K_s] and cr.y+cr.height<HEIGHT:
        cr.y+=10
    if keys[pygame.K_LEFT] and rc.x>border.x+border.width:
        rc.x-=10
    if keys[pygame.K_RIGHT] and rc.x+rc.width<WIDTH:
        rc.x+=10
    if keys[pygame.K_UP] and rc.y>0:
        rc.y-=10
    if keys[pygame.K_DOWN] and rc.y+rc.height<HEIGHT:
        rc.y+=10


def handlebullets(cr, rc, cbullets, rbullets, chealth, rhealth):
    for i in cbullets:
        i.x+=10
        if i.x>WIDTH:
            cbullets.remove(i)
        if i.colliderect(rc):
            cbullets.remove(i)
            rhealth-=1

    for i in rbullets:
        i.x-=10
        if i.x<0:
            rbullets.remove(i)
        if i.colliderect(cr):
            rbullets.remove(i)
            chealth-=1
            continue
        for j in cbullets:
            if i.colliderect(j):
                cbullets.remove(j)
                rbullets.remove(i)
                break

    return chealth, rhealth

def main():
    cr=pygame.Rect(300, HEIGHT//2, 300, 300)
    rc=pygame.Rect(WIDTH-300, HEIGHT//2, 250, 280)
    cbullets=[]
    rbullets=[]
    chealth=10
    rhealth=10
    while True:
        draw(cr, rc, cbullets, rbullets, chealth, rhealth)
        chealth, rhealth=handlebullets(cr, rc, cbullets, rbullets, chealth, rhealth)
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_LSHIFT:
                    b=pygame.Rect(cr.x+cr.width-80, cr.y+50, 80, 30)
                    cbullets.append(b)
                if i.key==pygame.K_RSHIFT:
                    g=pygame.Rect(rc.x-50, rc.y, 80, 30)
                    rbullets.append(g)
        keys=pygame.key.get_pressed()
        handlemovement(cr, rc, keys)
        pygame.display.update()
main()