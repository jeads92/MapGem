import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
import tile_crusher
from kivy.properties import ListProperty


kivy.require('1.11.1')


class EntryScreen(BoxLayout):
    '''
    The main screen that will let you jump to the map generating screen.
    '''
    def to_editmap(self):
        '''Switch to the map generating portion. '''
        main_app.screen_manager.current = 'Edit Map'


class MyLabel(Label):
    '''
    This is a default class for the label that will be created to represent
    a map tile. This is used in the Edit Map class.
    '''
    bg_color = ListProperty([0, 0, 0, 1])


class EditMap(GridLayout):
    '''
    Edit Map is the screen where the user can generate the map.
    '''
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


class MapGem(App):
    ''' Builds all of the screens as instances. '''
    def build(self):
        self.screen_manager = ScreenManager()

        self.entry_screen = EntryScreen()
        screen = Screen(name='Entry Screen')
        screen.add_widget(self.entry_screen)
        self.screen_manager.add_widget(screen)

        self.edit_map = EditMap()
        screen = Screen(name='Edit Map')
        screen.add_widget(self.edit_map)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    main_app = MapGem()
    main_app.run()
