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
  """
  Splits a string into a list of substrings, where each new substring 
  starts with a capital letter, without using the 're' module.

  Args:
    text (str): The input string to be split.

  Returns:
    list: A list of substrings.
  """
  if not text:
    return []

  segments = []
  current_segment = ""

  for char in text:
    # Check if the character is a capital letter
    if char.isupper():
      # If the current_segment is NOT empty, 
      # it means we've just completed a segment. 
      if current_segment:
        segments.append(current_segment)
      
      # Start a new segment with the current capital letter
      current_segment = char
    else:
      # If it's not a capital letter, just append it to the current segment
      current_segment += char
  
  # After the loop finishes, append the very last segment
  if current_segment:
    segments.append(current_segment)
    
  return segments
