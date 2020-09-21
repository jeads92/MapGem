import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
import tile_crusher
from kivy.properties import ListProperty


kivy.require('1.11.1')


def screen_changer(instance):
    ''' Switches to the screen based off of the screen name.'''
    pass


def label_maker(instance):
    '''Creates a label for the kivy GUI'''
    pass


class EntryScreen(BoxLayout):

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

    def to_tester(self):
        '''switch to testing screen'''
        main_app.screen_manager.current = 'StrMap'


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


class MainScreen(BoxLayout):
    def to_options(self):
        main_app.screen_manager.current = 'Options'

    def to_editmap(self):
        main_app.screen_manager.current = 'Edit Map'

    def to_viewmaps(self):
        main_app.screen_manager.current = 'View Maps'


class MyLabel(Label):
    '''
    This is a default class for the label that will be created to represent
    a map tile. This is used in the Edit Map class.
    '''
    bg_color = ListProperty([0, 0, 0, 1])


class EditMap(GridLayout):
    tile_colors = {'^': [134/255, 205/255, 130/255, 1],
                   '_': [162/255, 73/255, 54/255, 1],
                   '~': [82/255, 178/255, 207/255, 1],
                   '*': [241/255, 227/255, 243/255, 1],
                   '#': [156/255, 173/255, 206/255, 1],
                   '@': [0, 0, 0, 1]}

    map_object = tile_crusher.MapGenerator()
    map_object.gen_fullmap(10, 10)

    def generate_map_tiles(self):
        self.map_object.gen_fullmap(10, 10)
        self.map_layout = self.ids.grid
        self.map_layout.clear_widgets()

        for row in self.map_object.grid:
            for tile in row:
                self.new_label = MyLabel(bg_color=self.tile_colors[tile])
                self.map_layout.add_widget(self.new_label)


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
