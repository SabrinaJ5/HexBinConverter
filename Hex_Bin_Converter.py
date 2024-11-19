"""
Author: Sabrina Joseph
Date: 02-21-2024
Last Modified: 02-21-2024
Description: Lab 5A - Numeric Conversion
"""


def hex_char_decode(x): # letter conversions
    hex_map_lower = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    # this is my uppercase hex map
    x_lower = x.lower()
    x_upper = x.upper()
    for i in range(len(hex_map_lower)):
        if hex_map_lower[i] == x_lower or hex_map_lower[i] == x_upper:
            return i


# function for the first option
def hex_string_decode(x):
    # Check if the string starts with '0x' and remove it if present
    if len(x) >= 2 and x[0] == '0' and x[1] == 'x':
        x = x[2:]
    # creating a new list with the new converted characters
    decoded_list = []
    for char in x:
        decoded_list.append(hex_char_decode(char))
    # this is where I am now converting the decoded list to the decimal value
    deci_val = 0
    for i in range(len(decoded_list)):
        digit = decoded_list[i]
        deci_val = deci_val * 16 + digit
    return deci_val


# function for the second option
def binary_string_decode(x):
    deci_val = 0
    pwr = len(x) - 1
    for i in range(len(x)):
        digit = x[i]
        # this line is checking if there is a one in that place, if there is, it will be counted
        if digit == '1':
            deci_val += 2 ** pwr
        pwr -= 1
    return deci_val

# function for the third option


def binary_to_hex(x):
    # Convert binary to decimal
    deci_val = 0
    for digit in x:
        deci_val = deci_val * 2 + int(digit)

    # Convert decimal to hexadecimal
    hex_chars = "0123456789ABCDEF"
    hex_str = ""
    while deci_val > 0:
        remainder = deci_val % 16
        hex_str = hex_chars[remainder] + hex_str
        deci_val //= 16

    return hex_str


while True:
    # displaying the menu
    print("Decoding Menu\n"
          "-------------\n"
          "1. Decode hexadecimal\n"
          "2. Decode binary\n"
          "3. Convert binary to hexadecimal\n"
          "4. Quit\n")
    option = int(input("Please enter an option: "))

    while option == 1 or option == 2 or option == 3 or option == 4:

        # Option 1
        if option == 1:
            # getting the numeric string from user
            code = input("Please enter the numeric string to convert: ")
            hex_string = hex_string_decode(code)
            print(f"Result: {hex_string}\n")

        # Option 2
        elif option == 2:
            # getting the numeric string from user
            code = input("Please enter the numeric string to convert: ")
            binary_string = binary_string_decode(code)
            print(f"Result: {binary_string}\n")

        # Option 3
        elif option == 3:
            # getting the numeric string from user
            code = input("Please enter the numeric string to convert: ")
            binary_string = binary_to_hex(code)
            print(f"Result: {binary_string}\n")

        # Option 4
        elif option == 4:
            exit()

        break
    continue
