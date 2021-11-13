import itertools
from json import JSONEncoder, JSONDecodeError, loads, dump, JSONDecoder
# define the Encoder class used in serialization
import orders


class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__

    # define the Order class, which is the base class for all the  products in the store

class Decoder(JSONDecoder):
    """ We have to transform the serialized string into Python objects"""

    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        cat = Order(*vals)
        return cat


class Order:
    id_iter = itertools.count()

    def __init__(self, products: dict, address: str):
        self.id = next(self.id_iter)
        self.products = products
        self.address = address

    def __eq__(self, other):
        """ Overloaded in order to verify the membership inside a collection """
        return self.id == other.id

    @staticmethod
    def write_to_file(product, address):
        orders.Orders.add_order(Order(product, address))
