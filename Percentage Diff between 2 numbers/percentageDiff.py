def percentage_diff(number_one, number_two):
    diff = abs(number_one - number_two)
    difference_in_percentage = diff / number_one
    return round(difference_in_percentage,2) * 100


first_number = int(input("Provide your first number:\n"))
second_number = int(input("\nProvide your second number:\n"))

print("\nThe percentage difference between the two numbers is: " + str(percentage_diff(first_number, second_number)) + "%")
