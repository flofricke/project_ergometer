from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.core.window import Window

Window.size = (800, 480)
Window.borderless = True

import time
import random
import kwad

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

#class

class ImageButton(ButtonBehavior, Image):
    pass

class MainScreen(Screen):
    pass

class SportScreen(Screen):
    pass

class SettingScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    kwad.attach()

root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    MainScreen:
    SportScreen:
    SettingScreen:

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'horizontal'
        padding: 100
        ImageButton:
            source: 'fahrrad.png'
            allow_stretch: False
            keep_ratio: True
            on_press: app.root.current = 'sport'
        ImageButton:
            source: 'tech_einstellungen.png'
            allow_stretch: False
            keep_ratio: True
            on_press: app.root.current = 'setting'

<SportScreen>:
    name: 'sport'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Action'
            font_size: 30
        ImageButton:
            source: 'close_ph.png'
            allow_stretch: False
            keep_ratio: True
            on_press: app.root.current = 'main'
            a: self.show_area('r')

<SettingScreen>:
    name: 'setting'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Einstellungen'
            font_size: 30
        ImageButton:
            source: 'close_ph.png'
            allow_stretch: False
            keep_ratio: True
            on_press: app.root.current = 'main'

''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()
