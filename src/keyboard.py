from src.item import Item

class Mixinlang:
    def __init__(self, language="EN"):
        self.language = language


    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
            return self
        elif self.language == "RU":
            self.language = "EN"
            return self


class KeyBoard(Item, Mixinlang):
    def __init__(self, name, price, quantity, language="EN"):
        self.language = language
        super().__init__(name, price, quantity)

