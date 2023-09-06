from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.texture import Texture
from kivy.core.image import Image as CoreImage
import math


Builder.load_file('dialbox.kv')


class DialBox(BoxLayout):

    manager = ObjectProperty(None)
    dial_image = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_image_touch_move(self, *args):
        if args[0].collide_point(*args[1].pos):

            if args[0] == self.dial_image:
                # Close button pressed. Change button appearance
                #print (self.dial_image.center_x, self.dial_image.center_y)
                #print (*args[1].pos)
                x, y = args[1].pos
                delta_x = self.dial_image.center_x - x
                delta_y = self.dial_image.center_y - y
                theta = math.atan2(delta_y, delta_x) #*(180/math.pi)
                if theta < 0:
                    theta = theta + 2*math.pi
                theta = theta*(180/math.pi) - 180
                print (theta)
                self.dial_image.angle = theta


    def on_image_release(self, *args):
        if args[0].collide_point(*args[1].pos):

            if args[0] == self.dial_image:
                # Close button pressed. Change button appearance
                print (self.dial_image.center_x, self.dial_image.center_y)
            
            