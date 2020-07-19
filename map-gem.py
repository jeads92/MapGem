import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


kivy.require('1.11.1')


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Init method runs gridlayout init.
        self.cols = 1

        self.new_user_btn = Button(text='New User')
        self.new_user_btn.bind(on_press=self.test)
        self.add_widget(self.new_user_btn)

        self.login_btn = Button(text='Login')
        self.add_widget(self.login_btn)

        self.skip_btn = Button(text='Skip Login')
        self.add_widget(self.skip_btn)

    def test(self, instance):
        # Temporary function to test if bind works
        print('Test has been run')


class MapGem(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MapGem().run()
