# Chapter 5, Exercise 2:
# Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

number = 0
total = 0
largest = None
smallest = None

while True:
    number_input = input('Enter a number: ')

    if number_input == 'done':
        break

    try:
        number = int(number_input)
    except:
        print('Invalid input')
        continue

    total = total + number

    if largest == None or number > largest:
        largest = number

    if smallest == None or number < smallest:
        smallest = number

print(total, largest, smallest)
