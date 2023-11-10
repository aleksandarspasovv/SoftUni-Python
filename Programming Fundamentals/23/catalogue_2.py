class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [word for word in self.products if word.startswith(first_letter)]

    def __repr__(self):
        sorted_list = sorted(self.products, key=lambda x: x.lower())
        item = "\n".join(self.products)
        return f"Items in the {self.name} catalogue:{item}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
