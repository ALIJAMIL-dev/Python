import manim as mn

class CircleToSquare(mn.Scene):
    def construct(self):
        circle = mn.Circle()  # Create a circle
        square = mn.Square()  # Create a square

        self.play(mn.Create(circle))  # Animate the creation of the circle
        self.play(mn.Transform(circle, square))  # Transform the circle into a square
        self.play(mn.FadeOut(square))  # Fade out the square