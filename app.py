__author__ = 'jc247746'

# An __init__ method capable of initialising a trip details field
# A build method that sets the window title appropriately, sets the window size to 350 x 700, and defines the root widget appropriately
# “callback methods” for handling various aspects of app behaviour as defined above

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConverterApp(App):
    trip_file = open("config.txt", "r", encoding='utf-8')

    line = trip_file.readline()
    current_country = "Current trip location:\n" + line

    def build(self):
        Window.size = (350, 700)
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('converter_app_trial.kv')
        return self.root

    # def current_location(self):
    #     self.root.ids.current_location.text = "current country goes here"

    def handle_update_button(self):
        self.root.ids.status_field.text = "Last updated " + "*the current time*"

ConverterApp().run()
