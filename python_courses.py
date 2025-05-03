# while loop 
# total_iteration_number = 5
# first_iteration_number = 0

# while (first_iteration_number <= total_iteration_number):
#   first_iteration_number = first_iteration_number + 1
#   if first_iteration_number == 3:
#     continue
#   print(first_iteration_number)


# while (first_iteration_number <= total_iteration_number):
#   first_iteration_number = first_iteration_number + 1
#   if first_iteration_number == 3:
#     break
#   print(first_iteration_number)

# reddish_fruits = ["Straberry", "cherry", "blackberry", "pomegranat"]
# non_radish_fruits = ["pineapple", "appricot", "nectarin", "papaya"]

# for fruit in range(0,6):
#   print(fruit)

# for letter in fruits[0]:
#   if letter == "p":
#     continue
#   print(letter)


# reddish_fruits = ["Straberry", "cherry", "blackberry", "pomegranat"]
# non_radish_fruits = ["pineapple", "appricot", "nectarin", "papaya"]


# for red_fruit in reddish_fruits:
#   for non_reddish_fruit in non_radish_fruits:
#     print(red_fruit, non_reddish_fruit)

# function 


#  call function based unknown arguments
# def calculate_sum_number (*number):
#   total_number = number[0] + number[1]
#   return total_number

# result_sum_numbers = calculate_sum_number(16,16)
# print(result_sum_numbers)

# def calculate_sum_number (number1, number2):
#   total_number = number1 + number2
#   return total_number

# result_sum_numbers = calculate_sum_number(number2 = 8, number1= 12)
# print(result_sum_numbers)


# call function based unknown number of key-value pair argument
def calculate_sum_number (number1, number2 = 16):
  total_number = number1 + number2
  return total_number

result_sum_numbers = calculate_sum_number(8,8)
print(result_sum_numbers)