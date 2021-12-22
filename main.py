import pygame

pygame.init()

class DrawInformations():
    GREEEN = 31, 160, 70

    BACKGROUND_COLOR = GREEEN

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.windows = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Dutch Pub")

def draw(draw_info):
    draw_info.windows.fill(draw_info.BACKGROUND_COLOR)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    draw_info = DrawInformations(1500, 1000)    # resolution

    while run:
        clock.tick(60)      # gmae speed (fps)

        draw(draw_info)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    pygame.quit()

if __name__ == "__main__":
    main()