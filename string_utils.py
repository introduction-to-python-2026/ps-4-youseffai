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
def split_before_each_uppercases(formula):

  segments = re.split(r'([A-Z])', text)

  result = []

  start_index = 1 if segments and segments[0] == '' else 0
  
  for i in range(start_index, len(segments), 2):
 
    if i + 1 < len(segments):
      result.append(segments[i] + segments[i+1])
    else:

      result.append(segments[i])

  return result

