def split_before_each_uppercases(formula):
    def split(formula):
  my_list=[]
  form_list=list(formula)
  element=""
  i=-1
  for item in form_list:
    
    print(i)
    print(my_list)
    if item.isupper():
      element=""
      element+=item
      my_list.append(element)
      i+=1
    if item.islower():
      element+=item
      my_list[i]=element
    if item.isdigit():
      element+=str(item)
      my_list[i]=element

  
  return my_list


def split_at_first_digit(formula):
    pass # Replace the `pass` with your code
