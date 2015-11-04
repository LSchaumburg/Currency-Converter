__author__ = 'jc247746'

# An __init__ method capable of initialising a trip details field
# A build method that sets the window title appropriately, sets the window size to 350 x 700, and defines the root widget appropriately
# “callback methods” for handling various aspects of app behaviour as defined above

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from datetime import datetime
import currency
from trip import Details
from currency import web_utility
from kivy.properties import StringProperty
from kivy.properties import ListProperty


class ConverterApp(App):
    trip_file = open("config.txt", "r", encoding='utf-8')

    home_country = trip_file.readline().strip("\n")

    date_today = datetime.now().strftime("%Y/%m/%d")
    current_date = "Today is: \n" + date_today

    for line in trip_file:
        parts = line.split(",")
        country_name = parts[0]
        # print(country_name)
        start_date = parts[1]
        # print(start_date)
        end_date = parts[2]
        # print(end_date)
        if start_date <= date_today <= end_date:
            current_country = country_name

    # COUNTRY NAME TO BE BASE OFF THE CURRENT DATE AND THE DATES IN THE TRIP FILE
    # part = date_today.split("/")
    # for line in trip_file:
    #     if part[1] <= date_today <= part[2]:
    #         current_country_name = part[0]
    current_location = "Current trip location:\n" + current_country

    current_place = StringProperty()
    country_codes = ListProperty()

    # trip_details = currency.get_all_details()
    # trip_details.keys() is for the country code
    # home_country is for home country_name

    def __init__(self):  # , trip_details):
        super().__init__()

    def build(self):
        # __init__.trip_details = currency.get_all_details()
        # print(listed_trips)

        Window.size = (350, 700)
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        self.accepted_trip_details()
        # self.country_names = sorted(listed_trips)
        # self.current_place = self.country_names[0]
        return self.root

    def accepted_trip_details(self):
        # how to disable app from being used when an error occurs???
        trip_details = currency.get_all_details()
        list_of_trips = sorted(trip_details.keys())
        # print(list_of_trips)
        app_config_file = open("config.txt", "r", encoding='utf-8')
        first_line = app_config_file.readline()
        print(first_line.strip("\n"))
        # for country in list_of_trips:
            # print(list_of_trips)
        if first_line.strip("\n") in list_of_trips:
            for line in app_config_file:
                parts = line.split(",")
                if parts[0] in list_of_trips:
                    if len(parts[1]) == 10 and len(parts[2].strip("\n")) == 10:
                        self.root.ids.status_field.text = "Valid country"
                    else:
                        self.root.ids.status_field.text = "Invalid trip details"
                else:
                    self.root.ids.status_field.text = "Invalid trip details\ninvalid country"
        else:
            self.root.ids.status_field.text = "Invalid home country"
        app_config_file.close()

    def handle_update_button(self):
        localtime = datetime.now().strftime("%H:%M:%S")
        self.root.ids.status_field.text = "Last updated: " + localtime

        print("Updated exchange rate")

    def handle_home_currency_input(self):
        currency_value = self.root.ids.currency_value.text

        for parts in trip_details:
            if parts.key() == home_country:
                home_code = parts[2]

        for parts in trip_details:
            if parts.keys() == country_selector:
                away_code = parts[2]

        print(currency.convert(currency_value, home_code, away_code))

        # self.root.ids.status_field.text = home_code + "(" + home_symbol + ") to " + away_code + "(" + away_symbol + ")"

        ## input_url = "https://www.google.com/finance/converter?a={}&from={}&to={}".format(currency_value, home_code, away_code)
        ## converted_value = web_utility.load_page(input_url)
        ## result_amount_start = converted_value.find("class=bld>")
        ## result_amount_finish = converted_value.find("</span")
        ## result_amount_location = converted_value[result_amount_start:result_amount_finish]
        ## # print(result_amount_location)
        ##
        ## result_amount = result_amount_location.split("class=bld>")
        ## split_amount = result_amount[1]
        ## final_value = split_amount.split(" ")
        ## self.root.ids.current_currency_input.text = final_value[0]

    # def handle_away_currency_input(self, currency_value, home_country_code, away_country_code):
    #     currency.convert(currency_value, away_country_code, home_country_code)
    #     self.root.ids.status_field.text = "{}, ({}), to {}, ({})".format(away_country_code, away_symbol, home_country_code, home_symbol)
    #     self.root.ids.home_currency_input = converted_value

    def change_country(self):
        self.root.ids.country_selector.text = LISTED_TRIPS[country_code]
        # listed_trips = []
        #
        # for line in trip_file:
        #     parts = line.split(",")
        #     country_name = parts[0]
        #     listed_trips.append(country_name)
        # # print(listed_trips)
        # self.root.ids.country_selector.text = listed_trips[0]


# for updating the app:
# value_as_string = str(currency_value)

# currency from home to away
# input_url = ("https://www.google.com/finance/converter?a={}&from={}&to={}").format(value_as_string, home_country_code, away_country_code)

# currency from away to home
# input_url = ("https://www.google.com/finance/converter?a={}&from={}&to={}").format(value_as_string, away_country_code, home_country_code)

# converted_value = web_utility.load_page(input_url)
# return converted_value

ConverterApp().run()
