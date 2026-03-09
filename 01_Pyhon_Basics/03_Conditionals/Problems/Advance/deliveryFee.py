"""
3. The Multi-Tiered Delivery Fee
Calculate shipping_cost based on distance (km), weight (kg), and is_fragile (bool).
Distance is the first gate—local vs. long distance.
Inside those distance gates, weight determines the base price.
Fragile items add a surcharge, but only if they are being shipped over a certain weight.
If the distance is too far (e.g., > 500km), we don't even look at weight; we just decline the shipment.
Goal: Calculate and print the total cost or "Declined."
"""

distance = float(input("Enter distance in km: "))
weight = float(input("Enter weight in kg: "))
fragile = str(input("is it fragile(Y/N): "))
is_fragile = fragile.lower() == "y"
if distance < 100:
    price = distance*(weight*10)# 10 per kg per km
    if is_fragile and weight > 10:
        price *= 1.2
    print(f"Final price = {price}")
elif distance <= 500:
    price = distance*(weight*9)# 9 per kg per km for long distance
    if is_fragile and weight > 10:
        price *= 1.3
    print(f"Final price = {price}")
else:
    print("Sorry we can't ship this far!") 
