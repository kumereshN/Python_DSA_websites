def str_to_int(input_str):
  if input_str[0] == '-':
    is_negative = True
    input_str = input_str[1:]
  else:
    is_negative = False

  output_lst = [ord(input_str[i]) - ord('0') for i in range(len(input_str))]

  output_no = (10 ** (len(output_lst)-1)) * output_lst[0]
  j = 1

  for i in reversed(range(1, len(output_lst))):
    output_no += output_lst[i] * j
    j *= 10

  if is_negative:
    return output_no * -1
  else:
    return output_no
