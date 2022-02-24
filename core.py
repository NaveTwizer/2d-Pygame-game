import pygame


# Rectangle class. Can be improved
class Rectangle:
    def __init__(self, screen, color, left, top, width, height):
        self.screen = screen
        self.color = color
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
    def draw(self):
        draw_rectangle(self.screen, self.color,\
            self.left, self.top, self.width, self.height)
    
# initialize needed stuff, may be more to come on the way!
def initialize():
    pygame.init()
    pygame.mixer.init()

def update_screen():
    pygame.display.update()

# draw rectangle function used in the rectangle class.
def draw_rectangle(screen, color, left, top, width, height):
    pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))

# play music on repeat
def play_music_repeat(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1) #-1 makes it to loop endlessly