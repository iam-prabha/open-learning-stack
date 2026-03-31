# example.py - Demonstration of for and while loops

# 1. for loop over a sequence (list)
fruits = ["apple", "banana", "cherry"]
print("--- Iterating over a list ---")
for fruit in fruits:
    print(f"I like {fruit}")

# 2. for loop with range()
# range(start, stop, step)
print("\n--- Using range() ---")
for i in range(3):
    print(f"Loop count: {i}")

# 3. while loop
count = 3
print("\n--- while loop ---")
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Blast off!")

# 4. break and continue
print("\n--- break and continue ---")
for num in range(1, 10):
    if num == 3:
        print("Skipping 3 (continue)")
        continue
    if num == 7:
        print("Stopping at 7 (break)")
        break
    print(f"Number: {num}")

# 5. Iterating with index using enumerate()
print("\n--- Using enumerate() ---")
for index, fruit in enumerate(fruits):
    print(f"Rank {index+1}: {fruit}")
