import pandas


def string_checker(question,ans=["yes","no"]):
    """The most basic yes no checker"""
    while True:
        # gets the user response and makes it lowercase
        user_response = input(question).lower()
        # checks for first item in list or first character in first item
        if user_response == ans[0] or user_response == ans[0][0]:
            return True
        # same for second
        elif user_response == ans[1] or user_response == ans[1][0]:
            return False
        else:
            print(F"sorry please answer with either {str(ans).strip('[]')}")


def num_checker(question, type="float",max = ""):
    """this checks integers are above min value (0) and below either anything or five and also converts it to float or string to test.
    Do not fret that having a number as max will underline in yellow this is the computer thinking that it knows best, it is wrong of course"""
    error = F"please enter a {type} that is above 0"
    if not max == "":
        error+= F" and below {max}"

    while True:
        value = input(question).strip("$")
        # special case for grams can cause error with the fact that a user could enter the wrong number with g
        if "g" in value.lower():
            value = weight_conv(value)


        try:
            if type == "float":
                value = float(value)
            elif type == "int":
                value = int(value)
            if max == "":
                if value > 0:
                    return value
            elif 0 < value <= max:
                return value
            print(error)


        except ValueError:
            print(error)


def currency(x):
    """if you don't understand this why are you here its one line... it formats the currency im perplexed as to why you are reading this line despite you already knowing what it does... just read the literal one line of documentation if you must"""
    # literally just ads a $ at the start and formats it to 2 dp
    return "${:.2f}".format(x)


def write_the_file(text):
    """writes to the file (data in this case)"""
    text = str(text)
    text = text.strip("[]")
    text = "," + text
    open("data.txt", "w+").write(text)


def weight_conv(weight):
    """converts grams to kilograms"""
    weight = weight.lower()
    if not "k" in weight and "g" in weight:
        try:
            # removes the unnecessary text
            weight = weight.strip("g")
            # gets a float
            weight = float(weight)
            # makes it kgs equivalent
            weight /= 1000
        # returns a fail if it's a fail causing the user to try again
        except ValueError:
            return "Fail"
    else:
        weight = weight.strip("kg")
        weight = float(weight)
    return weight

def scorer(cost,weight,rating,rating_reviewers):
    """creates a score based on cost and reviews"""
    cost = cost/weight
    rating = rating/rating_reviewers
    return round(((rating / (cost * (((cost + 5 - rating)) * 2))) * 100000),3)

def new_data(name):
    """gets the user to add an item to the database (only gets name, weight and cost)"""
    print(
    F"we have not seen {name} yet so we need you to please fill out this "
    F"form before rating this product")
    raw_name.append(item_name)
    raw_cost.append(num_checker("please enter the cost "))
    raw_weight.append(num_checker("please enter the weight if you ignore the units it will be assumed as (kg) "))
    
def we_found_the_item(name):
    """to be used if an item matches the database used to double-check that the data is correct if not will fix it"""
    index = raw_name.index(name)
    cost = raw_cost[index]
    weight = raw_weight[index]
    rating = raw_rating[index]
    review_num = raw_review_num[index]
    # continues if the data is true gets the user to correct it if false
    if not string_checker(
            F"excellent news we found {name} in our database we just wish to confirm that this data is correct \n"
            F"is the cost of {name} is {currency(cost)} and {name} weighs {weight}kgs "):
        raw_cost[indexer] = (num_checker("please enter the cost as a number ignoring the $ "))
        raw_weight[indexer] = (
            num_checker("please enter the weight if you ignore the units it will be assumed as (kg) "))
        print("The item has been updated")
# opens the file (database)
file = open("data.txt", "r")
data = file.read()
data = data.replace("=","") + "="

# all the raw data extracted from the data.txt file
updated_data = []
raw_name = []
raw_cost = []
raw_weight = []
raw_rating = []
raw_review_num = []


# the users custom shopping list
shop_list = []
sort_shop_list = []
user_wallet = []
shop_score = []
sorted_shop_score = []
total = 0

# the data from one specific item
item_name = ""
item_cost = ""
item_weight = ""
item_rating = ""
item_review_num = ""

# counter usable across multiple places
t = 0
"""a ticker for anything be sure to set to zero before use"""

# used to get the specific item from the location on a raw list
indexer = 0
"""is used to find the data from multiple lists using one variable"""
# used across multiple places where a changeable string is needed
temp_word = ""
# used to decide what raw list to put our raw data while a ticker was needed elsewhere in use
sorter = 0


# runs until the intended end of the file the location of =
while not data[t] == "=":
    # breaks up each item
    if data[t] == "," and not data[t] == "=":
        t += 1
        # runs until the next break
        while not data[t] == "," and not data[t] == "=":
            # ignores the quotes
            if not data[t] == "'":
                # adds the char to the temp word
                temp_word = temp_word + data[t]
            t += 1
        # sorts the temp word based on how far through the file it is for example of it's a name it will be the zeroth instance so sorter equals zero
        if sorter == 0:
            # name
            raw_name.append(temp_word.strip(" "))
            sorter += 1
        elif sorter == 1:
            # cost
            temp_word = float(temp_word)
            raw_cost.append(temp_word)
            sorter += 1

        elif sorter == 2:
            # weight
            temp_word = float(temp_word)
            raw_weight.append(temp_word)
            sorter +=1
        elif sorter == 3:
            # rating
            temp_word = float(temp_word)
            raw_rating.append(temp_word)
            sorter +=1
        else:
            # number of reviews
            temp_word = int(temp_word)
            raw_review_num.append(temp_word)
            # sets the sorter back to zero as that will return the cycle back to the name
            sorter = 0
        temp_word = ""

print("welcome to bang for buck\na tool for shopping support")
print(F"This tool is used to give you the highest quality items based on rating and cost per unit from your personal shopping list\n")

# ability to review products before beginning
while string_checker("would you like to support this app by reviewing a product "):
    item_name = input("what is the name of the item you are looking for ").replace("=","").replace(",","")

    while item_name == "":
        item_name = input("please actually enter somthing ").replace("=","").replace(",","")
    # checks against the database for item
    if item_name in raw_name:
        # updates the indexer
        indexer = raw_name.index(item_name)
        # sets the relevant variables based on the indexer
        item_rating = raw_rating[indexer]
        item_review_num = raw_review_num[indexer]
        # shows the current rating
        print(F"thank you for taking your time to review {item_name} its current review is {item_rating/item_review_num} out of 5")
        # nabs the review and increments
        item_rating += num_checker("please enter your review ",type="int",max=5)
        item_review_num += 1
        raw_rating[indexer] = item_rating
        raw_review_num[indexer] = item_review_num
        # shows the new rating
        print(F"review successful!\nthe new review is now rated at {round(item_rating/item_review_num,2)} out of 5")

    else:
        # adds the new data
        new_data(item_name)
        raw_rating.append(num_checker("please enter your personal rating ",max=5))
        raw_review_num.append(1)
print("now that that's all cleared up lets get into this")
# gets the users budget
user_wallet = num_checker("please enter your budget ")

# gets the users list
if string_checker("do you want to put all the items in the list or would you prefer to list them one by one ",ans=["list","one by one"]):
    print("excellent choice... now this will be difficult you need to write each item with a comma between each item and ensure no spaces between ")
    full_list = input("ready... go ").replace("=","")
    while full_list == "":
        full_list = input("please dont enter '=' or ',' or nothing")
    # this makes a list in the same way that the file reader does
    full_list = "," + full_list + "="
    t = 0
    temp_word = ""
    # this code separates out items based on commas
    while not full_list[t] == "=": # the = is a forced end to the data
        if full_list[t] == "," and not full_list[t] == "=":
            t += 1
            # runs until the next break
            while not full_list[t] == "," and not full_list[t] == "=":
                temp_word = temp_word + full_list[t]
                t += 1
        # prevents the user from entering ,, as an option
        if not  temp_word == "":
            shop_list.append(temp_word)
        temp_word = ""
    for item in shop_list:
        if item in raw_name:
            we_found_the_item(item)
        # deals with unique foods
        else:
            new_data(item)
            raw_rating.append(num_checker("please enter your personal rating If you have yet to use this product you can base it on branding or just vibes ", max=5))
            raw_review_num.append(1)
# the more user-friendly method of making a list
else:
    print("great choice")
    # runs until out of items
    while not item_name == "quit":
        item_name = input("please enter a food item for your cart or type quit to quit ")
        # catches lack of items
        while item_name == "" or (item_name == "quit" and shop_list == []):
            item_name = input("please actually enter somthing ")
        if item_name == "quit":
            break
        # if the item is found in the database will check that the data is correct (if not will correct it) otherwise will get the user to add the item to the database
        if item_name in raw_name:
            we_found_the_item(item_name)
            shop_list.append(item_name)
        else:
            new_data(item_name)
            raw_rating.append(num_checker("please enter your personal rating If you have yet to use this product you can base it on branding or just vibes ", max=5))
            raw_review_num.append(1)
            shop_list.append(item_name)

# gets the users score
for item in shop_list:
    indexer = raw_name.index(item)
    item_weight = raw_weight[indexer]
    item_cost = raw_cost[indexer]
    item_rating = raw_rating[indexer]
    item_review_num = raw_review_num[indexer]
    shop_score.append(scorer(item_cost,item_weight,item_rating,item_review_num))

# this orders the users score by height and orders the correlating items
# sorts the shop score by itself
sorted_shop_score = sorted(shop_score)
for item in sorted_shop_score:
    # gets the original shop score index from the correlating sorted shop score
    indexer = shop_score.index(item)
    # adds the item from the shop list that correlates with the original shop score to where the sorted shop score is
    sort_shop_list.append(shop_list[indexer])
# polishes up and sets the items back to their common names
shop_score = sorted_shop_score
shop_list = sort_shop_list
total_cost = 0
# prunes the list of lowest scoring items until the cost is within budget
for item in shop_list:
    indexer = raw_name.index(item)
    # adds the cost of all the items to total cost
    total_cost += raw_cost[indexer]
# runs until under budget
while user_wallet < total_cost:
    # removes the lowest scoring item from shop list and its score
    shop_list.pop()
    shop_score.pop()
    # reestablishes cost
    total_cost = 0
    for item in shop_list:
        indexer = raw_name.index(item)
        total_cost += raw_cost[indexer]
the_costs = []
# sets up for the dictionary by establishing variables
for item in shop_list:
    indexer = raw_name.index(item)
    the_costs.append(currency(raw_cost[indexer]))
    total += raw_cost[indexer]
currency(total)


user_best_list = {
    "Name": shop_list,
    "Score": shop_score,
    "Cost": the_costs

}
# if the list is empty (all items were pruned)
if shop_list == []:
    print("sorry we were unable to find an acceptable bargain for you budget")
else:
    # prints the dataframe
    print("\n\n\n",pandas.DataFrame(user_best_list))
    print(f"\nTotal:                       {total}")

t = 0
# updates the data
for item in raw_name:
    updated_data.append(item)
    updated_data.append(raw_cost[t])
    updated_data.append(raw_weight[t])
    updated_data.append(raw_rating[t])
    updated_data.append(raw_review_num[t])
    t += 1
write_the_file(updated_data)