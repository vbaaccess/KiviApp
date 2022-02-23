import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.0.0')   # 1.9.0


class KiviInfo(App):

    def build(self):
        # return Label(text=self.name)
        return BoxLayout()


if __name__ == '__main__':
    kiviInfo = KiviInfo()
    kiviInfo.run()
