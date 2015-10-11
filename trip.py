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

        parts = date.split("/")
        if len(parts) == 3:
            if len(parts[0]) == 4 and len(parts[1]) == 2 and len(parts[2]) == 2:
                if parts[0].isdigit() == True and parts[1].isdigit() == True and parts[2].isdigit() == True:
                    print("Valid input")
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
                
        if not start_date.isdigit.split("/"):
            raise Error("Incorrect date format")

        if not end_date.isdigit.split("/"):
            raise Error("Incorrect date format")

        # Error checking that the start date is before the end date
        if start_date >= end_date:
            raise Error("Tried making the start date after the end date of travel. Expected Error.")

        # Error checking that the start date isn't already in the list
        for location in self.locations:
            if start_date in location[1]:
                raise Error("Tried to add date that already existed. Expected Error.")

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
        raise Error("No details about travel on that date")

    def is_empty(self):
        if len(self.locations) == 0:
            return True
        else:
            return False


""" Code Testing """
if __name__ == "__main__":
    """ Testing Country class """
    print("*** Testing Country class ***")
    country = Country("Germany", "EUR", "€")
    print("Testing format currency to print a value with a country's currency symbol: ", country.format_currency(100))
    print("Testing country input to produce a specified country's information ", country)
    print()

    """ Testing Details class """
    print("*** Testing Details class ***")
    details = Details()
    details.add("United States", "2015/09/01", "2015/09/17")
    details.add("Hong Kong", "2015/09/18", "2015/09/30")

    # start date already used
    try:
        details.add("Australia", "2015/09/18", "2016/10/25")
    except Error as error:
        print(error)

    # start date after end date
    try:
        details.add("Australia", "2016/10/25", "2015/09/18")
    except Error as error:
        print(error)

    # try:
    #     details.add("Australia", "12/06/2013", "24/06/2013")
    # except Error as error:
    #     print(error)
    #
    # try:
    #     details.add("Australia", "asdv/12/15", "2014/12/25")
    # except Error as error:
    #     print(error)

    # print(details.locations)
    # Checks is_empty
    try:
        details.is_empty()
    except Error as error:
        print("locations has data" error)

    details.locations = []

    try:
        details.is_empty()
    except Error as error:
        print(error)

    # details.current_country("2015/09/22")
    # print(details.current_country("2015/09/22"))
