


import pygame

pygame.init()
display = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Drawing")
clock = pygame.time.Clock()
 
loop = True
radius = 10
while loop:

    try:
        # pygame.mouse.set_visible(False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    radius += 1
                if event.key == pygame.K_DOWN:
                    radius -= 1
               
    
        mouseX, mouseY = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1,0,0):
            # pygame.draw.circle(display, 'red', (mouseX, mouseY, 10, 10))
            pygame.draw.circle(display, (200, 0, 0), (mouseX, mouseY), radius)
        pygame.display.update()

        clock.tick(10000)


    except Exception as e:
        print(e)
        pygame.quit()
        
pygame.quit()
