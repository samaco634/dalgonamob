import pygame

pygame.init()

screen = pygame.display.set_mode((500,300))
#pygame.display.set_caption("myRCcar")
#pygame.key.set_repeat(10)

# --- mainloop / event loop ---
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # <-- closing button was pressed
            running = False # it will exit `while` loop
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            print(event)
        

pygame.quit()
