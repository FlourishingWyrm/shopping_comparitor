file = open("data.txt", "r")
data = file.read()
data = data.translate("")
full_file = []
dataname = []
datacost = []
dataweight = []
ticker = 0
list_tracker = 0
tempword = ""
current_item_index = 0
while not data[ticker] == "=":
    if data[ticker] == "," and not data[ticker] == "=":
        ticker += 1
        while not data[ticker] == "," and not data[ticker] == "=":
            if not data[ticker] == "'":
                tempword = tempword + data[ticker]
            ticker += 1
        if list_tracker == 0:
            dataname.append(tempword)
            list_tracker += 1
        elif list_tracker == 1:
            tempword = float(tempword)
            datacost.append(tempword)
            list_tracker += 1
        else:
            tempword = float(tempword)
            dataweight.append(tempword)
            list_tracker = 0
        tempword = ""


def fancy_statement(decor, txt, lines):
    """this is a function that will return the inputted decor and txt into a format that looks like this decordecordecor
 txt decordecordecor"""
    # returns the above value
    if len(decor) == 0:
        decor = " "
    lines = int(lines)
    length = int(len(F"{decor * 3} {txt} {decor * 3}"))
    decor_length = len(decor)
    decor_line = F"{decor * int((length / decor_length))}"
    char = 0
    while not len(decor_line) == length:
        decor_line = F"{decor_line}{decor[char]}"
        char += 1
    decor_line = F"{decor_line}\n"
    # returns the request of the amount of lines with the lower line being unused
    return F"{decor_line * (round(((lines - 1) / 2)))}{decor * 3} {txt} {decor * 3}\n{decor_line * (round(((lines - 1) / 2 + 0.4)))}"


def string_checker(question, valid_as, returned_value):
    """Checks users enter either the full word or the first
    letter of the word in the valid answer list"""
    while True:
        # gets the user response and makes it lowercase
        user_response = input(question).lower()
        successes = 0
        part = ""
        for item in valid_as:
            test = "u"
            x = 0
            # checks if the user response is in the word list
            if item == user_response:
                return returned_value[valid_as.index(item)]
            elif user_response == "":
                break

            # checks if the user response is the same as the first letter of an item in a list
            elif user_response[x] == item[x] and len(user_response) <= len(item):
                while not x == len(item) and not x == len(user_response) - 1:
                    if user_response[x] == item[x]:
                        x += 1
                    else:
                        test = "h"
                        break
                if not len(user_response) > len(item) and not test == "h":
                    char_loc = len(user_response) - 1
                    if item[char_loc] == user_response[char_loc]:
                        successes += 1
                        part = item

        if successes == 1 and not part == "":
            return returned_value[valid_as.index(part)]
        elif part == "" or successes < 1:
            print(F"sorry please answer with {valid_as}")
        else:
            print(F"to avoid confusion please continue the word until it is significantly distinguishable ")


def currency(x):
    return "${:.2f}".format(x)


def write_the_file(text):
    text = str(text)
    text = text.strip("[]")
    text = "," + text + "="
    open("data.txt", "w+").write(text)


def num_checker(question, type="float", accepted=[]):
    """this checks integers are above min value -1 if there are not integers or are not above -1 it returns n error"""
    error = F"please enter a {type}"
    while True:
        value = input(question)
        if value in accepted:
            return value
        try:
            if type == "float":
                value = float(value)
            elif type == "int":
                value = int(value)
            return value

        except ValueError:
            print(error)

def weight_conv(question):


print(dataweight)
                            # _______________________welcome crap________________________________
# boot_up = string_checker("what mode would you like to boot up in? ",["baby","dev","standard"],["baby","dev","standard"])
freud = input("name of item")
current_name = ""
item_price = 0
item_weight = 0
temperary_overwriteable = ""
if freud in dataname:
    current_item_index = dataname.index(freud)
    item_price = datacost[current_item_index]
    item_weight = dataweight[current_item_index]
    if string_checker(f"the name that was entered already matches our database is this accurate:"
        f"\n(Cost: {item_price} Weight: {item_weight})", ["yes", "no"], [True, False]):
        current_item_index = dataname.index(freud)
        itemprice = datacost[current_item_index]
    else:
        print("since this was inaccurate we will need your help to update it")
        temperary_overwriteable = num_checker(
            f"what is the correct price, press enter if {item_price} is already correct", accepted=[""])
        if not temperary_overwriteable == "":

            item_price = temperary_overwriteable
            datacost[current_item_index] = temperary_overwriteable
        temperary_overwriteable = num_checker(
            f"what is the correct weight, press enter if {item_weight} is already correct", accepted=[""])
        if not temperary_overwriteable == "":
            item_weight = temperary_overwriteable
            dataweight[current_item_index] = temperary_overwriteable


else:
    print("this item was not found in our database, to ensure more accurate results please fill out the data...")
    item_price = num_checker("please enter the correct item price")
    item_weight = weight_conv()

ticker = 0

for item in dataname:
    full_file.append(item)
    full_file.append(datacost[ticker])
    full_file.append(dataweight[ticker])
    ticker += 1
    print(full_file)
write_the_file(full_file)
