def split_at_digit(formula):
    
    first_digit_index = -1

   
    for i, char in enumerate(formula):
        if char.isdigit():
            first_digit_index = i
            break

   
    if first_digit_index != -1:
       
        prefix = formula[:first_digit_index]

      
        number_str = formula[first_digit_index:]
        number = int(number_str)

        return (prefix, number)
    else:
       
        return (formula, 1)
