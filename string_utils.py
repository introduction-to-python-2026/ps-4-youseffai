def split_at_digit(formula):
    """
    Splits a string into a prefix (before the first digit) and
    an integer number (from the first digit onward).

    Args:
        formula (str): The input string (e.g., a chemical formula).

    Returns:
        tuple: A tuple containing (prefix_string, number_integer).
    """
    first_digit_index = -1

    # 1. Find the index of the first digit
    for i, char in enumerate(formula):
        if char.isdigit():
            first_digit_index = i
            break

    # 2. Check if a digit was found and split accordingly
    if first_digit_index != -1:
        # Digit found:
        # a. Prefix is the part before the first digit
        prefix = formula[:first_digit_index]

        # b. Number is the rest of the string converted to an integer
        number_str = formula[first_digit_index:]
        number = int(number_str)

        return (prefix, number)
    else:
        # No digit found: Return the original string and 1
        return (formula, 1)

# Examples to verify the function:
print(f'split_at_digit("H22") -> {split_at_digit("H22")}')
print(f'split_at_digit("NaCl1") -> {split_at_digit("NaCl1")}')
print(f'split_at_digit("O") -> {split_at_digit("O")}')
print(f'split_at_digit("CaCl2") -> {split_at_digit("CaCl2")}')


def split_before_each_uppercase_manual(formula):
    
    if not formula:
        return []

    result = []
    current_segment = ""

    for char in formula:
        if char.isupper():
            
            if current_segment:
                
                result.append(current_segment)
            
            current_segment = char
        else:
            
            current_segment += char

    if current_segment:
        result.append(current_segment)

    return result
