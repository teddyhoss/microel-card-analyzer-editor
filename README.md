# MicroEL Card Analyzer and Editor
This Python script analyzes and modifies parameters found in Sector 1, Rows 1, 2, and 3 of MicroEL cards. It provides a user-friendly interface for parsing, displaying, and editing the hexadecimal data stored in these specific card locations.
## Purpose
The MicroEL Card Analyzer and Editor serves to:

1. Parse and display the contents of Sector 1, Rows 1, 2, and 3 of MicroEL cards.
2. Allow users to modify specific parameters within these rows.
3. Provide a clear visualization of the data, including original hex values, inverted hex values, and decimal representations.
4. Facilitate easy editing of card parameters in various formats (HEX, HEX INVERTED, DECIMAL).

## Features and Parameter Details
The script processes a 32-character hexadecimal string, divided into the following parameters:

1. Operation number: 4 characters (2 bytes)
2. Total input sum: 4 characters (2 bytes)
3. Deposit: 2 characters (1 byte)
4. Credit: 4 characters (2 bytes)
5. Transaction date: 8 characters (4 bytes)
6. Points: 4 characters (2 bytes)
7. Last transaction amount: 4 characters (2 bytes)
8. Checksum: 2 characters (1 byte)

Each character in the hexadecimal string represents 4 bits, so 2 characters make 1 byte (8 bits).
Key features include:

- Colorized display of the full hexadecimal string
- Detailed breakdown of each parameter
- Interactive parameter modification
- Support for inputting new values in HEX, HEX INVERTED, or DECIMAL format
- Automatic recalculation and display of modified data

## Usage

1. Run the script: python microel_card_analyzer.py
2. Enter the 32-character hexadecimal string when prompted
3. View the parsed and colorized data
4. Choose to modify a parameter if desired
5. Select the parameter to modify
6. Choose the format for entering the new value (HEX, HEX INVERTED, or DECIMAL)
7. Enter the new value
8. View the updated data
9. Repeat steps 4-8 as needed, or exit the program

## Important Note
The third row of Sector 1 indicates the row with the previous credit. This information is crucial for understanding the card's transaction history and current balance.
## Requirements

`Python 3.6 or higher`
