import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
    #加载飞船图像并获取其外接矩形
        original_image = pygame.image.load('images/ship.bmp')
        
        scale = 0.05
        width = int(original_image.get_width() * scale)
        height = int(original_image.get_height() * scale)
        self.image = pygame.transform.scale(original_image, (width, height))

        self.rect = self.image.get_rect()
        
    # 对于每艘新飞船， 都将其放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        
    #在飞船的属性x中储存一个浮点数
        self.x = float(self.rect.x)
        
    #移动标志，飞船一开始不移动
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
    
        self.rect.x = self.x
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)