# class Test:
#     pass

class BaseClass:
    def show(self):
        return "hello"
    
def add_attribute(self):
    self.b = 10

# Dynamically create a class with type()
Test = type("Test", (BaseClass,), {"a": 5, "add_attribute": add_attribute})
t = Test()

result = t.show()          # Calls BaseClass.show() => "hello"
result = t.a               # Access attribute 'a' => 5
t.add_attribute()          # Adds 'b' attribute dynamically
result = t.b               # Access new attribute => 10

print(result)


# Custom metaclass that uppercases public attribute names
class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        modified_attrs = {}

        for name, val in attrs.items():
            if name.startswith("_"):
                modified_attrs[name] = val
            else:
                modified_attrs[name.upper()] = val

        return type(class_name, bases, modified_attrs)

class Person(metaclass=Meta):
    x = 5
    y = 10
    _age = 40

    def hello(self):
        print("hello")

p = Person()

result = p.X        # Access capitalized attribute
result = p.Y        # Access capitalized attribute
result = p._age     # Access private attribute (unchanged)

print(result)
