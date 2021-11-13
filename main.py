import order
import product
from orders import Orders

from category import Category
from categories import Categories
from product import Product, Necklace, Bracelet, Earring
from products import Products
from json import JSONDecodeError


# define some functions to be used in the main menu. You can follow the
# suggestion described in the lab requirement, by simulating a switch
# instruction using a dictionary, or just using multiple 'if' branches
# which is, obviously, much uglier
"""
IMPORTANT NOTE TO READ:
Dear reader/teacher,
When I've started this project was at 4 AM when I hadn't sleep and I started reading everything regarding the project up to 2 hours.
After those 2 hours, I started coding and making progress. Thus, being involved in multiple cynical, madness and insanity,
I did it. My eyes are burning like spicy chips with Wasabi, but after this long time of over 10 hours of non-stop coding and practicing,
I realized that the true power of the code is not being smart, but being a fighter.
So, to make my words understandable, this code was completed and written starting from 6AM
And then, only me and God knew why is it working. Now only God knows.

As my human brain was murdering me with constant need of sleep, I was taking very important progress
with one of my favorite colleagues which I respect him for helping me out for some guidelines.

If you do not understand some part of the code, or if you think it is very very messy, that was
the initial plan of designing my code from the beginning. It works on several tips and tricks learned from the University slides
and I applied them in order to see if it works. And yes, they work.

If there are any questions regarding this project, please don't hesitate to contact me through email.
Have a great day!
Darian
"""

def function(main_select):
    if main_select == "Category" or main_select == "Product":
        second_menu = {1: "Add a", 2: "Remove a", 3: "Display all"}
        return '\n'.join(f"{k}: {v} {main_select}" for k, v in second_menu.items())
    else:
        second_menu = {1: "Add a", 3: "Display all"}
        return '\n'.join(f"{k}: {v} {main_select}" for k, v in second_menu.items())


def add_category(text):
    if text == "Order":
        ordering = dict()
        display_categories("Product")
        print("\n Exit")
        choice = input("Select your choice:")
        if choice == "Exit":
            return
        quantity = int(input("Select the quantity:"))
        if choice not in ordering:
            ordering[choice] = quantity
        else:
            ordering[choice] = order[choice] + quantity
        while choice != "Exit:":
            if choice == "Exit":
                return
            more = int(input("Do you want more items?\n 1. Yes\n 2. No\nYour choise: "))
            if more == 1:
                pass
            elif more == 2:
                break
            else:
                pass
            display_categories("Product")
            choice = input("Select your choice:")
            quantity = int(input("Select the quantity:"))
            if choice not in ordering:
                ordering[choice] = quantity
            else:
                ordering[choice] = order[choice] + quantity
        address = input("Enter your address:")
        item = order.Order(ordering, address)
        item.write_to_file(ordering, address)
    else:
        print(f"Please name the {text}: ")
        text2 = input()
        if text == "Category":
            Categories.add_category(Category(text2))
        elif text == "Product":
            list_products = {"Product": Product, "Necklace": Necklace, "Bracelets": Bracelet, "Earring": Earring}
            display_categories("Category")
            category_list = Categories.categories
            text3 = input("Please enter a category: ")
            while Category(text3) not in category_list:
                text3 = input("Please enter a valid(!) category: ")
            item = list_products.get(text3, Product)
            item.write_to_file(text2)
        elif text == "Order":
            pass


def delete_category(text):
    display_categories(text)
    print(f"Please refer to the name of the {text}: ")
    text2 = input()
    if text == "Category":
        Categories.remove_category(Category(text2))
    elif text == "Product":
        Products.remove_product(Product(text2, Category("Text")))


def display_categories(text):
    print("-" * 20)
    if text == "Category":
        for i in Categories.categories:
            print("Category name: " + i.name)
    elif text == "Product":
        for i in Products.products:
            print("Product name: " + i.name)
    elif text == "Order":
        for i in Orders.orders:
            print("Order number: " + str(i.id))
    print("-" * 20)


def error_handler():
    print("This option does not exist")


def Exit():
    return "Thank you for your visit, please come back soon!"


if __name__ == "__main__":
    Categories.load_categories()
    Products.load_products()
    Orders.load_orders()
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
    prod_1 = Product("Keas Kalvin Kelin", cat_1)

    # add them inside the Categories collection, and also save them
    # on the disk
    Categories.add_category(cat_1)
    Categories.add_category(cat_2)
    Categories.add_category(cat_3)

    # # display the existing categories
    # try:
    #     categories = Categories.load_categories()
    #     for cat in categories:
    #         print(cat.name)
    # except JSONDecodeError as e:
    #     categories = None
    # # remove one category from the Categories collection
    # Categories.remove_category(cat_3)
    # # display again the existing categories
    # for cat in categories:
    #     print(cat.name)
