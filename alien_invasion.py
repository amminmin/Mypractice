import sys
import pygame
from settings import Settings 
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
             (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._creat_fleet()
        
        self.bg_color = (self.settings.bg_color)
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 侦听键盘和鼠标的事件
            self._check_events()
            self.ship.update()
            self._update_bullets()
            #每次循环时都重绘屏幕
            self._update_screen()
            self.clock.tick(60)
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  
                self._check_keyup_events(event)
        
    def _check_keydown_events(self, event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True  
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        
    def _check_keyup_events(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False  
                               
    def _fire_bullet(self):
        """创建一颗子弹,并将其加入编组bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)                           
          
    def _update_screen(self):
        """更新屏幕上的图像,并切换到新屏幕"""
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()
    
    def _update_bullets(self):
        self.bullets.update()
        #删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _creat_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        
        current_x = alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            self._creat_alien(current_x)
            current_x += 2 * alien_width
    
    def _creat_alien(self, x_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)  
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
