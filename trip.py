__author__ = 'Luke'


class Error(Exception):
    def __init__(self, value):
        super().__init__(value)


class Country:
    def __init__(self, name, currency_code, currency_symbol):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol


# This class is used to record the sequence of countries visited during a trip.
class Details:
    def __init__(self):
        self.locations = []

    def __str__(self):
        return "{}, {}, {}".format(self.country_name, self.start_date, self.end_date)

    # locations (allowed to use list or dict) used to store the trip details
    def add(self, country_name, start_date, end_date):
        if date_setout != "YYYY/MM/DD":

        try:
            bad_date = False
        except:
            bad_date = True

        if bad_date == True:
            raise Error


        self.locations.append((country_name, start_date, end_date))

    # If the date string is within the start date and end date for a particular trip location then
    # the function should return the name of the country for that part of the trip.
    def current_country(self, date_string):
        self.date_string = date_string

    def is_empty(self, locations):
        if locations == "":
            is_empty = True
        else:
            is_empty = False
