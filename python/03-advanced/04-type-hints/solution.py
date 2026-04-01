# solution.py - Type Hints answers

from typing import List, Dict, Optional, Union, Callable, Any, Protocol

# TODO 1
def sum_list(nums: List[int]) -> int:
    return sum(nums)

# TODO 2
user_data: Dict[str, Any] = {"id": 1, "username": "admin"}

# TODO 3
def get_first_element(items: List[str]) -> Optional[str]:
    return items[0] if items else None

# TODO 4
def parse_id(val: Union[int, str]) -> int:
    return int(val)

# TODO 5
def apply_math(x: int, func: Callable[[int], int]) -> int:
    return func(x)

# TODO 6
class User:
    def __init__(self, username: str, age: Optional[int] = None) -> None:
        self.username = username
        self.age = age

# CHALLENGE
class Flyable(Protocol):
    def fly(self) -> str: ...

class Plane:
    def fly(self) -> str: return "Propellers spinning"

class Bird:
    def fly(self) -> str: return "Wings flapping"

def launch(item: Flyable) -> None:
    print(item.fly())

# --- Verification ---
print("--- Verification ---")
print(f"sum_list([1, 2, 3]): {sum_list([1, 2, 3])}")
print(f"parse_id('123'): {parse_id('123')}")
print(f"apply_math(5, lambda x: x*x): {apply_math(5, lambda x: x*x)}")

bird = Bird()
plane = Plane()
launch(bird)
launch(plane)

print("\n--- Why it works ---")
print("1. Runtime: Python ignores these hints; performance is unchanged.")
print("2. Tooling: Mypy reads these to find logic bugs without running code.")
print("3. Optional[T]: Explicitly says 'T or None' — prevents unexpected NoneErrors.")
print("4. Protocol: Enables 'static duck typing'. A class doesn't need to inherit from Flyable to be Flyable.")
