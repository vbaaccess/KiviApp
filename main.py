import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import random

kivy.require('2.0.0')   # 1.9.0


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(1, 6))


class RollDice(App):

    def build(self):
        self.title = 'Roll Dice'
        # return Label(text=self.name)
        return MyRoot()


if __name__ == '__main__':
    RollDiceApp = RollDice()
    RollDiceApp.run()
