import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


kivy.require('1.11.1')


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Init method runs gridlayout init.
        self.add_widget(Label(text='New User'))
        self.add_widget(Label(text='Login'))
        self.add_widget(Label(text='Skip Login'))


class MapGem(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MapGem().run()
