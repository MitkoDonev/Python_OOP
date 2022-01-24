class Language:
    def say_hello(self):
        raise NotImplementedError("Please say_hello class in child class!")


class Bulgarian(Language):
    pass


class French(Language):
    def say_hello(self):
        print("Bonjour")


class Chinese(Language):
    def say_hello(self):
        print("Ihaaa")


def intro(lang):
    lang.say_hello()


steve = French()
john = Chinese()
mitko = Bulgarian()

intro(steve)
intro(john)
intro(mitko)
