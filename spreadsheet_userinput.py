import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)


sheet = client.open('food_prep_python').sheet1

#.......................
#
#
#
# ASK
# FOR
# USER
# INPUT
#
#
#
# ...................

user_input = input('What did you eat? :')
ingredients = sheet.col_values(1)
pp = pprint.PrettyPrinter()

#...........................
#
#
#..........................


def check_if_exist(a):
    count = 1
    for x in ingredients:
        # print(count) # for testing
        if x == a:
            print("Food : Calories : Fat : Carbs : Protein : Type \n")
            pp.pprint(sheet.row_values(count))
        else:
            count += 1


check_if_exist(user_input)

"""
pp = pprint.PrettyPrinter()
ingredients = sheet.col_values(1)
pp.pprint(ingredients)

tes test
"""
