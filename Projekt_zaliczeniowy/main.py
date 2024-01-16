from settings import *
from tetris import Tetris, Text
from datetime import datetime
import sys, pathlib, requests
import string

class StartScreen:
    def __init__(self, app):
        self.app = app
        self.font = pg.font.Font(FONT_PATH, 50)
        self.title_text = self.font.render("Tetris", True, 'white')
        self.font = pg.font.Font(FONT_PATH, 20)
        self.start_text = self.font.render("Press Enter to Start", True, 'white')
        self.scoreboard_text = self.font.render("Press ESC to see Leaderboard", True, 'white')
        self.title_rect = self.title_text.get_rect(center=(WIN_W // 2, WIN_H // 2 - 50))
        self.start_rect = self.start_text.get_rect(center=(WIN_W // 2, WIN_H // 2 + 50))
        self.scoreboard_rect = self.scoreboard_text.get_rect(center=(WIN_W // 2, WIN_H // 2 + 90))

    def draw(self):
        self.app.screen.fill(BG_COLOR)
        self.app.screen.blit(self.title_text, self.title_rect)
        self.app.screen.blit(self.start_text, self.start_rect)
        self.app.screen.blit(self.scoreboard_text, self.scoreboard_rect)
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.app.start_game()
                elif event.key == pg.K_ESCAPE:
                    self.app.current_screen = 'scoreboard'
            elif event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

class PauseOverlay:
    def __init__(self, app):
        self.app = app
        self.overlay_surface = pg.Surface(WIN_RES, pg.SRCALPHA)
        self.overlay_surface.fill((0, 0, 0, 150))
        self.font = pg.font.Font(FONT_PATH, 36)
        self.title_text = self.font.render("Paused", True, 'white')
        self.paused_text = self.font.render("Press ESC to resume", True, 'white')
        self.title_rect = self.title_text.get_rect(center=(WIN_W // 2, WIN_H // 2 - 50))
        self.paused_rect = self.paused_text.get_rect(center=(WIN_W // 2, WIN_H // 2 + 50))

    def draw(self):
        self.app.screen.blit(self.overlay_surface, (0, 0))
        self.app.screen.blit(self.title_text, self.title_rect)
        self.app.screen.blit(self.paused_text, self.paused_rect)
        pg.display.flip()

class GameOver:
    def __init__(self, app):
        self.app = app
        
        self.font = pg.font.Font(FONT_PATH, 70)
        self.title_text = self.font.render("Game Over!", True, 'red')
        self.title_rect = self.title_text.get_rect(center=(WIN_W // 2, WIN_H // 2 - 200))
        
        self.font = pg.font.Font(FONT_PATH, 20)
        self.back_text = self.font.render("Press ESC", True, 'white')
        self.back_text_1 = self.font.render("to go back to menu", True, 'white')
        self.back_rect = self.back_text.get_rect(center=(WIN_W // 2, WIN_H // 2 - 25))
        self.back_rect_1 = self.back_text_1.get_rect(center=(WIN_W // 2, WIN_H // 2))
        
        self.leaderboard_text = self.font.render("Pres Enter", True, 'white')
        self.leaderboard_text_1 = self.font.render("to inseert your score in the leaderboard", True, 'white')
        self.leaderboard_rect = self.leaderboard_text.get_rect(center=(WIN_W // 2, WIN_H // 2 + 75))
        self.leaderboard_rect_1 = self.leaderboard_text_1.get_rect(center=(WIN_W // 2, WIN_H // 2 + 100))

    def draw(self):
        self.app.screen.fill(BG_COLOR)

        self.font = pg.font.Font(FONT_PATH, 50)
        score_text = self.font.render(f"Your score: {self.app.tetris.score}", True, 'yellow')
        score_rect = score_text.get_rect(center=(WIN_W // 2, WIN_H // 2 - 100))

        self.app.screen.blit(self.title_text, self.title_rect)
        self.app.screen.blit(score_text, score_rect)
        self.app.screen.blit(self.back_text, self.back_rect)
        self.app.screen.blit(self.back_text_1, self.back_rect_1)
        self.app.screen.blit(self.leaderboard_text, self.leaderboard_rect)
        self.app.screen.blit(self.leaderboard_text_1, self.leaderboard_rect_1)
        
        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.app.tetris:
                        self.app.tetris.gameover = False
                    self.app.current_screen = 'start'
                elif event.key == pg.K_RETURN:
                    self.app.current_screen = 'scoreboard'
            elif event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

class Scoreboard:
    def __init__(self, app, database_url="https://tetris-ef706-default-rtdb.europe-west1.firebasedatabase.app/"):
        self.app = app
        self.database_url = database_url + "scores"
        self.font = pg.freetype.Font(FONT_PATH)
        self.entering_name = False
        self.player_name = ""

    def load_scores(self):
        response = requests.get(f"{self.database_url}.json")
        scores = response.json()
        return scores or []
    
    def get_top_scores(self, num=10):
        scores = self.load_scores()
        sorted_scores = sorted(scores, key=lambda x: x["score"], reverse=True)
        return sorted_scores[:num]

    def save_scores(self, scores):
        requests.put(f"{self.database_url}.json", json=scores)

    def add_score(self, player_name, score):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_score = {"player_name": player_name, "score": score, "timestamp": timestamp}

        scores = self.load_scores()
        if not scores:
            scores = [new_score]
        else:
            scores.append(new_score)

        self.save_scores(scores)

    def draw(self):
        top_scores = self.get_top_scores()

        self.app.screen.fill(BG_COLOR)
        self.font.render_to(self.app.screen, (50, 50), "Top Scores:", fgcolor='green', size=50)

        for i, score in enumerate(top_scores):
            player_name = score.get("player_name", "Unknown")
            score_value = score.get("score", 0)
            timestamp = score.get("timestamp", "N/A")

            score_text = f"  {i + 1}. {player_name}: {score_value} ({timestamp})"
            self.font.render_to(self.app.screen, (50, 100 + (1 + i) * 25),
                                score_text, fgcolor='gray', size=20)
            
        if(self.app.tetris is not None and self.app.tetris.gameover):
            if not self.entering_name:
                self.font.render_to(self.app.screen, (50, 500), "Press Enter to submit your score.", fgcolor='yellow', size=20)
            else:
                input_text = f"Enter your name: {self.player_name}"
                self.font.render_to(self.app.screen, (50, 500), input_text, fgcolor='yellow', size=20)

        pg.display.flip()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.app.entering_name = False
                    self.app.current_screen = 'start'
                elif event.key == pg.K_RETURN:
                    if(self.app.tetris is not None and self.app.tetris.gameover):
                        if not self.entering_name:
                            self.entering_name = True
                        else:
                            self.add_score(self.player_name, self.app.tetris.score)
                            self.player_name = ""
                            self.entering_name = False
                            self.app.current_screen = 'start'
                elif event.key == pg.K_BACKSPACE and self.entering_name:
                    if len(self.player_name) > 0:
                        self.player_name = self.player_name[:-1]
                elif self.entering_name:
                    if event.unicode.isalnum() or event.unicode in string.punctuation:
                        self.player_name += event.unicode
            elif event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

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
        self.paused_overlay = PauseOverlay(self)
        self.gameover = GameOver(self)
        self.scoreboard = Scoreboard(self)
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
                self.paused_overlay.draw()
            pg.display.flip()
        elif self.current_screen == 'gameover':
            self.gameover.draw()
        else:
            self.scoreboard.draw()

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
        elif self.current_screen == 'gameover':
            self.gameover.check_events()
        else:
            self.scoreboard.check_events()
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()