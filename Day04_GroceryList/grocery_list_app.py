grocery_list = []

print("Welcome to the Grocery List App!")
print("Type 'done' to finish.\n")

while True:
    item = input("Enter an item to add: ")
    if item.lower() == 'done':
        break
    grocery_list.append(item)

print("\nYour Grocery List:")
for i, item in enumerate(grocery_list, start=1):
    print(f"{i}. {item}")
