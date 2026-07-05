# Fantasy Games Inventory
stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1,"arrow": 3}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
        item_total = item_total + v
    print("Total number of items:", str(item_total))

displayInventory(stuff)

# List to Dictionary Function For Fantasy Games Inverntory
def addToInventory(inventory, addeditems):
    for item in addeditems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory
 
ivn = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "degger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(ivn, dragonLoot)
displayInventory(inv)