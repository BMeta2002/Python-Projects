class RetailItems:
    def __init__(self, item_description, unit_in_inventory, price):
        self.__item_description = item_description
        self.__unit_in_inventory = unit_in_inventory
        self.__price = price

    # Magic Method
    def __str__(self):
        return f"Description: {self.get_item_description()}\n" \
               f"Units in inventory: {self.get_unit_in_inventory()}\n" \
               f"Price: ${self.get_price():.2f}\n" \


    # Accessors and Mutators
    def set_item_description(self, item_description):
        self.__item_description = item_description

    def set_unit_in_inventory(self, unit_in_inventory):
        self.__unit_in_inventory = unit_in_inventory

    def set_price(self, price):
        self.__price = price

    def get_item_description(self):
        return self.__item_description

    def get_unit_in_inventory(self):
        return self.__unit_in_inventory

    def get_price(self):
        return self.__price
