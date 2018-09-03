import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

#.......................

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

ingredients_sheet = client.open('food_prep_python').sheet1
meals_sheet = client.open('meal').sheet1

meals = meals_sheet.col_values(2)
ingredients = ingredients_sheet.col_values(1)
pp = pprint.PrettyPrinter()

#.......................
#
# ASK
# FOR
# USER
# INPUT
#
# ...................

user_input = input('What did you eat? :')

#.......................
#
# CHECK IF USER INPUT IS A VALID MEAL
# IF MEAL EXISTS RETRIEVE LIST OF INGREDIENTS
# DATA IS STORED IN GOOGLE SHEET "MEAL" https://docs.google.com/spreadsheets/d/1zickEdwJB_wdhGquufZANr0Dnr8b6a5hAkN5i_Uk9A4/edit#gid=0
#
#......................


def check_meals(a):
    count = 1
    for x in meals:
        if x == a:
            check_meals.z = (meals_sheet.row_values(count))
            check_meals.z = check_meals.z[3:]
            # print("Check meals function works! details are %s" % check_meals.z)
        else:
            count += 1


check_meals(user_input)

#..........................
#
# USING LIST OF INGREDIENTS GENERATED FROM ABOVE FUNCTION
# SEARCH FOR INGREDIENT IN GOOGLE SHEET "food_prep_python" https://docs.google.com/spreadsheets/d/1TXosQg8zy19UAh3l9rA6Qa4ekkWBVwxsaS6UELhY20I/edit#gid=0
# IF INGREDIENT IS FOUND IN LIST, PRINT CALORIES FOR INGREDIENT
#
#............................


def calc_ingredients(y):
    length_of_list = (len(y))  # NEED TO FIND LENGTH OF INGREDIENTS LIST FOR INDEXING ... IF TOO LONG WILL "INDEX OUT OF RANGE"
    index_num_ingredients = 0  # STARTING INDEX LOCATION FOR INGREDIENTS LIST
    print("\n function to grab list of ingredients works! details are %s \n" % y)  # print ingredients
    print("the length of this list should be %s \n" % length_of_list)  # prints length of ingredients list e.g '6' ... list starts from 1 not ZER0.

 #........................................................................................................................................................

    for x in ingredients:
        while index_num_ingredients < length_of_list - 1:
            count = 1
            total_cal = 0
            for x in ingredients:  # GOES THOUGH VALUES IN GOOGLE SHEET INGREDIENTS COL
                if x == y[index_num_ingredients]:  # IF VALUE =
                    check_ingredients = (ingredients_sheet.row_values(count))
                    calories_found = (check_ingredients[1:2])
                    print(" %s has " % y[index_num_ingredients])
                    print(" %s calories" % calories_found[0])
                    # total_cal += int(calories_found[0])
                    # print(calories_found)
                    # print("IF has run here!")
                    index_num_ingredients += 1

                else:
                    count += 1
                    #$print("Else has run here!")


calc_ingredients(check_meals.z)
