def percentage_diff(number_one, number_two):
    diff = abs(number_one - number_two)
    difference_in_percentage = (diff / number_one) * 100
    return round(difference_in_percentage,2)


first_number = float(input("Provide your first number:\n"))
second_number = float(input("\nProvide your second number:\n"))

if first_number < second_number:
    print("\nThe percentage difference between the two numbers is: " + str(percentage_diff(first_number, second_number)) + "%")
else:
    print("\nThe percentage difference between the two numbers is: -" + str(percentage_diff(first_number, second_number)) + "%")
