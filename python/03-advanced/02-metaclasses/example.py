# example.py - Metaclasses in Python

# 1. Classes are objects!
class MyClass:
    pass

print(f"Type of MyClass instance: {type(MyClass())}")
print(f"Type of MyClass itself: {type(MyClass)}") # Output: <class 'type'>

# 2. Creating a class dynamically using type()
# type(name, bases, dict)
DynamicGreeting = type('DynamicGreeting', (), {'greet': lambda self: "Hello from dynamic class!"})
d = DynamicGreeting()
print(f"\nDynamic call: {d.greet()}")

# 3. Defining a custom Metaclass
class AutoAttributeMeta(type):
    """A metaclass that automatically adds a 'created_at' attribute to all its classes."""
    def __new__(mcs, name, bases, attrs):
        import datetime
        # attrs is the dictionary of attributes defined in the class body
        attrs['created_at'] = datetime.datetime.now().isoformat()
        # call the parent __new__ to actually create the class object
        return super().__new__(mcs, name, bases, attrs)

class User(metaclass=AutoAttributeMeta):
    pass

class Product(metaclass=AutoAttributeMeta):
    pass

print("\n--- Custom Metaclass ---")
u = User()
p = Product()
print(f"User created at: {u.created_at}")
print(f"Product created at: {p.created_at}")

# 4. Enforcing naming conventions
class FinalClassMeta(type):
    """Enforces that all attributes must be lowercase."""
    def __new__(mcs, name, bases, attrs):
        for attr_name in attrs:
            if not attr_name.startswith('__') and not attr_name.islower():
                raise TypeError(f"Attribute '{attr_name}' must be lowercase in class {name}")
        return super().__new__(mcs, name, bases, attrs)

print("\n--- Validation Metaclass ---")
try:
    class BadClass(metaclass=FinalClassMeta):
        ValidAttr = 10 # This will trigger the TypeError
except TypeError as e:
    print(f"Caught validation error: {e}")
