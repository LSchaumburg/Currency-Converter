__author__ = 'Luke'

import web_utility

# convert will access the web utility
def convert(amount, original_currency_code, destination_currency_code):

    amount_as_string = str(amount)

    try:
        input_url = ("https://www.google.com/finance/converter?a={}&from={}&to={}").format(amount_as_string, original_currency_code, destination_currency_code)
        # print(input_url)
        converted_amount = web_utility.load_page(input_url)

        result_amount_start = converted_amount.find("class=bld>")
        result_amount_finish = converted_amount.find("</span")
        result_amount_location = converted_amount[result_amount_start:result_amount_finish]
        # print(result_amount_location)

        result_amount = result_amount_location.split("class=bld>")
        split_amount = result_amount[1]
        final_value = split_amount.split(" ")

        return final_value[0]
    except:
        return -1


# search for a country and get the details from the file
# get_details will access the file
# gets the name of the country and find the code and symbol
def get_details(country_name):
    countries_file = open("currency_details.txt", "r", encoding='utf-8')

    country_details = ()

    for line in countries_file:
        country_line = line.split(",")
        if country_name in line:
            if country_line[0] != country_name:
                return ()
            else:
                return country_details.__add__((country_line[0], country_line[1], country_line[2]))

    # print(country_details)

    countries_file.close()
    return ()

# get only the line that the user refers to (eg. "Australia" only reads Australia,AUD,$

# print(convert(1, "AUD", "JPY"))
# country_name = input("What is the name of the country? ")
# print(get_details(country_name))

""" Code Testing """
if __name__ == "__main__":

    print("invalid conversion", "1", "AUD", "->", "AUD", "=", currency.convert(1, "AUD", "AUD"))
    print("invalid conversion", "1", "JPY", "->", "ABC", "=", currency.convert(1, "JPY", "ABC"))
    print("invalid conversion", "1", "ABC", "->", "USD", "=", currency.convert(1, "ABC", "USD"))
    print("valid conversion", "10.95", "AUD", "->", "JPY", "=", currency.convert(10.95, "AUD", "JPY"))
    print("valid conversion reverse", "965.71", "JPY", "->", "AUD", "=", currency.convert(965.71, "JPY", "AUD"))
    print("valid conversion", "10.95", "AUD", "->", "BGN", "=", currency.convert(10.95, "AUD", "BGN"))
    print("valid conversion reverse", "13.82", "BGN", "->", "AUD", "=", currency.convert(13.82, "BGN", "AUD"))
    print("valid conversion", "200.15", "BGN", "->", "JPY", "=", currency.convert(200.15, "BGN", "JPY"))
    print("valid conversion reverse", "13390.51", "JPY", "->", "BGN", "=", currency.convert(13390.51, "JPY", "BGN"))
    print("valid conversion", "100", "JPY", "->", "USD", "=", currency.convert(100, "JPY", "USD"))
    print("valid conversion reverse", "0.83", "USD", "->", "JPY", "=", currency.convert(0.83, "USD", "JPY"))
    print("valid conversion", "19.99", "USD", "->", "BGN", "=", currency.convert(19.99, "USD", "BGN"))
    print("valid conversion reverse", "34.39", "BGN", "->", "USD", "=", currency.convert(34.39, "BGN", "USD"))
    print("valid conversion", "19.99", "USD", "->", "AUD", "=", currency.convert(19.99, "USD", "AUD"))
    print("valid conversion reverse", "27.26", "AUD", "->", "USD", "=", currency.convert(27.26, "AUD", "USD"))

    print("invalid details", currency.get_details("Unknown"))
    print("invalid details", currency.get_details("Japanese"))
    print("invalid details", currency.get_details(""))
    print("valid details", currency.get_details("Australia"))
    print("valid details", currency.get_details("Japan"))
    print("valid details", currency.get_details("Hong Kong"))
