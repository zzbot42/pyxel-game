import pyxel
from engine import *
#pyxel.image(0).load(0, 0, "filename.pyxres")

SKY_COLOR = 0
PLAYER_COLOR = 11
FLOOR_COLOR = 12


class App:
    def __init__(self):
        pyxel.init(400, 300, title="Platformer", quit_key=pyxel.KEY_Q)
        self.floors = [
            Box(0, pyxel.height - 20, pyxel.width, 20, FLOOR_COLOR, filled=True),
            Box(50, pyxel.height - 100, 40, 20, FLOOR_COLOR, filled=True),
            Box(-200, pyxel.height - 20, 30, 25, FLOOR_COLOR, filled=True),
            Box(-400, pyxel.height - 20, 30, 25, FLOOR_COLOR, filled=True),
            Box(-500, pyxel.height - 100, 30, 25, FLOOR_COLOR, filled=True),
            Box(-700, pyxel.height - 150, 30, 25, FLOOR_COLOR, filled=True),
            Box(-850, pyxel.height - 0, 30, 25, FLOOR_COLOR, filled=True),
            Box(-1000, pyxel.height - 20, 30, 25, FLOOR_COLOR, filled=True),
            Box(-1100, pyxel.height - 20, 20, 25, FLOOR_COLOR, filled=True),
            Box(-1300, pyxel.height - 20, 20, 25, FLOOR_COLOR, filled=True),
            Box(-1500, pyxel.height - 20, 20, 25, FLOOR_COLOR, filled=True),
            Box(-1600, pyxel.height - 20, 20, 25, FLOOR_COLOR, filled=True),
            Box(-1700, pyxel.height - 100, 20, 25, FLOOR_COLOR, filled=True),
            Box(-1600, pyxel.height - 180, 20, 25, FLOOR_COLOR, filled=True),
            Box(-1700, pyxel.height - 260, 20, 25, FLOOR_COLOR, filled=True),







        ]
        self.player = Player(
           20,
           20,
           20,
           20,
           PLAYER_COLOR,
           filled=True,
           keys_move_x_pos=[pyxel.KEY_D, pyxel.KEY_RIGHT],
           keys_move_x_neg=[pyxel.KEY_A, pyxel.KEY_LEFT],
           keys_jump=[pyxel.KEY_W, pyxel.KEY_SPACE, pyxel.KEY_UP],
        )
        pyxel.run(self.update, self.draw)

    def update(self):
        pass
        for floor in self.floors:
            self.player.fall(floor.is_colliding_top)
        self.player.inputs()
        pyxel.camera(self.player.x - 190, 10)
 
    def draw(self):
        pyxel.cls(SKY_COLOR)

        for floor in self.floors:
            floor.draw()

        self.player.draw()


App()
