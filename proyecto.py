from manim import *

class RectangleWithBalls(Scene):
    def construct(self):
        # Crear el rectángulo
        rectangle = Rectangle(width=6, height=4)
        rectangle.set_stroke(color=BLUE, width=4)
        rectangle.set_fill(color=WHITE, opacity=0.5)
        
        # Crear las bolas amarillas dentro del rectángulo
        balls = VGroup()
        positions = [
            LEFT + UP, RIGHT + UP, LEFT + DOWN, RIGHT + DOWN, ORIGIN
        ]  # Coordenadas relativas para las bolas
        
        for pos in positions:
            ball = Circle(radius=0.3, color=YELLOW, fill_opacity=1)
            ball.move_to(pos)
            balls.add(ball)
        
        # Añadir el rectángulo y las bolas a la escena
        self.play(Create(rectangle))
        self.play(FadeIn(balls))
        self.wait(2)