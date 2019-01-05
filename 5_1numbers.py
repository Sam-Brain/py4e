# Chapter 5, Exercise 1:
# Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using 'try' and 'except' and print an error message and skip to the next number.

number = 0
total = 0
count = 0
average = 0

while True:
    number_input = input('Enter a number: ')

    if number_input == 'done':
        break

    try:
        number = int(number_input)
        total = total + number
        count = count + 1
    except:
        print('Invalid input')
        continue

average = total / count
print(total, count, average)