from json import JSONEncoder, JSONDecoder, loads
import category
import products


# define the Encoder class used in serialization
class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__

    # define the Product class, which is the base class for all the  products in the store


class Decoder(JSONDecoder):
    """ We have to transform the serialized string into Python objects"""

    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        if data['category']['name'] == "Bracelet":
            cat = Bracelet(*vals)
        elif data['category']['name'] == "Necklace":
            cat = Necklace(*vals)
        elif data['category']['name'] == "Earring":
            cat = Earring(*vals)
        else:
            cat = Product(*vals)
        return cat


class Product:
    def __init__(self, name, category: category.Category):
        self.name = name
        self.category = category

    @staticmethod
    def write_to_file(name):
        products.Products.add_product(Product(name, category.Category("Brand")))

    def __eq__(self, other):
        """ Overloaded in order to verify the membership inside a collection """
        return self.name == other.name

class Necklace(Product):
    def __init__(self, name, category, color: str, material: str, length: int):
        super().__init__(name, category)
        self.color = color
        self.material = material
        self.length = length

    @staticmethod
    def write_to_file(name):
        color = input("Color: ")
        material = input("Material: ")
        length = int(input("Length: "))
        products.Products.add_product(Necklace(name, category.Category("Necklace"), color, material, length))


class Bracelet(Product):
    def __init__(self, name, category, color: str, weight: int):
        super().__init__(name, category)
        self.color = color
        self.weight = weight

    @staticmethod
    def write_to_file(name):
        color = input("Color: ")
        weight = int(input("Weight: "))
        products.Products.add_product(Bracelet(name, category.Category("Bracelet"), color, weight))


class Earring(Product):
    def __init__(self, name, category, material: str, length: int, weight: int):
        super().__init__(name, category)
        self.material = material
        self.length = length
        self.weight = weight

    @staticmethod
    def write_to_file(name):
        material = input("Material: ")
        length = int(input("Length: "))
        weight = int(input("Weight: "))
        products.Products.add_product(Earring(name, category.Category("Earring"), material, length, weight))
