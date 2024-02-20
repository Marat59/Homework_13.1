class Category:
    name: str
    description: str
    goods: list

    count_category = 0
    count_unique_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.count_category += 1
        Category.count_unique_products += 1

    @property
    def goods(self):
        return self.__goods

    def add_goods(self, product):
        self.__goods.append(product)

    @property
    def get_product(self):
        current_list = []
        for product in self.__goods:
            current_list.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')
        return current_list
