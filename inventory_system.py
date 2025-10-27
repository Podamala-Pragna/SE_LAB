"""Inventory Management System
This module provides basic functions to add, remove, save, and load inventory data.
Used for static code analysis lab demonstration.
"""

import ast

# Global dictionary to hold stock data
stock_data = {}


def add_item(item_name, quantity, items=None):
    """Add an item and its quantity to the inventory."""
    if items is None:
        items = []
    items.append({"item": item_name, "qty": quantity})
    print(f"✅ Added {item_name} ({quantity}) to inventory.")


def remove_item(item_name):
    """Remove an item from the inventory if it exists."""
    try:
        del stock_data[item_name]
        print(f"🗑️ Removed {item_name} from inventory.")
    except KeyError as e:
        print(f"⚠️ Item not found: {e}")


def get_qty(item_name):
    """Get the quantity of a given item."""
    return stock_data.get(item_name, "Item not found")


def load_data():
    """Load inventory data from a file."""
    global stock_data
    try:
        with open("inventory.txt", encoding="utf-8") as file:
            content = file.read()
            stock_data = ast.literal_eval(content)
        print("📦 Inventory data loaded successfully.")
    except FileNotFoundError:
        print("⚠️ File not found.")
    except Exception as e:
        print(f"❌ Error loading data: {e}")


def save_data():
    """Save current inventory data to a file."""
    with open("inventory.txt", "w", encoding="utf-8") as file:
        file.write(str(stock_data))
    print("💾 Inventory data saved successfully.")


def print_data():
    """Print the current inventory data."""
    print("📋 Current Inventory:")
    for item, qty in stock_data.items():
        print(f" - {item}: {qty}")


def check_low_items(threshold):
    """Check and display items with quantity below a threshold."""
    print(f"🔍 Items with quantity below {threshold}:")
    for item, qty in stock_data.items():
        if qty < threshold:
            print(f"⚠️ {item}: {qty}")


# Example usage for testing
if __name__ == "__main__":
    add_item("Laptop", 5)
    stock_data["Phone"] = 2
    print_data()
    check_low_items(3)
    save_data()
    load_data()
