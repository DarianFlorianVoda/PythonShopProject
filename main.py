from category import Category
from categories import Categories
from product import Product
from products import Products
from json import JSONDecodeError


# define some functions to be used in the main menu. You can follow the
# suggestion described in the lab requirement, by simulating a switch
# instruction using a dictionary, or just using multiple 'if' branches
# which is, obviously, much uglier
def function(main_select):
    second_menu = {1: "Add a", 2: "Remove a", 3: "Display all"}
    return '\n'.join(f"{k}: {v} {main_select}" for k, v in second_menu.items())

def add_category(text):
    print(f"Please name the {text}: ")
    text2 = input()
    if text == "Category":
        Categories.add_category(text2)
    elif text == "Product":
        Products.add_product(text2)

#TODO: think about orders class, serialization on txt, set price, materials and others for category, product and order


def delete_category(text):
    print(f"Please refer to the name of the {text}: ")
    text2 = input()
    Categories.remove_category(text2)


def display_categories(text):
    for i in Categories.load_categories():
        print(i.name)


def error_handler():
    print("This option does not exist")


def Exit():
    return "Thank you for your visit, please come back soon!"


if __name__ == "__main__":
    menus = {1: add_category, 2: delete_category, 3: display_categories, 4: Exit.__name__}
    main_menu = {1: "Category", 2: "Product", 3: "Order", 4: Exit.__name__}
    while (True):
        print("Welcome to Dari Shop! Please choose an option\n")
        print('\n'.join(f"{k}: {v}" for k, v in main_menu.items()))
        option = int(input("Enter your option: "))
        func = main_menu.get(option, error_handler)
        try:
            func()
        except:
            if func == Exit.__name__:
                print(Exit())
                break
            else:
                print(function(func))
                option2 = int(input("Enter your option: "))
                func2 = menus.get(option2, error_handler)
                try:
                    func2()
                except:
                    func2(func)

        break
    # below some usage examples

    # create some categories
    cat_1 = Category("Necklaces")
    cat_2 = Category("Bracelets")
    cat_3 = Category("Earrings")
    prod_1 = Product("Keas Kalvin Kelin")

    # add them inside the Categories collection, and also save them
    # on the disk
    Categories.add_category(cat_1)
    Categories.add_category(cat_2)
    Categories.add_category(cat_3)

    # display the existing categories
    try:
        categories = Categories.load_categories()
        for cat in categories:
            print(cat.name)
    except JSONDecodeError as e:
        categories = None

    # remove one category from the Categories collection
    Categories.remove_category(cat_3)

    # display again the existing categories
    for cat in categories:
        print(cat.name)
