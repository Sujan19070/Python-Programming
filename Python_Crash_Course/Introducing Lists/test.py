# Guest list
guests = ["Alice", "Bob", "Charlie", "David", "Eve"]

print("Original list:")
print(guests)

print("\nI can invite only two people for dinner.\n")

guests.pop()
print(f"Sorry, I can't invite you to dinner.")

guests.pop()
print(f"Sorry, I can't invite you to dinner.")

guests.pop()
print(f"Sorry, I can't invite you to dinner.")

print("\nFinal list:")
print(guests)