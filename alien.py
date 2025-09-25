import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        
        original_image = pygame.image.load('images/alien_ship_gray.png')

        scale = 1
        width = int(original_image.get_width() * scale)
        height = int(original_image.get_height() * scale)
        self.image = pygame.transform.scale(original_image, (width, height))

        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
        
        
        
    
    
        
    
    