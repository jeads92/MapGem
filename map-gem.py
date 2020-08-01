import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen


kivy.require('1.11.1')


class LoginScreen(GridLayout):

    def to_newuser(self):
        main_app.screen_manager.current = 'New Account'
        # yes

    def to_userlogin(self):
        main_app.screen_manager.current = 'User Login'

    def to_mainmenu(self):
        main_app.screen_manager.current = 'Main Screen'


class UserLogin(GridLayout):
    pass


class NewAccount(GridLayout):
    pass


class MainScreen(GridLayout):
    pass


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
