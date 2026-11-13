# Lunch menu app: 5 fake restaurants, 2 dishes each (name, price, tags).
# MY COMMENT restaurants is a collection. In this collection is dictionary and lists and tuples.
restaurants = {
    "Pasta Place": [
        ("Mushroom Risotto", 9.50, ["mushrooms", "dairy"]),
        ("Spaghetti Bolognese", 10.00, ["gluten", "meat"]),
    ],
    "Green Bowl": [
        ("Falafel Wrap", 7.50, ["gluten", "vegan"]),
        ("Quinoa Salad", 8.00, ["vegan", "nuts"]),
    ],
    "Burger Barn": [
        ("Classic Burger", 11.00, ["gluten", "meat"]),
        ("Mushroom Swiss Burger", 12.50, ["gluten", "meat", "mushrooms"]),
    ],
    "Sushi Spot": [
        ("Salmon Roll", 9.00, ["fish"]),
        ("Veggie Roll", 7.00, ["vegan"]),
    ],
    "Taco Town": [
        ("Beef Taco", 6.50, ["meat", "spicy"]),
        ("Mushroom Quesadilla", 8.50, ["mushrooms", "dairy", "gluten"]),
    ],
}

# Ask for a filter, like "no mushrooms" or "gluten".
# MY COMMENT This filter uses ingredients to filter dishes. 
user_filter = input("Filter (for example 'no mushrooms' or 'gluten'): ").strip().lower()

# Find the tag we care about, and whether the dish should have it or not.
if user_filter.startswith("no "):
    tag = user_filter[3:]
    want_tag = False
else:
    tag = user_filter
    want_tag = True

# Check every dish and print the ones that match.
for restaurant, dishes in restaurants.items():
    for name, price, tags in dishes:
        has_tag = tag in tags
        if has_tag == want_tag:
            print(f"{restaurant}: {name} - {price:.2f}")

# Wait for Enter so the window does not close right away.
# MY COMMENT This input is needed to close app. Without this input, the app closes immediately after prining the results.
input("Press Enter to close...")
