import pygame

class Font:
    def __init__(self, text, x, y):
        # Initialize text, x, y attributes and the font renderer
        self.text = text
        self.x = x
        self.y = y
        self.fontrender = pygame.font.Font("./font.ttf", 60)  # Loads a font file with size 60
        self.text_surface = self.fontrender.render(self.text, True, (0, 0, 0))
        self.rect = self.text_surface.get_rect(topleft=(self.x, self.y))  # Set the position of the text
        print(self.rect)

    def render(self,screen):
        # Render the text and draw it on the screen at (x, y)
        screen.blit(self.text_surface, (self.x, self.y))

    def is_clicked(self, mouse_pos):
        # Check if the mouse click is inside the rect of the text
        if self.rect.collidepoint(mouse_pos):
            return True
        return False
    
    
    def clear_text(self):
        self.text= ""
        self.text_surface = self.fontrender.render(self.text, True, (0, 0, 0))

# Create an instance of the Font class with the text you want to display
# Text = Font  # Adjusted for proper centering

