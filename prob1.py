number = input("What number would you like for me to add? ")

sum_digits = lambda x: sum(num for num in map(int, number))

print(sum_digits(number))