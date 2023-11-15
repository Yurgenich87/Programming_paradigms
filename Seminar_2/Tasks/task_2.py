def say_hello():  # Это подпрограмма
    print("Привет!")


def show_message(message):  # Это процедура
    print(message)


show_message("Это сообщение.")


def add(a, b):
    return a + b


result = add(3, 4)
print(result)


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} говорит: Гав!!!")


dog = Dog("Бобик")
dog.bark()
