from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):

    name = ObjectProperty(None)
    lastName = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        name = self.name.text
        last = self.lastName.text
        email = self.email.text

        print("Name:", name, "Last Name:", last, "Email:", email)
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""


class example04_MyGridSimpleForm(App):
    def build(self):
        self.title = "Examle UI by kvlang"
        return MyGrid()


example04_MyGridSimpleForm().run()
