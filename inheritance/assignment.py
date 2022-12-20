
# parent class that describes a generic meal

class Meal:
    timeOfDay = '' # morning, noon, evening, etc.
    calories = 0 # keeps track of calories of the meal
    ingredient_1 = '' # lists a main ingredient
    ingredient_2 = '' # lists a main ingredient
    ingredient_3 = '' # lists a main ingredient
    how_many_serves = 0 # how many does the meal serve?
    how_long_to_cook = 0 # how many minutes does it take to put together?
    hot = True #would be true if it was a cooked item
    cold = False # would be false if it was a cooked item

# options for breakfast to include milk and/or juice

class Breakfast (Meal):
    juice = '' # type of juice drank for breakfast 
    milk = False # use Boolean value to denote whether
                 # milk will be drank/used for the breakfast


# options for lunch to add a salad and record how many ounces of water drank

class Lunch (Meal):
    salad = True # true if user will be eating a salad with their lunch
    water = 0 # indicates how many ounces of water drank with lunch

# options for dinner to include wine and to mark whether there were servings
# leftover that could be consumed for another lunch or dinner meal

class Dinner (Meal):
    wine = True # true to indicate if drinking wine with dinner
    leftovers = False # false would indicate there are no leftovers to save
