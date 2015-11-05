__author__ = 'Luke Schaumburg'

# An __init__ method capable of initialising a trip details field
# A build method that sets the window title appropriately, sets the window size to 350 x 700, and defines the root widget appropriately
# “callback methods” for handling various aspects of app behaviour as defined above

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import time
import currency
from trip import Details
from trip import Error


class ConverterApp(App):
    trip_file = open("config.txt", "r", encoding='utf-8')
    home_country = trip_file.readline().strip("\n")
    trip_file.close()

    date_today = time.strftime("%Y/%m/%d")
    current_date = "Today is: \n" + date_today

    saved_trips = []
    trip_file = open("config.txt", "r", encoding='utf-8')
    next(trip_file)
    for line in trip_file:
        parts = line.strip("\n").split(",")
        saved_trips.append(parts[0])
    trip_file.close()

    trip_file = open("config.txt", "r", encoding='utf-8')
    next(trip_file)
    set_trips = Details()
    for line in trip_file:
        parts = line.strip("\n").split(",")
        try:
            set_trips.add(parts[0], parts[1], parts[2])
        except Error as error:
            print(error.value)

    current_country = set_trips.current_country(date_today)
    current_location = "Current trip location:\n" + current_country

    def __init__(self):
        super().__init__()
        self.trip_details = currency.get_all_details()
        # print(self.trip_details)

    def build(self):
        Window.size = (350, 700)
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        self.accepted_trip_details()
        self.disable_app()
        return self.root

    def disable_app(self):
        self.root.ids.home_currency_input.disabled = True
        self.root.ids.away_currency_input.disabled = True
        self.root.ids.country_selector.disabled = True

    def enable_app(self):
        self.root.ids.home_currency_input.disabled = False
        self.root.ids.away_currency_input.disabled = False
        self.root.ids.country_selector.disabled = False

    def accepted_trip_details(self):
        # how to disable app from being used when an error occurs???
        trip_details = self.trip_details
        list_of_trips = sorted(trip_details.keys())
        # print(list_of_trips)
        app_config_file = open("config.txt", "r", encoding='utf-8')
        first_line = app_config_file.readline()
        # print(first_line.strip("\n"))

        if first_line.strip("\n") in list_of_trips:
            for line in app_config_file:
                parts = line.split(",")
                if parts[0] in list_of_trips:
                    if len(parts[1]) == 10 and len(parts[2].strip("\n")) == 10:
                        self.root.ids.status_field.text = "Trip details accepted"
                    else:
                        self.root.ids.status_field.text = "Invalid trip details"
                        self.disable_app()
                else:
                    self.root.ids.status_field.text = "Invalid trip details\ninvalid country"
                    self.disable_app()
        else:
            self.root.ids.status_field.text = "Invalid home country"
            self.disable_app()
        app_config_file.close()

    def handle_update_button(self):
        localtime = time.strftime("%H:%M:%S")
        self.enable_app()
        # self.handle_currency_input()
        if self.root.ids.country_selector.text == "":
            user_country = self.current_country
            self.root.ids.country_selector.text = user_country
            self.root.ids.home_currency_input.text = ""
        self.root.ids.status_field.text = "Last updated: " + localtime
        # self.handle_currency_input("away")

    def handle_currency_input(self, home_away):
        country_information = self.trip_details
        selected_country = self.root.ids.country_selector.text

        away_country_information = country_information.get(selected_country)
        away_country_code = (away_country_information[1])

        home_country_information = (country_information.get(self.root.ids.home_country.text.strip("\n")))
        home_country_code = home_country_information[1]

        if self.root.ids.away_currency_input.text == "":
            self.root.ids.home_currency_input.text = ""

        elif home_away == "away":
            currency_value = self.root.ids.away_currency_input.text

            converted_value = currency.convert(currency_value, away_country_code, home_country_code)
            self.root.ids.home_currency_input.text = str(converted_value)
            self.root.ids.status_field.text = away_country_code + " (" + away_country_information[2] + ") to " + home_country_code + " (" + home_country_information[2] + ")"

        elif home_away == "home":
            currency_value = self.root.ids.home_currency_input.text

            converted_value = currency.convert(currency_value, home_country_code, away_country_code)
            self.root.ids.away_currency_input.text = str(converted_value)
            self.root.ids.status_field.text = home_country_code + " (" + home_country_information[2] + ") to " + away_country_code + " (" + away_country_information[2] + ")"

ConverterApp().run()
