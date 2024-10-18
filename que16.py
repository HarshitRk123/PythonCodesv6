def prepare_grocery_bill():
    total_amount = 0
    items = []
    
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        try:
            quantity = int(input(f"Enter quantity for {item_name}: "))
            price_per_unit = float(input(f"Enter price per unit for {item_name}: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for quantity and price.")
            continue
        item_total = quantity * price_per_unit
        total_amount += item_total
        items.append((item_name, quantity, price_per_unit, item_total))
    print("\nGrocery Bill:")
    print("-" * 30)
    print(f"{'Item':<15} {'Quantity':<10} {'Price/Unit':<10} {'Total':<10}")
    print("-" * 30)
    
    for item in items:
        name, qty, price, total = item
        print(f"{name:<15} {qty:<10} {price:<10.2f} {total:<10.2f}")
    
    print("-" * 30)
    print(f"{'Total Amount':<35} {total_amount:<10.2f}")
prepare_grocery_bill()
