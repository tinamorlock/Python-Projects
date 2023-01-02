
import sqlite3

# parent class that describes a generic meal
# will include a method for the user to add entries for recipes
# this code will eventually be used to create an application for
# culinary cozy mystery authors to keep track of the recipes
# they use in their books


class Meal:
    calories = 0                # keeps track of calories of the meal
    recipeName = ''
    recipeCat = 'unknown'              # breakfast / lunch / dinner / unknown if not categorized
    recipe_num = 1              # this will get incremented as more recipes are created by the user
    # once the database is connected, recipe_num will be removed, and we should be able to use an
    # auto-incremented key in SQL to make this number simpler

    recipe_letter = 'U'         # U = Unknown
    # we probably won't use the parent class for anything, as it makes a recipe uncategorized

    how_many_serves = ''         # how many does the meal serve?
    # will have to convert this to a string if you need it to be an int

    prep_time = ''               # how many minutes does it take to put together?
    # will have to convert this to a string if you need it to be an int

    ingredients = []            # this will hold a list of ingredients the user enters
    ingredient_amount = []      # this will hold the amount of the ingredient user enters
    hot = True                  # would be true if it was a cooked item
    series_name = ''            # book series the recipe belongs to
    book_title = ''             # book title the recipe is used in
    book_chapter = ''
    instructions = []
    scratch = False             # True if made from scratch, False would indicate it uses pre-made ingredients

    # following method will assist the user in creating a database of recipes based upon their input
    # but, for now, it's just going to print on the screen to make sure it works before making it
    # more complicated

    def add_recipe(self):
        self.recipeName = input('What is the name of your recipe?\n>>> ')
        self.ingredients = []        # will be added to
        add_more = 'y'
        while add_more.lower() == 'y':
            self.ingredients.append(input('Enter an ingredient for the recipe:\n>>> '))
            self.ingredient_amount.append(input('How much of this ingredient should be added?\n>>> '))
            add_more = input('Do you want to add another ingredient? (y/n) >>> ')
            if add_more.lower() == 'y':
                continue
        self.calories = input('How many calories in your recipe? >>> ')
        self.prep_time = input('What is the prep time for this recipe? (Enter your answer in minutes.)\n>>> ')
        self.how_many_serves = input('How many people does your recipe serve? (Enter numerical input.)\n>>> ')
        hot_or_cold = input('Is your recipe served hot or cold? (hot / cold) >>> ')
        if hot_or_cold.lower() == 'hot':
            self.hot = True
        else:
            self.hot = False
        self.series_name = input('What book series does this recipe appear in?\n>>> ')
        self.book_title = input('What book title does this recipe appear in?\n>>> ')
        self.book_chapter = input('What CHAPTER NUMBER can this meal be found in? >>> ')
        add_more = 'y'
        print('\nLet\'s add some instructions for the recipe!')
        while add_more.lower() == 'y':
            self.instructions.append(input('\nEnter an instruction for the recipe:\n>>> '))
            add_more = input('Do you want to add another instruction for the recipe? (y/n) >>> ')
            if add_more.lower() == 'y':
                continue

    def print_recipe(self):
        print('Recipe #{}{}: {}'.format(self.recipe_letter, self.recipe_num, self.recipeName))
        print('This is a(n) {} recipe.'.format(self.recipeCat))
        print('Total prep time: {}'.format(self.prep_time))
        if self.hot:
            print('This meal will be served hot.')
        else:
            print('This meal will be served cold.')
        print('\nList of ingredients you will need:\n')

        # loop will print as many ingredients as user entered for this recipe

        loop_stop = len(self.ingredients)
        x = 0                               # initializing counter for loop

        while x < loop_stop:
            print('{} of {}\n'.format(self.ingredient_amount[x], self.ingredients[x]))
            x = x + 1
        print('\nHere are your instructions for the recipe:\n')

        # loop will print as many instructions as user entered for this recipe

        loop_stop = len(self.instructions)
        x = 0  # initializing counter for loop
        while x < loop_stop:
            print('{}\n'.format(self.instructions[x]))
            x = x + 1
        print('\nThis recipe makes {} servings.'.format(self.how_many_serves))
        print('This recipe was used in this book series: {}'.format(self.series_name))
        print('This recipe was used in this book: {}'.format(self.book_title))
        print('This meal can be found in Chapter {}.'.format(self.book_chapter))


# options for breakfast to include milk and/or juice


class Breakfast (Meal):
    juice = ''                  # type of juice drank for breakfast, enters none for none
    milk = False                # use Boolean value to denote whether milk will be drank/used for the breakfast
    recipeCat = 'breakfast'
    recipe_letter = 'B'          # will come before recipe number

    def add_recipe(self):
        self.recipeName = input('What is the name of your recipe?\n>>> ')
        self.ingredients = []        # will be added to
        add_more = 'y'
        while add_more.lower() == 'y':
            self.ingredients.append(input('Enter an ingredient for the recipe:\n>>> '))
            self.ingredient_amount.append(input('How much of this ingredient should be added?\n>>> '))
            add_more = input('Do you want to add another ingredient? (y/n) >>> ')
            if add_more.lower() == 'y':
                continue
        self.calories = input('How many calories in your recipe? >>> ')
        self.prep_time = input('What is the prep time for this recipe? (Enter your answer in minutes.)\n>>> ')
        self.how_many_serves = input('How many people does your recipe serve? (Enter numerical input.)\n>>> ')
        hot_or_cold = input('Is your recipe served hot or cold? (hot / cold) >>> ')
        if hot_or_cold.lower() == 'hot':
            self.hot = True
        else:
            self.hot = False
        self.series_name = input('What book series does this recipe appear in?\n>>> ')
        self.book_title = input('What book title does this recipe appear in?\n>>> ')
        self.book_chapter = input('What CHAPTER NUMBER can this meal be found in? >>> ')
        add_more = 'y'
        print('\nLet\'s add some instructions for the recipe!')
        while add_more.lower() == 'y':
            self.instructions.append(input('\nEnter an instruction for the recipe:\n>>> '))
            add_more = input('\nDo you want to add another instruction for the recipe? (y/n) >>> ')
            if add_more.lower() == 'y':
                continue
        self.juice = input('What type of juice was drank with this meal? (Enter none for none.)\n>>> ')
        temp_milk = input('Was milk drank with this meal? (y/n) >>> ')
        if temp_milk.lower() == 'y':
            self.milk = True
        else:
            self.milk = False

        # prints the entered recipe

    def print_recipe(self):
        print('Recipe #{}{}: {}'.format(self.recipe_letter, self.recipe_num, self.recipeName))
        print('This is a(n) {} recipe.'.format(self.recipeCat))
        print('Total prep time: {}'.format(self.prep_time))
        if self.hot:
            print('This meal will be served hot.')
        else:
            print('This meal will be served cold.')
        print('List of ingredients you will need:\n')

        # loop will print as many ingredients as user entered for this recipe

        loop_stop = len(self.ingredients)
        x = 0                               # initializing counter for loop

        while x < loop_stop:
            print('{} of {}'.format(self.ingredient_amount[x], self.ingredients[x]))
            x = x + 1

        print('\nHere are your instructions:\n')

        # loop will print as many instructions as user entered for this recipe

        loop_stop = len(self.instructions)
        x = 0  # initializing counter for loop

        while x < loop_stop:
            print('{}'.format(self.instructions[x]))
            x = x + 1

        print('\nThis recipe makes {} servings.'.format(self.how_many_serves))
        if self.milk:
            print('Milk goes well with this meal.')
        print('Juice that goes well with this meal: {}'.format(self.juice))
        print('This recipe was used in this book series: {}'.format(self.series_name))
        print('This recipe was used in this book: {}'.format(self.book_title))
        print('This meal can be found in Chapter {}.'.format(self.book_chapter))


class Lunch (Meal):
    recipeCat = 'lunch'
    recipe_letter = 'L'          # will come before recipe number
    salad = True                # indicates if character ate salad with this meal
    type_of_salad = ''          # the type of salad that goes well with this meal

    def add_recipe(self):
        self.recipeName = input('What is the name of your recipe?\n>>> ')
        self.ingredients = []        # will be added to
        add_more = 'y'
        while add_more.lower() == 'y':
            self.ingredients.append(input('Enter an ingredient for the recipe:\n>>> '))
            self.ingredient_amount.append(input('How much of this ingredient should be added?\n>>> '))
            add_more = input('Do you want to add another ingredient? (y/n) >>> ')
            if add_more.lower() == 'y':
                continue
        self.calories = input('How many calories in your recipe? >>> ')
        self.prep_time = input('What is the prep time for this recipe? (Enter your answer in minutes.)\n>>> ')
        self.how_many_serves = input('How many people does your recipe serve? (Enter numerical input.)\n>>> ')
        hot_or_cold = input('Is your recipe served hot or cold? (hot / cold) >>> ')
        if hot_or_cold.lower() == 'hot':
            self.hot = True
        else:
            self.hot = False
        self.series_name = input('What book series does this recipe appear in?\n>>> ')
        self.book_title = input('What book title does this recipe appear in?\n>>> ')
        self.book_chapter = input('What CHAPTER NUMBER can this meal be found in? >>> ')
        add_more = 'y'
        print('\nLet\'s add some instructions for the recipe!')
        while add_more.lower() == 'y':
            self.instructions.append(input('\nEnter the next instruction for the recipe:\n>>> '))
            add_more = input('Do you want to add another instruction for the recipe? (y/n) >>> ')
            if add_more.lower() == 'y':
                continue
        temp_salad = input('Was a salad eaten with this meal? (y/n) >>> ')
        if temp_salad.lower() == 'y':
            self.salad = True
            self.type_of_salad = input('What type of salad? >>> ')
        else:
            self.salad = False

        # prints the entered recipe --- START HERE

    def print_recipe(self):
        print('Recipe #{}{}: {}'.format(self.recipe_letter, self.recipe_num, self.recipeName))
        print('This is a(n) {} recipe.'.format(self.recipeCat))
        print('Total prep time: {}'.format(self.prep_time))
        if self.hot:
            print('\n\nThis meal will be served hot.')
        else:
            print('\n\nThis meal will be served cold.')
        print('\n\nList of ingredients you will need:\n\n')

        # loop will print as many ingredients as user entered for this recipe

        loop_stop = len(self.ingredients)
        x = 0                               # initializing counter for loop

        while x < loop_stop:
            print('{} of {}'.format(self.ingredient_amount[x], self.ingredients[x]))
            x = x + 1

        print('\nHere are your instructions:\n')

        # loop will print as many instructions as user entered for this recipe

        loop_stop = len(self.instructions)
        x = 0  # initializing counter for loop

        while x < loop_stop:
            print('{}\n'.format(self.instructions[x]))
            x = x + 1

        print('\n\nThis recipe makes {} servings.'.format(self.how_many_serves))
        if self.salad:
            print('\n\nType of salad that would go well with this meal: {}'.format(self.type_of_salad))
        print('\n\nThis recipe was used in this book series: {}'.format(self.series_name))
        print('\n\nThis recipe was used in this book: {}'.format(self.book_title))
        print('\n\nThis meal can be found in Chapter {}.'.format(self.book_chapter))

# options for dinner to include wine and to mark whether there were servings


class Dinner (Meal):
    wine = ''                 # type of wine that pairs well with this meal
    sweets = ''                 # what dessert, if any, made with this meal, enters none for none
    recipeCat = 'dinner'
    recipe_letter = 'D'          # will come before recipe number

    def add_recipe(self):
        self.recipeName = input('\nWhat is the name of your recipe?\n>>> ')
        self.ingredients = []        # will be added to
        add_more = 'y'
        while add_more.lower() == 'y':
            self.ingredients.append(input('\nEnter an ingredient for the recipe:\n>>> '))
            self.ingredient_amount.append(input('How much of this ingredient should be added?\n>>> '))
            add_more = input('\nDo you want to add another ingredient? (y/n) >>> ')
            if add_more.lower() == 'y':
                continue
        self.calories = input('\nHow many calories in your recipe? >>> ')
        self.prep_time = input('\nWhat is the prep time for this recipe? (Enter your answer in minutes.)\n>>> ')
        self.how_many_serves = input('\nHow many people does your recipe serve? (Enter numerical input.)\n>>> ')
        hot_or_cold = input('\nIs your recipe served hot or cold? (hot / cold) >>> ')
        if hot_or_cold.lower() == 'hot':
            self.hot = True
        else:
            self.hot = False
        self.series_name = input('\nWhat book series does this recipe appear in?\n>>> ')
        self.book_title = input('\nWhat book title does this recipe appear in?\n>>> ')
        self.book_chapter = input('\n\nWhat CHAPTER NUMBER can this meal be found in? >>> ')
        add_more = 'y'
        while add_more.lower() == 'y':
            self.instructions.append(input('\nEnter the next instruction for the recipe:\n>>> '))
            add_more = input('\nDo you want to add another instruction for the recipe? (y/n) >>> ')
            if add_more.lower() == 'y':
                continue
        self.wine = input('\n\nWhat type of wine was drank with this meal? (Enter none for none.)\n>>> ')
        self.sweets = input('\n\nWhat dessert was eaten with this meal? (Enter none for none.)\n>>> ')

        # prints the entered recipe

    def print_recipe(self):
        print('\n\nRecipe #{}{}: {}'.format(self.recipe_letter, self.recipe_num, self.recipeName))
        print('\n\nThis is a(n) {} recipe.'.format(self.recipeCat))
        print('\n\nTotal prep time: {}'.format(self.prep_time))
        if self.hot:
            print('\n\nThis meal will be served hot.')
        else:
            print('\n\nThis meal will be served cold.')
        print('\n\nList of ingredients you will need:\n\n')

        # loop will print as many ingredients as user entered for this recipe

        loop_stop = len(self.ingredients)
        x = 0                               # initializing counter for loop

        while x < loop_stop:
            print('{} of {}'.format(self.ingredient_amount[x], self.ingredients[x]))
            x = x + 1

        print('\n\nHere are your instructions:\n\n')

        # loop will print as many instructions as user entered for this recipe

        loop_stop = len(self.instructions)
        x = 0  # initializing counter for loop

        while x < loop_stop:
            print('{}\n'.format(self.instructions[x]))
            x = x + 1

        print('\n\nThis recipe makes {} servings.'.format(self.how_many_serves))
        print('\n\nWine drank with this meal: {}'.format(self.wine))
        print('\n\nDessert eaten with this meal: {}'.format(self.sweets))
        print('\n\nThis recipe was used in this book series: {}'.format(self.series_name))
        print('\n\nThis recipe was used in this book: {}'.format(self.book_title))
        print('\n\nThis meal can be found in Chapter {}.'.format(self.book_chapter))


class Dessert(Meal):
    chocolate = True                # set as True if it has Chocolate
    fruit = True                    # set as True if it has fruit in it
    fruit_used = ''                 # ex: Apples, bananas, pears, etc.


if __name__ == "__main__":

    grilled_cheese = Lunch()
    grilled_cheese.add_recipe()
    grilled_cheese.print_recipe()

