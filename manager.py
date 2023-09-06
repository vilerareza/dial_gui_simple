import os
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.metrics import dp
from dialbox import DialBox

Builder.load_file('manager.kv')

class Manager(BoxLayout):

    dial_box = ObjectProperty()

    def stop(self):
        pass