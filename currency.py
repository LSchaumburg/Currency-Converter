__author__ = 'Luke'

import web_utility


def convert(amount, original_currency_code, destination_currency_code):

    amount_as_string = str(amount)

    try:
        input_url = ("https://www.google.com/finance/converter?a={}&from={}&to={}").format(amount_as_string, original_currency_code, destination_currency_code)
        # print(input_url)
        converted_amount = web_utility.load_page(input_url)

        container_start = converted_amount.find("class=bld>")
        container_finish = converted_amount.find("</span")
        amount_container = converted_amount[container_start:container_finish]
        # print(amount_container)

        currency_bold = amount_container.split("class=bld>")
        split_currency = currency_bold[1]
        final_value = split_currency.split(" ")

        return final_value[0]
    except:
        return -1


# search for a country and get the details from the file
def get_details(country_name):
    countries_file = open("currency_details.txt", "r", encoding='utf-8')

    country_details = ()

    for line in countries_file:
        country_line = line.split(",")
        if country_name in line:
            if country_line[0] == country_name:
                return country_line
            else:
                return ()

    countries_file.close()

# get only the line that the user refers to (eg. "Australia" only reads Australia,AUD,$

print(convert(1, "AUD", "JPY"))
country_name = input("What is the name of the country? ")
print(get_details(country_name))

# get_details will access the file
# gets the name of the country and find the code and symbol

# convert will access the web utility
