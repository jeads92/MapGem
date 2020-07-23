import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen


kivy.require('1.11.1')


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Init method runs gridlayout init.
        self.cols = 1

        self.new_user_btn = Button(text='New User')
        self.new_user_btn.bind(on_press=self.to_newuser)
        self.add_widget(self.new_user_btn)

        self.login_btn = Button(text='Login')
        self.login_btn.bind(on_press=self.to_userlogin)
        self.add_widget(self.login_btn)

        self.skip_btn = Button(text='Skip Login')
        self.skip_btn.bind(on_press=self.to_mainmenu)
        self.add_widget(self.skip_btn)

    def to_newuser(self, instance):
        main_app.screen_manager.current = 'New Account'
        # yes

    def to_userlogin(self, instance):
        main_app.screen_manager.current = 'User Login'

    def to_mainmenu(self, instance):
        main_app.screen_manager.current = 'Main Screen'


class UserLogin(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Login to Account'))
        self.add_widget(Label(text=""))

        self.add_widget(Label(text='Username'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password'))
        self.password = TextInput(multiline=False,
                                  password=True)
        self.add_widget(self.password)


class NewAccount(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Create New Account'))
        self.add_widget(Label(text=""))

        self.add_widget(Label(text="Username"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password"))
        self.password = TextInput(multiline=False,
                                  password=True)
        self.add_widget(self.password)


class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        # Need to display the username in the topright corner
        self.new_map = Button(text='Create New Maps')
        self.add_widget(self.new_map)

        self.view_maps = Button(text='View Maps')
        self.add_widget(self.view_maps)

        self.options = Button(text='Options')
        self.add_widget(self.options)


class MapGem(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.loginscreen = LoginScreen()
        screen = Screen(name='Login Screen')
        screen.add_widget(self.loginscreen)
        self.screen_manager.add_widget(screen)

        self.user_login = UserLogin()
        screen = Screen(name='User Login')
        screen.add_widget(self.user_login)
        self.screen_manager.add_widget(screen)

        self.new_account = NewAccount()
        screen = Screen(name='New Account')
        screen.add_widget(self.new_account)
        self.screen_manager.add_widget(screen)

        self.mainscreen = MainScreen()
        screen = Screen(name='Main Screen')
        screen.add_widget(self.mainscreen)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    main_app = MapGem()
    main_app.run()
