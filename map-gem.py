import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty


kivy.require('1.11.1')


class EntryScreen(GridLayout):

    def to_newuser(self):
        main_app.screen_manager.current = 'New Account'
        # yes

    def to_userlogin(self):
        main_app.screen_manager.current = 'User Login'

    def to_mainmenu(self):
        main_app.screen_manager.current = 'Main Screen'


class UserLogin(GridLayout):
    name1 = ObjectProperty(None)
    password1 = ObjectProperty(None)

    def to_mainmenu(self):
        # the print function is a test. deleat it after
        # concept for ids and vars is understood.
        print(f'Name: {self.name1.text}, password: {self.password1.text}')
        main_app.screen_manager.current = 'Entry Screen'

    def to_login(self):
        main_app.screen_manager.current = 'Login Screen'


class NewAccount(GridLayout):
    def to_mainmenu(self):
        main_app.screen_manager.current = 'Main Screen'


class MainScreen(GridLayout):
    pass


class MapGem(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.entry_screen = EntryScreen()
        screen = Screen(name='Entry Screen')
        screen.add_widget(self.entry_screen)
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
