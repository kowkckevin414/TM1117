import pygame


class InputBox:
   
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('dodgerblue2')
        self.text = text
        self.txt_surface = pygame.font.SysFont('Comic Sans MS', 32).render(self.text, True, self.color)
        self.active = False

    def update(self,event):
        if event.key == pygame.K_BACKSPACE:
            self.text =  self.text[:-1]
        elif event.key == pygame.K_RETURN:
            pass
        else:
            if self.txt_surface.get_width() < self.rect.w-32:
                self.text += event.unicode
        self.txt_surface = pygame.font.SysFont('Comic Sans MS', 32).render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+2, self.rect.y+2))
        pygame.draw.rect(screen, self.color, self.rect,2)



