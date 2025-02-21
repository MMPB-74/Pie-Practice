import time
import random
import textwrap
import math


fastest_times = {}

#need to setup ingredients and other assets


# List of recipes 
recipes = [
    {"name": "Buffalo Chicken Pizza", "ingredients": ["mz", "buff", "carmon", "bac"]},  
    {"name": "Funky Q. Chicken Pizza", "ingredients": ["mz", "bbq chkn", "carmon", "bac", "ched", "bbq s"]},  
    {"name": "Great White Pizza", "ingredients": ["og", "ric", "roasted", "prov", "mz", "on", "roma", "feta"]},  
    {"name": "Hey Dude Pizza", "ingredients": ["ranch", "mz", "chkn", "bac", "ched", "japs"]},  
    {"name": "House Special Pizza", "ingredients": ["red", "mz", "pepp", "sausage", "beef", "on", "gpep", "mush", "olive", "roma", "bac", "ham", "mz"]},  
    {"name": "Kosmic Karma Pizza", "ingredients": ["red", "roasted", "spin", "mz", "roma", "feta", "pesto s"]},  
    {"name": "Marley", "ingredients": ["pesto b", "mz", "sausage", "on", "jerk"]},  
    {"name": "Maui Wowie", "ingredients": ["pesto b", "mz", "ham", "papple", "jerk", "bac", "bpep"]},  
    {"name": "Mellowterranean", "ingredients": ["og", "mz", "chkn", "on", "grrp", "olive", "feta"]},  
    {"name": "Merry Prankster Pie", "ingredients": ["herb", "mz", "chkn", "sausage", "gpep", "grrp", "white"]},  
    {"name": "Mighty Meaty Pizza", "ingredients": ["red", "mz", "pepp", "sausage", "beef", "ham", "bac"]},  
    {"name": "Pacific Rim Pizza", "ingredients": ["red", "mz", "ham", "bac", "carmon", "papple", "japs"]},  
    {"name": "Philosophers Pie", "ingredients": ["og", "steak", "prov", "feta", "mz", "kalamata", "arty", "porto"]},  
    {"name": "Sausagefest Calzone", "ingredients": ["mz", "ric", "prov", "sal", "mtbl", "sausage"]},  
    {"name": "Holy Shiitake Pizza", "ingredients": ["og", "mz", "white", "trio", "carmon"]},  
    {"name": "Thai Dye", "ingredients": ["og", "mz", "curry", "on", "roma"]},  
    {"name": "Veg Out Pizza", "ingredients": ["red", "spin", "mz", "on", "gpep", "mush", "olive", "roma"]},  
    {"name": "Veggie Supreme Calzone", "ingredients": ["mz", "ric", "prov", "spin", "mush", "roma"]},  
    {"name": "White Rabbit", "ingredients": ["og", "roasted", "spin", "mz", "feta", "mush", "arty"]},
    {"name": "Steakhouse Pizza", "ingredients": ["og", "mz", "steak", "trio", "carmon", "mamas"]},
    {"name": "Steak Calzone", "ingredients": ["mz", "ric", "prov", "steak", "on", "gpep", "mush"]},
    {"name": "Super Pep", "ingredients": ["red", "mz", "pepp", "pepp", "mamas"]},
    {"name": "Da'Vinci", "ingredients": ["og", "spin", "mz", "mtbl", "ric", "red"]},
    {"name": "Loaded Potato", "ingredients": ["og", "mz", "potat", "carmon", "bac", "ched"]},
    {"name": "Mad Italian", "ingredients": ["og", "mz", "sal", "ham", "on", "grrp", "cini"]},
    {"name": "Magical Mystery Tour", "ingredients": ["pesto b", "spin", "mz", "mush", "porto", "japs", "feta"]},
    {"name": "Miss Mushroom", "ingredients": ["red", "spin", "garlic", "vmz", "carmon", "porto"]},
]

##ingredients grouped all together



# Ingredient dictionary (shorthand -> full name)
ingredient_check = {
    'red': 'red sauce',  
    'og': 'olive oil-garlic base',  
    'pesto b': 'pesto base',
    'pesto chkn': 'pesto chicken',
    'pesto s': 'pesto swirl',
    'ranch': 'ranch base',  
    'herb': 'herb aioli',  
    'bbq chkn': 'barbecue chicken',
    'bbq s': 'barbecue swirl',
    'buff': 'buffalo chicken',  
    'jerk': 'jerk chicken',  
    'curry': 'curry chicken',  
    'mz': 'shredded mozzarella',  
    'ched': 'cheddar',  
    'white': 'white cheddar',  
    'prov': 'provolone',  
    'ric': 'ricotta',  
    'feta': 'crumpled feta',  
    'pepp': 'pepperoni',  
    'bac': 'bacon',  
    'ham': 'ham',  
    'beef': 'beef',  
    'sausage': 'italian sausage',  
    'chkn': 'grilled chicken',  
    'steak': 'cooked steak',  
    'sal': 'salami',  
    'mtbl': 'meatball',  
    'mush': 'mushrooms',  
    'gpep': 'green peppers',  
    'on': 'onion',  
    'olive': 'black olives',  
    'roma': 'roma tomato slices',  
    'spin': 'fresh spinach',  
    'roasted': 'roasted tomatoes',  
    'mamas': ["mama lil's peppers", 'mama lils peppers'],  
    'grrp': 'garlic-roasted red peppers',  
    'arty': 'artichoke hearts',  
    'kalamata': 'kalamata olives',  
    'porto': 'portobello',  
    'japs': 'jalapenos',  
    'bpep': 'banana peppers',  
    'papple': 'pineapple',  
    'trio': 'mushroom trio',  
    'carmon': 'caramelized onions',
    'garlic': 'minced garlic',
    'potat': 'roasted red potatoes',
    'vmz': 'vegan mozzarella',
    'cini': 'pepperoncini',
}



        
###let's fix this thing now
def librarian_resource(input_ingredient):
    # Normalize the input (strip spaces and convert to lowercase)
    input_ingredient = input_ingredient.strip().lower()

    # Reverse lookup from the ingredient_check dictionary
    for shorthand, full_name in ingredient_check.items():
        # If the full name or shorthand matches the input, return the shorthand
        if input_ingredient == full_name or input_ingredient == shorthand:
            return shorthand
        if input_ingredient in ["fire pie", "fire", "bake", "oven", "done", "finished", "go", "fin", "hands", "good", "complete", "enter", "f", "fir", "fie", "fi", "pie"]:
            return "fire"
    # If input does not match any known ingredient
    return "Please retype ingredient"



##
def get_ingredient_input():
    chosen_ingredients = []  # List to store chosen ingredients
    ####################
    
    
    while True:
        user_input = input("...")
        result = librarian_resource(user_input)
        ingredient = (result)  

        if ingredient in ["fire pie", "fire"]:
            return chosen_ingredients  # Stop and return list of chosen ingredients
        
        if ingredient in ingredient_check:
            chosen_ingredients.append(ingredient)
            
        else:
            print("No match man, please try again(:")

##the intro text for new players to describe the game


def intro(): 
    # Call the typewriter function to display text
    intro_text =("This game is designed to help pizza cooks on the line practice their side of our signature recipes.")
    wrapped_intro_text = textwrap.fill(intro_text, width=75)
    type_writer(wrapped_intro_text)
    #hooolllddd on
    load_ing("...")
    print("\nSo, we'll only request demonstration of knowledge up to Bake.")
    load_ing("  ")
    print("\nNo EXPO ingredients or additions will be covered Here.")
    print("\nlittle tip: if you don't know one, \njust fire anything and it will ask if you want to be told the recipe (;")
    load_ing("\n. . . . . . . . . . . . . . .")
    type_writer("\nLet's go!".center(65)) 
    print ("\nThe following list gives different short-hand codes for each ingredient, \n(to lessen your typing requirement.)".center(75))
    input("\n ")
    print("\nYou can type the shorthand provided, or the full given name listed below. \n(capitals are irrelevant)")
    input("")
    print ("\nUp to you. But!")
    time.sleep(1)
    print("Any other mistyped entries will not be recognized, \nand will throw up a note that the ingredient wasn't added to the pizza.".center(75))
    time.sleep(1)
    print("\nOther areas of input, like questions from the game about preferences, will accept a wide range of responses including just the first letter")
    print("\n(for example, 'fire' would accept 'f' and 'yes' or 'no' would register from just 'y' or 'n')")
    print("\nbut several longer written words and statements will work too, so have some fun with it!")
    time.sleep(2)
    



##do that delayed type-writing!


def type_writer(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Newline at the end

def load_ing(text, delay=0.30):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Newline at the end


# Recipe Timer
def start_timer():
    return time.time()

def end_timer(start_time):
    return round(time.time() - start_time)



   



##ingredient input handling missions

ingredients_table = [
    ("Red Sauce", "red"),
    ("Olive Oil-Garlic", "og"),
    ("Pesto Base", "pesto b"),
    ("Pesto Chicken", "pesto chkn"),
    ("Pesto Swirl", "pesto s"),
    ("Ranch Base", "ranch"),
    ("Herb Aioli", "herb"),
    ("Barbecue Chicken", "bbq chkn"),
    ("Barbecue Swirl", "bbq s"),
    ("Buffalo Chicken", "buff"),
    ("Jerk Chicken", "jerk"),
    ("Curry Chicken", "curry"),
    ("Shredded Mozzarella", "mz"),
    ("Cheddar", "ched"),
    ("White Cheddar", "white"),
    ("Provolone", "prov"),
    ("Ricotta", "ric"),
    ("Crumpled Feta", "feta"),
    ("Pepperoni", "pepp"),
    ("Bacon", "bac"),
    ("Ham", "ham"),
    ("Beef", "beef"),
    ("Italian Sausage", "sausage"),
    ("Grilled Chicken", "chkn"),
    ("Cooked Steak", "steak"),
    ("Salami", "sal"),
    ("Meatball", "mtbl"),
    ("Mushrooms", "mush"),
    ("Green Peppers", "gpep"),
    ("Onion", "on"),
    ("Black Olives", "olive"),
    ("Roma Tomato Slices", "roma"),
    ("Fresh Spinach", "spin"),
    ("Roasted Tomatoes", "roasted"),
    ("Mama Lil's Peppers", "mamas"),
    ("Garlic-Roasted Red Peppers", "grrp"),
    ("Artichoke Hearts", "arty"),
    ("Kalamata Olives", "kalamata"),
    ("Portobello", "porto"),
    ("Jalapenos", "japs"),
    ("Banana Peppers", "bpep"),
    ("Pineapple", "papple"),
    ("Mushroom Trio", "trio"),
    ("Caramelized Onions", "carmon"),
    ("Minced Garlic", "garlic"),
    ("Roasted Potatoes", "potat"),
    ("Vegan Mozzarella", "vmz"),
    ("Pepperoncini", "cini"),
]



# Function to print the table with fixed-width formatting in 4 columns
def display_ingredients(table):
    print("\n")
    print("\n")
    
    print("These are your ingredients, use them wisely!\n")

    # Define a fixed width for columns
    column_width = 22  
    separator = " | "  

    # Create the header
    header = f"{'Ingredient':<{column_width}}{separator}{'Shorthand':<{column_width}}{separator}" \
             f"{'Ingredient':<{column_width}}{separator}{'Shorthand':<{column_width}}"
    print("-" * len(header))  # Print a separator line
    print(header)  # Print the header
    print("-" * len(header))  # Print another separator line

    # Split table into two halves
    mid_index = math.ceil(len(table) / 2)  # Ensure even split if odd number of items
    first_half = table[:mid_index]
    second_half = table[mid_index:]

    # Pad second_half if it has fewer elements (so zip doesn't cut off)
    max_length = max(len(first_half), len(second_half))
    first_half += [("", "")] * (max_length - len(first_half))
    second_half += [("", "")] * (max_length - len(second_half))

    # Print ingredients in 4-column format
    for (ingredient1, shorthand1), (ingredient2, shorthand2) in zip(first_half, second_half):
        wrapped_ingredient1 = textwrap.shorten(ingredient1, width=column_width - 3, placeholder="...")
        wrapped_shorthand1 = textwrap.shorten(shorthand1, width=column_width - 3, placeholder="...")
        wrapped_ingredient2 = textwrap.shorten(ingredient2, width=column_width - 3, placeholder="...")
        wrapped_shorthand2 = textwrap.shorten(shorthand2, width=column_width - 3, placeholder="...")

        print(f"{wrapped_ingredient1:<{column_width}}{separator}{wrapped_shorthand1:<{column_width}}{separator}"
              f"{wrapped_ingredient2:<{column_width}}{separator}{wrapped_shorthand2:<{column_width}}")

    print("-" * len(header))  # Print a closing separator line








def check_recipe(chosen_ingredients, correct_recipe, recipe_name, elapsed_time):
   #Compares player's ingredients to the correct recipe and determines result#
    
    if chosen_ingredients == correct_recipe:
        print(f"\nPerfect! You made the {recipe_name} exactly right!")
        if recipe_name not in fastest_times or elapsed_time < fastest_times[recipe_name]:
            fastest_times[recipe_name] = elapsed_time  # Update fastest time
            print(f"\nAnd it took {elapsed_time} seconds, your current personal best!")  # New record!
        else:
            print(f"\nAnd it took {elapsed_time} seconds!")
        replay = input("\nLet it go?")
        if replay in ["y", "yes", "yse", "yses", "yeses", "yees", "yess", "yeess", "yeah", "ye", "sure", "yes please", "yeh", "please", "pls", "yep", "ready", "i guess", "go ahead", "ok", "okay", "k", "yiss", "aw yiss", "go", "bye", "seeya", "see ya", "let it go"]:
            print("This recipe is now removed from practice.")
            time.sleep(1)
            return "perfect"
        else:
            return
    
    
    elif sorted(chosen_ingredients) == sorted(correct_recipe):
        print("\nYou had all the right toppings, but not quite in the 'preferred' order. Still tasty!".center(65))
        if recipe_name not in fastest_times or elapsed_time < fastest_times[recipe_name]:
            fastest_times[recipe_name] = elapsed_time  # Update fastest time
            print(f"\nAnd it took {elapsed_time} seconds, your current personal best!")  # New record!
        else:
            print(f"\nAnd it took {elapsed_time} seconds!")
        print(f"\nThe shroomin arrangement for a {recipe_name} is: {' → '.join(correct_recipe)}")
        
        choice = input("\nReady to remove this recipe from practice, or nah? ").strip().lower()
        if choice in ["y", "yes","yse", "yses", "yeses", "yees", "yess", "yeess", "yeah", "ye", "sure", "yes please", "yeh", "please", "pls", "yep", "ready", "i guess", "go ahead", "ok", "okay", "k", "yiss", "aw yiss", "go", "bye", "seeya", "see ya", "let it go"]:
            
            print ("\nEy, they outty.")
            time.sleep(1)
            return "remove"
        else:
            print ("\nI gotchu")
            return "keep"
    
    else:
        print("\nFar Out! Your pizza had missing or extra ingredients. Keep trying!".center(65))
        input()
        inquiry = input("\n(Do you want a reminder what goes on it??)").strip().lower()
        if inquiry in ["y", "yes", "yse", "yses", "yeses", "yees", "yess", "yeess", "yeah", "ye", "sure", "yes please", "yeh", "please", "yep", "ready", "i guess", "go ahead", "ok", "okay", "k", "yiss", "aw yiss", "go"]:
            print(f"\nThat'll have, uh, {' → '.join(correct_recipe)} (;")
            
        else:
            print("Heard that")
            time.sleep(1)
        return replay_recipe(recipe_name, correct_recipe)



def replay_recipe(recipe_name, correct_recipe):
    while True:
        retry = input(f"\nRetry that one real quick?").strip().lower()
        
        if retry not in ["y", "yes", "yse", "yses", "yeses", "yees", "yess", "yeess", "yeah", "ye", "sure", "yes please", "yeh", "please", "yep", "ready", "i guess", "go ahead", "ok", "okay", "k", "yiss", "aw yiss", "go"]:
            print("Let's gooo")
            time.sleep(1)
            return "wrong" # Exits function correctly if player declines retry

        display_ingredients(ingredients_table)
        print(f"Alright, need a {recipe_name} on the fly!")

        chosen_ingredients = []


        chosen_ingredients = get_ingredient_input()
        result = check_replay(chosen_ingredients, correct_recipe, recipe_name)

        if result in ["perfect","remove"]:
            print("\nYou so got it now! Shuffling it back in.")
            time.sleep(2)
            return "wrong"  # Exit retry loop if the answer is correct without saving the recipe as correct in the whole game
        else:
            print("\nPut it on top of the oven and let's get back to it!".center(65))
            print ("\n ")
            time.sleep(3)
            return "wrong"

###
def check_replay(chosen_ingredients, correct_recipe, recipe_name):
   #Compares player's ingredients to the correct recipe and determines result#
    
    if chosen_ingredients == correct_recipe:
        print(f"\nThat's exactly right!")
        time.sleep(1)
        return "perfect"
       
    
    
    elif sorted(chosen_ingredients) == sorted(correct_recipe):
        print("\nThose ARE all the right toppings, though the schoox build chart will suggest".center(65))
        print(f"the shroomin arrangement for a {recipe_name} to be: {' → '.join(correct_recipe)}")
        time.sleep(1)
        return "remove"
    
    else:
        print (f"\nNo worries, that just gets: {' → '.join(correct_recipe)} (:")
    
        time.sleep(1)
        return "keep"
       


#signinfies game end


def close_program():
    print ("*~*").center(45)
    

##
def get_replay_input():
    while True:
        
        named = input ("\nEnter 'Replay' to play again, or 'End' to close the game!").strip().lower()
        if named in ["replay", "re", "r", "rep", "repl", "reapla", "repla", "replae", "rel", "again", "y", "yes", "play", "pl", "p", "go", "repeat", "play again", "menu", "restart", "repeat"]:
            return True
        elif named in ["nah", "na", "nope", "bye", "later", "laters", "exit", "finished", "end", "en", "done", "over", "no", "n", "leave", "finish", "fin", "ex", "e"]:
            print("\nThanks for hanging!")
            return False
        else:
            print("\nDidn't catch that..")
        
        
# Call this function when the player chooses "End"

#####
def main():
    #Main game loop where the player makes pizzas.#
    display_main_menu()


    while True:
        practice_recipes = recipes[:]  # List of recipes still in practice

        while practice_recipes:
            recipe = random.choice(practice_recipes)  # Pick a random recipe
            recipe_name = recipe ["name"]
            correct_recipe = recipe["ingredients"]  # Get correct ingredient list
####prompt start!

            
        #start game
            display_ingredients(ingredients_table)  # Show the ingredient list before each round
        #call order
            print(f"\nYou Got Hands? I need a {recipe_name}!".center(65))
            type_writer("Enter each ingredient one at a time. When finished, type 'Fire' Pie to submit.")
            start_time = start_timer()

            chosen_ingredients = get_ingredient_input()
            elapsed_time = end_timer(start_time)
        
            result = check_recipe(chosen_ingredients, correct_recipe, recipe_name, elapsed_time)

           

            if result in ["perfect", "remove"]:
                practice_recipes.remove(recipe)# Take the recipe out of practice

        print("\nNice! You've mastered all these recipes!")
        if not get_replay_input(): #will they play again
            break

    close_program()

def menu_answer():
    given = input ("Are you a 'New' Player or 'Seasoned' Player?").strip().lower()
    if given in ["new", "n", "ne", "nwe", "new player", "new p", "new pl", "new pla", "new play", "new playe", "noob"]:
        return "n"
    
    elif given in ["seasoned", "s", "se", "sea", "seas", "seaso", "season", "seasone", "seasoned p", "seasoned pl", "seasoned pla", "seasoned play", "seasoned playe", "seasoned player", "returning", "pro", "old"]:
        return "s"
    
    else:
        print("My bad, I can recognize a lot of responses here, but that isn't one of them.")
        return menu_answer()
        
    ##main menu time bruh
def display_main_menu():
    print("MELLOW MUSHROOM PIZZA BAKERS".center(77))
    time.sleep(1)
    print("Makeline Recipe Memory Practice".center(77))
    print("-" * 77)
    time.sleep(3)
    print("\nKeyboard Time! \n(Use 'Enter' to submit and progress)".center(77))
    choice = menu_answer()
    if choice == "n":
        intro()
        input("\nReady? Enter the Mellowverse!")
        return
    elif choice == "s":
        input("Ready? Enter the Mellowverse!")
        return





    
    display_main_menu()
    
    

# Run the game
if __name__ == "__main__":
    main()
