__author__ = 'Luke Schaumburg'

import datetime


class Error(Exception):
    def __init__(self, value):
        super().__init__(value)


class Country:
    def __init__(self, name, currency_code, currency_symbol):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def __str__(self):
        return "\'{} {} {}\'".format(self.name, self.currency_code, self.currency_symbol)

    def format_currency(self, amount):
        return self.currency_symbol + format(amount, ".0f")


# This class is used to record the sequence of countries visited during a trip.
class Details:
    def __init__(self):
        self.locations = []

    # locations (allowed to use list or dict) used to store the trip details
    def add(self, country_name, start_date, end_date):
        if not (isinstance(country_name, str) or isinstance(start_date, str) or isinstance(end_date, str)):
            raise Error("At least on of these variables is not a string")

        # Error checking that the start date is before the end date
        if start_date >= end_date:
            raise Error("Start date is after end date")

        # Error checking that the start date isn't already in the list
        for location in self.locations:
            if start_date in location[1]:
                raise Error("Start date already exists")

        self.locations.append((country_name, start_date, end_date))
        return self.locations

    # If the date string is within the start date and end date for a particular trip location then
    # the function should return the name of the country for that part of the trip.
    def current_country(self, date_string):
        self.date_string = date_string

        if not datetime.datetime.strptime(date_string, "%Y/%m/%d"):
            raise Error("Date has incorrect format")

        for location in self.locations:
            if location[1] <= date_string <= location[2]:
                return location[0]
            else:
                raise Error("No details about travel on that date")

    def is_empty(self):
        if len(self.locations) == 0:
            return True
        else:
            return False


""" Code Testing """
if __name__ == "__main__":
    details = Details()
    details.add("United States", "2015/09/01", "2015/09/17")
    details.add("Hong Kong", "2015/09/18", "2015/09/30")
    details.add("Australia", "2015/09/18", "2016/10/25")  # Can't be added because of existing start date 

    print(details.locations)
    # details.current_country("2015/09/22")
    # print(details.current_country("2015/09/22"))

    try:
        pass
    except:
        pass
