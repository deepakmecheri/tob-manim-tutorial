from manim import *
from pathlib import Path
import os

FLAGS = "-pqm -v WARNING"
SCENE = "FirstScene"

class FirstScene(Scene):
    def construct(self):
        text = Text("Hello World")
        self.play(Write(text))
        self.wait()


# This makes it easier to run on vscode. Just hit the play button
if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} {FLAGS} {SCENE}")