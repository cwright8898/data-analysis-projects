my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
first_three = my_string[:3]
rest_of_string = my_string[3:]
string2 = rest_of_string + first_three
print(string2)


# Use a template literal to print the original and modified string in a descriptive phrase.
print(f"the original string was: '{my_string}' and the modified string was: '{string2}'")


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
my_string = input("Enter a string: ")
num_letters = int(input("How many letters should be moved from the start to the end? "))
new_string = my_string[num_letters:] + my_string[:num_letters]

print(f"The original string was '{my_string}' and the modified string is '{string2}'.")

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
my_string = input("Enter a string: ")
num_letters = int(input("How many letters should be moved from the start to the end? "))

if num_letters > len(my_string):
    original_input = num_letters
    num_letters = 3
    note = f" (input {original_input} was too large, so defaulted to 3 letters)"
else:
    note = ""
string2 = my_string[num_letters:] + my_string[:num_letters]

print(f"The original string was '{my_string}' and the modified string is '{string2}'{note}.")