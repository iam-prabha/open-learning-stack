# example.py - Type Hints in Python

from __future__ import annotations # allows forward references
from typing import List, Dict, Optional, Union, Callable, Protocol, Any

# 1. Basic annotations
name: str = "Alice"
age: int = 30
is_active: bool = True

def greet(name: str) -> str:
    return f"Hello, {name}"

print("--- Basic Types ---")
print(greet(name))

# 2. Collections (List, Dict, Tuple)
numbers: List[int] = [1, 2, 3]
config: Dict[str, Any] = {"version": 1, "enabled": True}

def process_list(items: List[float]) -> float:
    return sum(items)

# 3. Optional and Union
# Optional[int] is shorthand for Union[int, None]
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

def stringify(value: Union[int, float, str]) -> str:
    return str(value)

print("\n--- Optional & Union ---")
print(f"User 1: {find_user(1)}")
print(f"User 99: {find_user(99)}")
print(f"Stringified: {stringify(123.45)}")

# 4. Callable (Typing functions as arguments)
def execute_task(task: Callable[[int, int], int], a: int, b: int) -> int:
    return task(a, b)

add: Callable[[int, int], int] = lambda x, y: x + y
print("\n--- Callable ---")
print(f"Result: {execute_task(add, 5, 10)}")

# 5. Protocol (Structural Subtyping / Duck Typing)
# A class satisfies a Protocol if it has the required methods,
# regardless of inheritance.
class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing a circle O")

class Square:
    def draw(self) -> None:
        print("Drawing a square []")

def render(item: Drawable) -> None:
    item.draw()

print("\n--- Protocol ---")
render(Circle())
render(Square())
