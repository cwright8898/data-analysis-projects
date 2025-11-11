from operator import index


food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_list = sorted(food.split(","))
equipment_list = sorted(equipment.split(","))
pets_list = sorted(pets.split(","))
sleep_aids_list = sorted(sleep_aids.split(","))

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [food_list, equipment_list, pets_list, sleep_aids_list]
print(cargo_hold)


# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.

cabinet_index = int(input("select cabinet number(0-3): "))


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
if cabinet_index <= 0 or cabinet_index > 3:
    print("Error: select valid cabinet number")
else:
    print(f"the contents of cabinet, {cabinet_index}: {cargo_hold[cabinet_index]}")


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check 
# if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”

item = input('Enter an item check: ')
if item in cargo_hold[cabinet_index]:
    print(f"cabinet {cabinet_index} does contain {item}")
else:
    print(f"cabrinet {cabinet_index} does not contain {item}")
