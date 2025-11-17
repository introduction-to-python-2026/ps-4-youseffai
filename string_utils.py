def split_formula_into_components(formula):
  components = []
  current_element = ""
  current_number = ""

  for char in formula:
    if char.isalpha():

      if current_number:
        components.append(current_number)
        current_number = ""

      if char.isupper():
  
        if current_element:
          components.append(current_element)
        current_element = char 
      else: 
        current_element += char
    elif char.isdigit():

      if current_element:
        components.append(current_element)
        current_element = ""
      current_number += char 


  if current_element:
    components.append(current_element)
  if current_number:
    components.append(current_number)

  return components
def split_at_first_digit(formula):
    pass # Replace the `pass` with your code
