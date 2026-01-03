# static array , Dynamic array and string
# O(1) - instant operation , O(n) - lookup operation

a = [1, 2, 3, 4, 5]

# append - insert at the end - O(1)
a.append(6)
print(f"Append array: {a}")

# pop - remove at the end - O(1)
a.pop()
print(f"removed at end: {a}")

# insert ( not at the end ) - O(n)
a.insert(2, 4)
print(f"inserted in specific index: {a}")
# accessing element given index 2 - O(1)
print(f"Access array at index: {a[2]}")

# modify an element - O(1)
a[0] = 2
print(f"modify array at index of 0th: {a}")

# check length of array - O(1)
print(f"check length of the array: {len(a)}")

# Strings

# Append to end of string - O(n)
s = "hello"

b = s + "z"  # It's append with new variable
print(f"Append string at end with new variable: {b}")

# Check if something is in string - O(n)
if "e" in s:
    print(True)

# Access positions - O(1)
print(f"Access string at index(like array/list): {s[2]}")

# Check length of string - O(1)
print(f"check length of string: {len(s)}")
