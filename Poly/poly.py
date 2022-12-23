

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
    recipe_letter = 'U'         # U = Unknown
    how_many_serves = 0         # how many does the meal serve?
    prep_time = 0               # how many minutes does it take to put together?
    ingredients = []
    hot = True                  # would be true if it was a cooked item
    series_name = ''            # book series the recipe belongs to
    book_title = ''             # book title the recipe is used in
    book_chapter = 0
    instructions = []

    # following method will assist the user in creating a database of recipes based upon their input
    # but, for now, it's just going to print on the screen to make sure it works before making it
    # more complicated

    def add_recipe(self):
        self.recipeName = input('\nWhat is the name of your recipe?\n>>> ')
        self.ingredients = []        # will be added to
        add_more = 'y'
        while add_more.lower() == 'y':
            self.ingredients.append(input('\nEnter an ingredient for the recipe:\n>>> '))
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
            print('{}\n'.format(self.ingredients[x]))
            x = x + 1
        print('\n\nHere are your instructions:\n\n')

        # loop will print as many instructions as user entered for this recipe

        loop_stop = len(self.instructions)
        x = 0  # initializing counter for loop
        while x < loop_stop:
            print('{}\n'.format(self.instructions[x]))
            x = x + 1
        print('\n\nThis recipe makes {} servings.'.format(self.how_many_serves))
        print('\n\nThis recipe was used in this book series: {}'.format(self.series_name))
        print('\n\nThis recipe was used in this book: {}'.format(self.book_title))
        print('\n\nThis meal can be found in Chapter {}.'.format(self.book_chapter))


# options for breakfast to include milk and/or juice


class Breakfast (Meal):
    juice = ''                  # type of juice drank for breakfast, enters none for none
    milk = False                # use Boolean value to denote whether milk will be drank/used for the breakfast
    recipeCat = 'breakfast'
    recipe_letter = 'B'          # will come before recipe number

    def add_recipe(self):
        self.recipeName = input('\nWhat is the name of your recipe?\n>>> ')
        self.ingredients = []        # will be added to
        add_more = 'y'
        while add_more.lower() == 'y':
            self.ingredients.append(input('\nEnter an ingredient for the recipe:\n>>> '))
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
        self.juice = input('\n\nWhat type of juice was drank with this meal? (Enter none for none.)\n>>> ')
        temp_milk = input('\n\nWas milk drank with this meal? (y/n) >>> ')
        if temp_milk.lower() == 'y':
            self.milk = True
        else:
            self.milk = False

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
            print('{}\n'.format(self.ingredients[x]))
            x = x + 1

        print('\n\nHere are your instructions:\n\n')

        # loop will print as many instructions as user entered for this recipe

        loop_stop = len(self.instructions)
        x = 0  # initializing counter for loop

        while x < loop_stop:
            print('{}\n'.format(self.instructions[x]))
            x = x + 1

        print('\n\nThis recipe makes {} servings.'.format(self.how_many_serves))
        if self.milk:
            print('\n\nMilk goes well with this meal.')
        print('\n\nJuice that goes well with this meal: {}'.format(self.juice))
        print('\n\nThis recipe was used in this book series: {}'.format(self.series_name))
        print('\n\nThis recipe was used in this book: {}'.format(self.book_title))
        print('\n\nThis meal can be found in Chapter {}.'.format(self.book_chapter))


class Lunch (Meal):
    recipeCat = 'lunch'
    recipe_letter = 'L'          # will come before recipe number
    salad = True                # indicates if character ate salad with this meal
    type_of_salad = ''          # the type of salad that goes well with this meal

    def add_recipe(self):
        self.recipeName = input('\nWhat is the name of your recipe?\n>>> ')
        self.ingredients = []        # will be added to
        add_more = 'y'
        while add_more.lower() == 'y':
            self.ingredients.append(input('\nEnter an ingredient for the recipe:\n>>> '))
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
        temp_salad = input('\n\nWas a salad eaten with this meal? (y/n) >>> ')
        if temp_salad.lower() == 'y':
            self.salad = True
            self.type_of_salad = input('\n\nWhat type of salad? >>> ')
        else:
            self.salad = False

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
            print('{}\n'.format(self.ingredients[x]))
            x = x + 1

        print('\n\nHere are your instructions:\n\n')

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
            print('{}\n'.format(self.ingredients[x]))
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


if __name__ == "__main__":

    grilled_cheese = Lunch()
    grilled_cheese.add_recipe()
    grilled_cheese.print_recipe()

