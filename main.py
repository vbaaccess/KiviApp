import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

import random

kivy.require('2.0.0')   # 1.9.0


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self, dice_size):
        self.random_label.text = str(random.randint(1, dice_size))


class RollDice(App):

    def build(self):
        self.title = 'Roll Dice'

        root = MyRoot()

        return root


if __name__ == '__main__':
    RollDiceApp = RollDice()
    RollDiceApp.run()
