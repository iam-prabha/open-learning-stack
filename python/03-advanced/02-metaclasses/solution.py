# solution.py - Metaclasses answers

# TODO 1: Dynamic class
MyDynamicClass = type('MyDynamicClass', (), {
    'hello': lambda self: "Greetings!"
})

# TODO 2: PrefixMeta
class PrefixMeta(type):
    def __new__(mcs, name, bases, attrs):
        new_attrs = {}
        for key, val in attrs.items():
            if not key.startswith('__'):
                new_attrs[f"attr_{key}"] = val
            else:
                new_attrs[key] = val
        return super().__new__(mcs, name, bases, new_attrs)

# TODO 3: Testing PrefixMeta
class Simple(metaclass=PrefixMeta):
    test = 42

# TODO 4: Singleton Metaclass
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# TODO 5: DatabaseConnection
class DatabaseConnection(metaclass=Singleton):
    def __init__(self):
        print("Initializing connection...")

# CHALLENGE: TraceMeta
class TraceMeta(type):
    def __new__(mcs, name, bases, attrs):
        for key, val in attrs.items():
            if callable(val) and not key.startswith('__'):
                def make_wrapper(func_name, func):
                    def wrapper(*args, **kwargs):
                        print(f"Entering method: {func_name}")
                        return func(*args, **kwargs)
                    return wrapper
                attrs[key] = make_wrapper(key, val)
        return super().__new__(mcs, name, bases, attrs)

class TracedTask(metaclass=TraceMeta):
    def run(self):
        return "Work done"

# --- Verification ---
print("--- Verification ---")
print(f"Dynamic class call: {MyDynamicClass().hello()}")
print(f"Prefixed attribute: {Simple.attr_test}")

print("\nTesting Singleton...")
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"db1 is db2? {db1 is db2}")

print("\nTesting TracedTask...")
t = TracedTask()
print(t.run())

print("\n--- Why it works ---")
print("1. Metaclass __new__: Modifies the class definition (adding/renaming attributes) before it is built.")
print("2. Metaclass __call__: Controls what happens when you 'call' the class (i.e., create an instance).")
print("3. Singleton: Storing the instance in a class-level dictionary ensures globally unique objects.")
print("4. Python magic: '__metaclass__' hook lets you intercept the very birth of a class.")
