# Program to calculate weight on Earth and Moon

mass = float(input("Enter mass of object in kg: "))

earth_gravity = 9.8
moon_gravity = 1.62

earth_weight = mass * earth_gravity
moon_weight = mass * moon_gravity

print("Weight on Earth =", earth_weight, "N")
print("Weight on Moon =", moon_weight, "N")
