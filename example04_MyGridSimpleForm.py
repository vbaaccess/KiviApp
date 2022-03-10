from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class MyGrid(GridLayout):

    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def __init__(self, **kwargs):
        pass

    def pressed(self, instance):
        name = self.name.text
        last = self.lastName.text
        email = self.email.text

        print("Name:", name, "Last Name:", last, "Email:", email)
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


MyApp().run()
