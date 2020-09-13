import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
import tile_crusher

kivy.require('1.11.1')


def screen_changer(instance):
    ''' Switches to the screen based off of the screen name.'''


class EntryScreen(GridLayout):

    def to_newuser(self):
        ''' Switches to the New Account Screen. '''
        main_app.screen_manager.current = 'New Account'
        # yes

    def to_userlogin(self):
        ''' Switches to the login screen. '''
        main_app.screen_manager.current = 'User Login'

    def to_mainmenu(self):
        ''' Switches to the main screen. '''
        main_app.screen_manager.current = 'Main Screen'


class UserLogin(BoxLayout):
    ''' Allows the user to login to their account and load their data. '''
    name1 = ObjectProperty(None)
    password1 = ObjectProperty(None)

    def to_entryscreen(self):
        main_app.screen_manager.current = 'Entry Screen'

    def to_login(self):
        main_app.screen_manager.current = 'Login Screen'

    def to_mainscreen(self):
        main_app.screen_manager.current = 'Main Screen'


class NewAccount(BoxLayout):
    def to_mainmenu(self):
        main_app.screen_manager.current = 'Main Screen'


class MainScreen(GridLayout):
    def to_options(self):
        main_app.screen_manager.current = 'Options'

    def to_editmap(self):
        main_app.screen_manager.current = 'Edit Map'

    def to_viewmaps(self):
        main_app.screen_manager.current = 'View Maps'


class EditMap(GridLayout):
    map_label = tile_crusher.MapGenerator()
    map_label.gen_fullmap()
    
    


class Options(BoxLayout):
    ''' This screen will have all options the user can edit. '''
    pass


class ViewMaps(BoxLayout):
    ''' This screen allows the user to view, edit, and load their maps. '''
    pass


class MapGem(App):
    ''' Builds all of the screens as instances. '''
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

        self.options = Options()
        screen = Screen(name='Options')
        screen.add_widget(self.options)
        self.screen_manager.add_widget(screen)

        self.edit_map = EditMap()
        screen = Screen(name='Edit Map')
        screen.add_widget(self.edit_map)
        self.screen_manager.add_widget(screen)

        self.view_maps = ViewMaps()
        screen = Screen(name='View Maps')
        screen.add_widget(self.view_maps)
        self.screen_manager.add_widget(screen)


        return self.screen_manager


if __name__ == '__main__':
    main_app = MapGem()
    main_app.run()
