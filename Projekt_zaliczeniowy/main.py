from settings import *
from tetris import Tetris, Text
import sys
import pathlib

class StartScreen:
    def __init__(self, app):
        self.app = app
        self.font = pg.font.Font(FONT_PATH, 36)
        self.title_text = self.font.render("Tetris", True, 'white')
        self.start_text = self.font.render("Press Enter to Start", True, 'white')
        self.title_rect = self.title_text.get_rect(center=(WIN_W // 2, WIN_H // 2 - 50))
        self.start_rect = self.start_text.get_rect(center=(WIN_W // 2, WIN_H // 2 + 50))

    def draw(self):
        self.app.screen.fill(BG_COLOR)
        self.app.screen.blit(self.title_text, self.title_rect)
        self.app.screen.blit(self.start_text, self.start_rect)
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                self.app.start_game()

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.images = self.load_images()
        self.tetris = None
        self.text = None
        self.start_screen = StartScreen(self)
        self.current_screen = 'start'
        self.paused = False

    def load_images(self):
        files = [item for item in pathlib.Path(SPRITE_DIR_PATH).rglob('*.png') if item.is_file()]
        images = [pg.image.load(file).convert_alpha() for file in files]
        images = [pg.transform.scale(image, (TILE_SIZE, TILE_SIZE)) for image in images]
        return images

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.anim_trigger = False
        self.fast_anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    def start_game(self):
        self.tetris = Tetris(self)
        self.text = Text(self)
        self.current_screen = 'game'

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            pg.time.set_timer(self.user_event, 0)
            pg.time.set_timer(self.fast_user_event, 0)
        else:
            pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
            pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    def update(self):
        if not self.paused:
            if self.current_screen == 'game':
                self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        if self.current_screen == 'start':
            self.start_screen.draw()
        elif self.current_screen == 'game':
            self.screen.fill(color=BG_COLOR)
            self.screen.fill(color=FIELD_COLOR, rect=(0,0, *FIELD_RES))
            self.tetris.draw()
            self.text.draw()
            if self.paused:
                pass
            pg.display.flip()

    def check_events(self):
        if self.current_screen == 'start':
            self.start_screen.check_events()
        elif self.current_screen == 'game':
            self.anim_trigger = False
            self.fast_anim_trigger = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.toggle_pause()
                    elif not self.paused:
                        self.tetris.control(pressed_key=event.key)
                elif event.type == self.user_event:
                    self.anim_trigger = True
                elif event.type == self.fast_user_event:
                    self.fast_anim_trigger = True
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()