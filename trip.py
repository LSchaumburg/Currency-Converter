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
        if not (isinstance(self.country_name, str) or isinstance(self.start_date, str) or isinstance(self.end_date, str)):
            return Error

        if date == datetime.datetime.strptime(self.date_string, "%Y/%m/%d"):
            return date
        else:
            raise Error("Invalid date!")

        # if date_setout != "YYYY/MM/DD":
        #     try:
        #         bad_date = False
        #     except:
        #         bad_date = True
        #

        # if bad_date == True:
        #     raise Error


        self.locations.append((country_name, start_date, end_date))
        return locations

    # If the date string is within the start date and end date for a particular trip location then
    # the function should return the name of the country for that part of the trip.
    def current_country(self, date_string):
        self.date_string = date_string

        if not datetime.datetime.strptime(date_string, "%Y/%m/%d"):
            raise Error("Date has incorrect format")

        for location in self.locations:
            if location[1] <= date_string <= location[2] in self.locations:
                return location[0]
            else:
                raise Error("No details about travel on that date")



# you know how we have location in self.locations?
# that 'location' is how we access the information inside the list
# that is accessing the tuple information

                # used_date = open('config.txt', 'r')
                #
                # for line in used_date:
                #     if date_string in line:
                #         if date_string == used_date:
                #             raise Error
                #
                # if date_string == used_date:
                #
                # a, b, c = tu
                #
                #     if used_date == date_string:
                #         return True
                #     else:
                #         return False
                #
                # if date_string == False:
                #     raise Error
                #
                # trip_agenda = open('config.txt', 'r')
                # for line in trip_agenda:
                #     if date_string in line:
                #         raise Error
                #     else:
                #         trip_agenda.close()
                #         trip_agenda = open('config.txt', 'w')
                #         trip_agenda.write(date_string)
                #         trip_agenda.close()

    def is_empty(self):
        if len(self.locations) == 0:
            return True
        else:
            return False


""" Code Testing """
if __name__ == "__main__":
    details = Details()
    details.add("United States", "2015,09,01", "2015,09,17")
    details.add("Hong Kong", "2015,09,18", "2015,09,30")

    details.current_country("2015/09/22")
    try:
        pass
    except:
        pass
