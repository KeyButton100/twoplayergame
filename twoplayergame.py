import pygame, pyautogui
WIDTH, HEIGHT= pyautogui.size()
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket")
space=pygame.image.load("pictures/space.png")
city=pygame.transform.scale(pygame.image.load("pictures/city.png"), (WIDTH, HEIGHT))
cop=pygame.transform.scale(pygame.image.load("pictures/cop.png"), (300, 300))
rob=pygame.transform.scale(pygame.image.load("pictures/robber.png"), (300, 300))
cop=pygame.transform.flip(cop, True, False)

def draw(cr, rc):
    screen.blit(city, (0,0))
    screen.blit(cop, (cr.x, cr.y))
    screen.blit(rob, (rc.x, rc.y))

def handlemovement(cr, rc, keys):
    if keys[pygame.k_a]:
        cr.x-=10

def main():
    cr=pygame.Rect(300, HEIGHT//2, 300, 300)
    rc=pygame.Rect(WIDTH-300, HEIGHT//2, 300, 300)
    while True:
        draw(cr, rc)
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                pygame.quit()
        keys=pygame.key.getpressed()
        handlemovement(cr, rc, keys)
        pygame.display.update()
main()