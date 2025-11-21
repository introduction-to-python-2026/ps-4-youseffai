def split_at_first_digit(formula):
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
def split_before_each_uppercases(text):

  if not text:
    return []

  segments = []
  current_segment = ""

  for char in text:

    if char.isupper():

      if current_segment:
        segments.append(current_segment)

      current_segment = char
    else:
      current_segment += char
  
  if current_segment:
    segments.append(current_segment)
    
  return segments
