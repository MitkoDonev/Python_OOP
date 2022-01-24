METHODS = ["stripe", "paypal", "braintree"]


class Payment:
    def __init__(self, method):
        self.__method = method

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, new_method):
        if new_method in METHODS:
            self.__method = new_method

    @method.deleter
    def method(self):
        self.__method = None


pay = Payment("striple")
print(pay.method)
pay.method = "paypal"
print(pay.method)
pay.method = "xxxxxxxxxxxx"
print(pay.method)
del pay.method
print(pay.method)
