from manim import *

class FirstScene(Scene):
    def construct(self):
        text = Text("Hello World")
        self.play(Write(text))
        self.wait()