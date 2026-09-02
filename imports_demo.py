# from openai import OpenAI


# client = OpenAI()

# print(type(OpenAI))
# print(type(client))

# class Person:
#     pass

# print(type(Person))

# jasman = Person()

# print(type(jasman))


class Person:

    def __init__(self):
        self.name = "Jasman"

    def greet(self):
        print(f"Hello {self.name}")


p = Person()

print(p.name)

p.greet()