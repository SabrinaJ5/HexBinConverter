# Numeric Conversion Lab

## About the Project

This project was created as part of **Lab 5A** for my **Programming Fundamentals 1** class at the **University of Florida**. The objective of this assignment was to develop a program that decodes hexadecimal and binary numeric strings, as well as converts binary strings into hexadecimal.

The program offers users the following functionalities:
1. Decode a hexadecimal string to its decimal equivalent.
2. Decode a binary string to its decimal equivalent.
3. Convert a binary string to its hexadecimal equivalent.

## Features

- **Hexadecimal Decoding**: Converts hexadecimal strings (e.g., `0x1A3F`) into their decimal representations.
- **Binary Decoding**: Converts binary strings (e.g., `1101`) into their decimal representations.
- **Binary-to-Hexadecimal Conversion**: Converts binary strings (e.g., `1101`) into their hexadecimal representations.

## Author and Project Information

- **Author**: Sabrina Joseph  
- **Date Created**: 02-21-2024  
- **Last Modified**: 02-21-2024  
- **Description**: Lab 5A - Numeric Conversion  

## How It Works

1. **Menu Options**:  
   The program presents a menu to the user with four options:
   - Decode hexadecimal.
   - Decode binary.
   - Convert binary to hexadecimal.
   - Quit.

2. **User Input**:  
   The user selects one of the options and provides a numeric string to decode or convert.  
   Examples:  
   - For hexadecimal decoding, input: `0x1A3F`  
   - For binary decoding, input: `1010`  
   - For binary-to-hexadecimal conversion, input: `1010`

3. **Processing**:  
   Each option uses a corresponding function to process the input and return the result:
   - **Hexadecimal decoding** uses the `hex_char_decode()` and `hex_string_decode()` functions.
   - **Binary decoding** uses the `binary_string_decode()` function.
   - **Binary-to-Hexadecimal conversion** uses the `binary_to_hex()` function.

4. **Output**:  
   The result is displayed to the user in the terminal.

## Example Output

### Menu Example:
```plaintext
Decoding Menu
-------------
1. Decode hexadecimal
2. Decode binary
3. Convert binary to hexadecimal
4. Quit
```

## User Input Example:
- Selecting option 1 (Hexadecimal Decoding):
Input: 0x1A3F
Output: Result: 6719

- Selecting option 2 (Binary Decoding):
Input: 1010
Output: Result: 10

- Selecting option 3 (Binary-to-Hexadecimal Conversion):
Input: 1010
Output: Result: A

License

This project is licensed under the MIT License. See the LICENSE file for details.
