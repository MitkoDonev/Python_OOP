class Payment:
    def __init__(self, price) -> None:
        self.__final_price = price + price * 0.05

    def get_final_price(self):
        return self.__final_price

    def set_final_price(self, discount):
        self.__final_price = self.__final_price - self.__calculate_discount(discount)

    def __calculate_discount(self, discount):
        return self.__final_price * (discount / 100)


book = Payment(10)
print(book.get_final_price())
book.set_final_price(20)
print(book.get_final_price())
