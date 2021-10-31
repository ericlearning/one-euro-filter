import time
import arcade
import numpy as np
from filter import OneEuro

class Demo(arcade.Window):
    def __init__(self):
        super().__init__(1000, 1000, 'one-euro-demo')
        self.f = OneEuro(1, 0.005, 1)
        self.coords = np.array([self.width/2, self.height/2])
        arcade.set_background_color(arcade.color.WHITE)

    def on_mouse_motion(self, x, y, dx, dy):
        self.coords[0] = x
        self.coords[1] = y

    def on_draw(self):
        noisy_coords = self.coords + np.random.randn(2) * 10
        denoised_coords = self.f.filter(noisy_coords, time.time())

        arcade.start_render()
        arcade.draw_circle_outline(
            noisy_coords[0],
            noisy_coords[1],
            20, arcade.color.BLUE, 3)
        arcade.draw_circle_outline(
            denoised_coords[0],
            denoised_coords[1],
            10, arcade.color.RED, 3)

Demo()
arcade.run()