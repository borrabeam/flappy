import tkinter as tk

from gamelib import Sprite, GameApp, Text

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500

UPDATE_DELAY = 33
GRAVITY = 2.5
# STARTING_VELOCITY = -30
JUMP_VELOCITY = -20
PILLAR_SPEED = 20

class Dot(Sprite):
    def init_element(self):
        # self.vy = -30
        self.vy = -30
        self.is_started = False


    def update(self):
        # self.y += self.vy
        # self.vy += GRAVITY
        if self.is_started:
            self.y += self.vy
            self.vy += GRAVITY


    def start(self):
        self.is_started = True
    

    def jump(self):
        self.vy = JUMP_VELOCITY

class FlappyGame(GameApp):
    def create_sprites(self):
        self.dot = Dot(self, 'images/dot.png', CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
        self.elements.append(self.dot)
        

        self.pillar_pair = PillarPair(self, 'images/pillar-pair.pgitng', CANVAS_WIDTH, CANVAS_HEIGHT // 2)
        self.elements.append(self.pillar_pair)

    def init_game(self):
        self.create_sprites()
        self.is_started = False

    def pre_update(self):
        pass

    def post_update(self):
        pass

    def on_key_pressed(self, event):
        if event.char == " ":
            self.dot.start()
            self.dot.jump()

class PillarPair(Sprite):
    def update(self):
        self.x -= PILLAR_SPEED

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Banana Game")
 
    # do not allow window resizing
    root.resizable(False, False)
    app = FlappyGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
