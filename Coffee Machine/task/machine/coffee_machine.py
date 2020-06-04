total_available = 0
total_cups = int(input("Write how many cups of coffee you will need: "))
resources_available = {
    'machine_1': {
        "water": 1000,
        "milk": 1000,
        "beans": 1000,
    }
}

resources_needed = {
    'cup': {
        "water": 200,
        "milk": 50,
        "beans": 15,
    }
}


def order():
    print(f"For {total_cups} cups of coffee you will need: \n")
    for coffee, coffee_info in resources_needed.items():
        total_water = coffee_info['water'] * total_cups
        total_milk = coffee_info['milk'] * total_cups
        total_beans = coffee_info['beans'] * total_cups
        coffee_order = total_beans + total_water + total_milk
        print(f"{total_water} ml of water")
        print(f"{total_milk} ml of milk")
        print(f"{total_beans} g of coffee beans")

        if total_available == coffee_order:
            print(f"Yes I can make {total_cups} cups of coffee")
        elif coffee_order <= total_available:
            print(f"Yes I can make {total_cups} cups of coffee and even N more than that")
        else:
            print("No, I can make only N cups of coffee")
        return ()


def available():
    print("Supplies available in coffee machine:")
    for supply, machine_1_info in resources_available.items():
        water_available = machine_1_info['water']
        milk_available = machine_1_info['milk']
        beans_available = machine_1_info['beans']
        global total_available
        total_available = water_available + milk_available + beans_available
        print(f"{water_available} ml of water")
        print(f"{milk_available} ml of milk")
        print(f"{beans_available} g of beans")
        return total_available


available()
print()
order()
