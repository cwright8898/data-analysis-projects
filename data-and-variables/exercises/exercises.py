# 1. Declare and assign the variables here:
shuttle_name = "Determination"
shuttle_speed_mph = 17500
km_to_mars = 225000000
km_to_moon = 384400
miles_per_km = 0.621
# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(km_to_mars))
print(type(km_to_moon))
print(type(miles_per_km))
# Code your solution to exercises 3 and 4 here:

miles_to_mars = km_to_mars * miles_per_km
hours_to_mars = miles_to_mars / shuttle_speed_mph
days_to_mars = hours_to_mars / 24
print(shuttle_name, "will take", days_to_mars, "days to reach the Mars" )
# Code your solution to exercise 5 here
miles_to_moon = km_to_moon * miles_per_km
hours_to_moon = miles_to_moon / shuttle_speed_mph
days_to_moon = hours_to_moon / 24
print(shuttle_name, "will take", days_to_moon, "days to reach the Moon" )

num = 7

if num % 2 == 0:
   if num % 2 == 1:
      print("odd") 




for j in range(5):
    print("Index:", j)