__author__ = 'jc247746'

# An __init__ method capable of initialising a trip details field
# A build method that sets the window title appropriately, sets the window size to 350 x 700, and defines the root widget appropriately
# “callback methods” for handling various aspects of app behaviour as defined above

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import trip


class ConverterApp(App):
    def build(self):
            Window.size = (350, 700)
            self.title = "Foreign Exchange Calculator"
            self.root = Builder.load_file('converter_app_trial.kv')
            return self.root

ConverterApp().run()
