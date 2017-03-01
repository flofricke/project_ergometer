from kivy.core.window import Window

Window.size = (800, 480)
Window.borderless = True

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label

from kivy.graphics import Rectangle, Color
from kivy.uix.screenmanager import Screen, ScreenManager

class mainMenu(Screen):
    pass

class trainingMenu(Screen):
    pass

class FahrradApp(App):

    def build(self):
        #Grundlayout fuer Hauptbildschirm

        #Header
        header = BoxLayout(size_hint=(1,None), height=50)
        header.add_widget(Label(text="Platzhalter oben", id="oben"))

        infobar = BoxLayout(size_hint=(None,1), width=100)
        infobar.add_widget(Label(text="Info"))

        mitte = BoxLayout()
        mitte.add_widget(Label(text="Hier Widget"))
        mitte.add_widget(infobar)

        footer = BoxLayout(size_hint=(1,None), height=50)
        footer.add_widget(Label(text="Platzhalter unten"))

        #Container fuer alle einzelnen Teile, Header, Footer, Mitte mit Seite
        root = BoxLayout(orientation='vertical')
        root.add_widget(header)
        root.add_widget(mitte)
        root.add_widget(footer)

        return root

FahrradApp().run()
