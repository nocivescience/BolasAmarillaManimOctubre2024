from manim import *
import random
import numpy as np

class MovingBallsInRectangle(Scene):
    def construct(self):
        # Crear el rectángulo (contenedor)
        container = Rectangle(width=6, height=4)
        container.set_stroke(color=BLUE, width=4)
        container.set_fill(color=WHITE, opacity=0.1)
        
        # Crear las bolas
        num_balls = 10
        ball_radius = 0.1
        balls = VGroup()
        velocities = []  # Para almacenar las velocidades de las bolas

        # Crear bolas en posiciones aleatorias y con velocidades aleatorias
        for i in range(num_balls):
            x = random.uniform(-3 + ball_radius, 3 - ball_radius)
            y = random.uniform(-2 + ball_radius, 2 - ball_radius)
            color = YELLOW if i != 0 else RED  # La primera bola será roja
            ball = Circle(radius=ball_radius, color=color, fill_opacity=1)
            ball.move_to([x, y, 0])
            balls.add(ball)
            
            # Velocidades aleatorias para cada bola
            vel_x = random.uniform(-1, 1)
            vel_y = random.uniform(-1, 1)
            velocities.append(np.array([vel_x, vel_y, 0]))

        # Añadir el rectángulo y las bolas a la escena
        self.play(Create(container))
        self.play(FadeIn(balls))

        # Crear un trazado para la primera bola (roja)
        trace = TracedPath(balls[0].get_center, stroke_color=RED, stroke_width=1)

        # Simulación de movimiento
        def update_balls(mob, dt):
            for i in range(num_balls):
                ball = balls[i]
                velocity = velocities[i]
                
                # Actualizar posición de la bola
                ball.shift(velocity * dt)
                
                # Obtener la posición actual
                pos = ball.get_center()
                
                # Detectar colisión con las paredes del contenedor (rebote)
                if pos[0] - ball_radius < -3 or pos[0] + ball_radius > 3:
                    velocities[i][0] = -velocities[i][0]  # Invertir velocidad en X
                if pos[1] - ball_radius < -2 or pos[1] + ball_radius > 2:
                    velocities[i][1] = -velocities[i][1]  # Invertir velocidad en Y
                
                # Detectar colisiones entre bolas
                for j in range(i+1, num_balls):
                    other_ball = balls[j]
                    other_pos = other_ball.get_center()
                    distance = np.linalg.norm(pos - other_pos)
                    
                    if distance < 2 * ball_radius:
                        # Intercambiar velocidades (conservación del momentum)
                        velocities[i], velocities[j] = velocities[j], velocities[i]

        # Añadir el trazado a la escena
        self.add(trace)

        # Actualizar las bolas continuamente
        balls.add_updater(update_balls)

        # Mantener la escena por 10 segundos
        self.wait(20)

        # Detener las actualizaciones
        balls.remove_updater(update_balls)
