from manim import *
from pathlib import Path
import os

FLAGS = "-pqm -v WARNING"
SCENE = "FirstScene"

class FirstScene(Scene):
    def construct(self):
        common_config = {'fill_opacity': 1, 'stroke_width': 0}
        w = Circle(**common_config).set_color(WHITE).scale(3.03)
        b = Circle(**common_config).set_color(BLACK).scale(3)
        w1 = VMobject(**common_config).set_points(b.points[:int(len(b.points)/2)]).set_color(WHITE).rotate(-PI/2, about_point=ORIGIN)
        b2 = b.copy().scale(1/2).shift(UP*3/2).set_color(BLACK)
        w2 = b.copy().scale(1/2).shift(DOWN*3/2).set_color(WHITE)
        b3 = b2.copy().scale(1/4).move_to([0,-3/2,0])
        w3 = w2.copy().scale(1/4).move_to([0,3/2,0])

        
        self.add(w,b,w1,b2,w2,b3,w3)
        # self.add(b2,w2)


# This makes it easier to run on vscode. Just hit the play button
if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS} {SCENE}")