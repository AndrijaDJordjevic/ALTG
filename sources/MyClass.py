import re

class FirstPage:
    def __init__(self):
        self.project_info = ""
        self.address = ""
        self.client = ""
        self.date = ""
        self.lot_cfc = ""
        self.total_brut = 0.0
        self.prorata = 0.0
        self.total_hors_tva = 0.0
        self.tva = 0.0
        self.total_ttc = 0.0
    
    def __repr__(self):
        return f"FirstPage(total_brut={self.total_brut}, prorata={self.prorata}, total_hors_tva={self.total_hors_tva}, tva={self.tva}, total_ttc={self.total_ttc})"

class LastPage:
    def __init__(self):
        self.summary = ""
        self.total_net_ht = 0.0
        self.total_tva = 0.0
        self.total_net_ttc = 0.0
    
    def __repr__(self):
        return f"LastPage(total_net_ht={self.total_net_ht}, total_tva={self.total_tva}, total_net_ttc={self.total_net_ttc})"

class LineItem:
    def __init__(self, description, quantity, unit_price, total_price):
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = total_price
    
    def __repr__(self):
        return f"LineItem(description={self.description}, quantity={self.quantity}, unit_price={self.unit_price}, total_price={self.total_price})"

class MiddlePage:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def __repr__(self):
        return f"MiddlePage(items={self.items})"

