__author__ = 'jc247746'

# An __init__ method capable of initialising a trip details field
# A build method that sets the window title appropriately, sets the window size to 350 x 700, and defines the root widget appropriately
# “callback methods” for handling various aspects of app behaviour as defined above

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from datetime import datetime
import currency
from currency import web_utility


class ConverterApp(App):
    trip_file = open("config.txt", "r", encoding='utf-8')

    home_country = trip_file.readline()

    date_today = datetime.now().strftime("%Y/%m/%d")
    current_date = "Today is: \n" + date_today

    # COUNTRY NAME TO BE BASE OFF THE CURRENT DATE AND THE DATES IN THE TRIP FILE
    # part = date_today.split("/")
    # for line in trip_file:
    #     if part[1] <= date_today <= part[2]:
    #         current_country_name = part[0]

    current_location = "Current trip location:\n" + home_country

    trip_details = currency.get_all_details()

    # trip_details = currency.get_all_details()
    # trip_details.keys() is for the country code
    # home_country is for home country_name

    def __init__(self):
        super().__init__()

    def build(self):
        trip_details = currency.get_all_details()

        Window.size = (350, 700)
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        self.country_codes = sorted(trip_details)
        self.current_country = self.country_codes[0]
        return self.root

    def handle_update_button(self):
        localtime = datetime.now().strftime("%H:%M:%S")
        self.root.ids.status_field.text = "Last updated: " + localtime
        print("Updated exchange rate")

    def handle_home_currency_input(self):
        # currency_value = currency_value.text
        # value_as_string = currency_value
        # currency.convert(currency_value, home_country_code, away_country_code)
        self.root.ids.status_field.text = "AUD ($) to JPY ($)"  # "{}, ({}), to {}, ({})".format(home_country_code(part[1]), home_symbol(part[2]), away_country_code(part[1]), away_symbol(part[2]))
        input_url = "https://www.google.com/finance/converter?a=10&from=AUD&to=JPY"  # .format("10", "JPY", "AUD")
        converted_value = web_utility.load_page(input_url)
        result_amount_start = converted_value.find("class=bld>")
        result_amount_finish = converted_value.find("</span")
        result_amount_location = converted_value[result_amount_start:result_amount_finish]
        # print(result_amount_location)

        result_amount = result_amount_location.split("class=bld>")
        split_amount = result_amount[1]
        final_value = split_amount.split(" ")
        self.root.ids.current_currency_input.text = final_value[0]

    # def handle_away_currency_input(self, currency_value, home_country_code, away_country_code):
    #     currency.convert(currency_value, away_country_code, home_country_code)
    #     self.root.ids.status_field.text = "{}, ({}), to {}, ({})".format(away_country_code, away_symbol, home_country_code, home_symbol)
    #     self.root.ids.home_currency_input = converted_value

    # def change_country(self, trip_details):
    #     self.root.ids.output_label.text = trip_details[country_code]

# for updating the app:
# value_as_string = str(currency_value)

# currency from home to away
# input_url = ("https://www.google.com/finance/converter?a={}&from={}&to={}").format(value_as_string, home_country_code, away_country_code)

# currency from away to home
# input_url = ("https://www.google.com/finance/converter?a={}&from={}&to={}").format(value_as_string, away_country_code, home_country_code)

# converted_value = web_utility.load_page(input_url)
# return converted_value

ConverterApp().run()
