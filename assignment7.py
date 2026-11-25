def calculate_calories(carbs, fats, proteins):
    total = (carbs * 4) + (fats * 9) + (proteins * 4)
    return total

carbs = float(input("Enter carbs in grams: "))
fats = float(input("Enter fats in grams: "))
proteins = float(input("Enter proteins in grams: "))

if carbs < 0 or fats < 0 or proteins < 0:
    print("Invalid input")
else:
    calories = calculate_calories(carbs, fats, proteins)
    print("Total Calories:", calories)