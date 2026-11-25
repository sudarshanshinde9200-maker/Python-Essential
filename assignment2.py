EARTH_GRAVITY = 9.81
MOON_GRAVITY = 1.62

def calculate_weight(mass, gravity):
    weight = mass * gravity
    return weight

mass = float(input("Enter mass in kg: "))

if mass >= 0:
    print("Weight on Earth:",
          calculate_weight(mass, EARTH_GRAVITY), "N")

    print("Weight on Moon:",
          calculate_weight(mass, MOON_GRAVITY), "N")
else:
    print("Invalid mass")