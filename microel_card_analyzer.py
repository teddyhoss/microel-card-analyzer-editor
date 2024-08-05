import sys

def color_string(input_string):
    colors = ["\033[96m", "\033[36m", "\033[35m", "\033[34m", "\033[33m"]
    reset = "\033[0m"
    
    schema = [
        (4, "Operation number"),
        (4, "Total input sum"),
        (2, "Deposit"),
        (4, "Credit"),
        (8, "Transaction date"),
        (4, "Points"),
        (4, "Last transaction amount"),
        (2, "Checksum")
    ]
    
    result = []
    color_index = 0
    char_index = 0
    
    for length, description in schema:
        segment = input_string[char_index:char_index+length]
        colored_segment = colors[color_index] + segment + reset
        inverted_segment = ''.join(reversed([segment[i:i+2] for i in range(0, len(segment), 2)]))
        decimal_value = int(inverted_segment, 16)
        result.append((description, segment, colored_segment, inverted_segment, decimal_value))
        char_index += length
        color_index = (color_index + 1) % len(colors)
    
    return result

def print_data(parsed_data):
    print("\nFull colored string:")
    print(''.join(colored for _, _, colored, _, _ in parsed_data))
    
    print("\nParsed data:")
    for description, original, colored, inverted, decimal in parsed_data:
        print(f"{description}: {colored} (Inverted: {inverted}, Decimal: {decimal})")

def modify_parameter(parsed_data):
    print("\nChoose a parameter to modify:")
    for i, (description, _, _, _, _) in enumerate(parsed_data):
        print(f"{i + 1}. {description}")
    
    choice = int(input("Enter the number of the parameter to modify: ")) - 1
    
    if choice < 0 or choice >= len(parsed_data):
        print("Invalid choice.")
        return parsed_data

    print("\nChoose the format of the new value:")
    print("1. HEX")
    print("2. HEX INVERTED")
    print("3. DECIMAL")
    format_choice = input("Enter the number of your choice: ")

    if format_choice not in ['1', '2', '3']:
        print("Invalid format choice.")
        return parsed_data

    new_value = input("Enter the new value: ")

    description, original, colored, inverted, decimal = parsed_data[choice]
    length = len(original)

    if format_choice == '1':  # HEX
        new_hex = new_value.zfill(length)
        new_inverted = ''.join(reversed([new_hex[i:i+2] for i in range(0, len(new_hex), 2)]))
        new_decimal = int(new_inverted, 16)
    elif format_choice == '2':  # HEX INVERTED
        new_inverted = new_value.zfill(length)
        new_hex = ''.join(reversed([new_inverted[i:i+2] for i in range(0, len(new_inverted), 2)]))
        new_decimal = int(new_inverted, 16)
    else:  # DECIMAL
        new_decimal = int(new_value)
        new_inverted = f"{new_decimal:0{length}X}"
        new_hex = ''.join(reversed([new_inverted[i:i+2] for i in range(0, len(new_inverted), 2)]))

    new_colored = parsed_data[choice][2].replace(original, new_hex)
    parsed_data[choice] = (description, new_hex, new_colored, new_inverted, new_decimal)

    # Reconstruct the full string
    full_string = ''.join(segment for _, segment, _, _, _ in parsed_data)
    return color_string(full_string)

def main():
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
    else:
        input_string = input("Please enter the string to parse: ")
    
    if len(input_string) != 32:
        print("Error: The input string must be exactly 32 characters long.")
        return
    
    parsed_data = color_string(input_string)
    
    while True:
        print_data(parsed_data)
        
        choice = input("\nDo you want to modify a parameter? (y/n): ").lower()
        if choice != 'y':
            break
        
        parsed_data = modify_parameter(parsed_data)

if __name__ == "__main__":
    main()