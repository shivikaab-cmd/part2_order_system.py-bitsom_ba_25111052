
# GIVEN DATA
menu = {
    "Paneer Tikka": {"category": "Starters", "price": 180.0, "available": True},
    "Chicken Wings": {"category": "Starters", "price": 220.0, "available": False},
    "Veg Soup": {"category": "Starters", "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains", "price": 320.0, "available": True},
    "Dal Tadka": {"category": "Mains", "price": 180.0, "available": True},
    "Veg Biryani": {"category": "Mains", "price": 250.0, "available": True},
    "Garlic Naan": {"category": "Mains", "price": 40.0, "available": True},
    "Gulab Jamun": {"category": "Desserts", "price": 90.0, "available": True},
    "Rasgulla": {"category": "Desserts", "price": 80.0, "available": True},
    "Ice Cream": {"category": "Desserts", "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka": {"stock": 10, "reorder_level": 3},
    "Chicken Wings": {"stock": 8, "reorder_level": 2},
    "Veg Soup": {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka": {"stock": 20, "reorder_level": 5},
    "Veg Biryani": {"stock": 6, "reorder_level": 3},
    "Garlic Naan": {"stock": 30, "reorder_level": 10},
    "Gulab Jamun": {"stock": 5, "reorder_level": 2},
    "Rasgulla": {"stock": 4, "reorder_level": 3},
    "Ice Cream": {"stock": 7, "reorder_level": 4},
}

# ===============================
# TASK 1 - MENU
# ===============================
categories = ["Starters", "Mains", "Desserts"]

for cat in categories:
    print("\n====", cat, "====")
    for item, details in menu.items():
        if details["category"] == cat:
            status = "Available" if details["available"] else "Unavailable"
            print(item, "-", details["price"], "-", status)

# stats
print("\nTotal items:", len(menu))

available_count = 0
for item in menu:
    if menu[item]["available"]:
        available_count += 1
print("Available items:", available_count)

# most expensive
max_price = 0
max_item = ""
for item in menu:
    if menu[item]["price"] > max_price:
        max_price = menu[item]["price"]
        max_item = item
print("Most expensive:", max_item, max_price)

# under 150
print("\nItems under 150:")
for item in menu:
    if menu[item]["price"] < 150:
        print(item, "-", menu[item]["price"])

# ===============================
# TASK 2 - CART
# ===============================
cart = []

def add_item(name, qty):
    if name not in menu:
        print("Item not found")
        return

    if not menu[name]["available"]:
        print("Item not available")
        return

    for c in cart:
        if c["item"] == name:
            c["quantity"] += qty
            return

    cart.append({
        "item": name,
        "quantity": qty,
        "price": menu[name]["price"]
    })

def remove_item(name):
    for c in cart:
        if c["item"] == name:
            cart.remove(c)
            return
    print("Item not in cart")

# simulate
add_item("Paneer Tikka", 2)
add_item("Gulab Jamun", 1)
add_item("Paneer Tikka", 1)
add_item("Mystery Burger", 1)
add_item("Chicken Wings", 1)
remove_item("Gulab Jamun")

print("\nCart:", cart)

# ===============================
# TASK 3 - INVENTORY
# ===============================
import copy

inventory_backup = copy.deepcopy(inventory)

inventory["Paneer Tikka"]["stock"] = 5

print("\nOriginal:", inventory["Paneer Tikka"])
print("Backup:", inventory_backup["Paneer Tikka"])

# reorder alert
for item in inventory:
    if inventory[item]["stock"] <= inventory[item]["reorder_level"]:
        print("Reorder:", item)

# ===============================
# TASK 4 - SALES LOG
# ===============================
sales_log = {
    "2025-01-01": [{"total": 220}, {"total": 210}],
    "2025-01-02": [{"total": 220}],
}

# revenue per day
for date in sales_log:
    total = 0
    for order in sales_log[date]:
        total += order["total"]
    print(date, "=", total)