# Chapter 3, Exercise 2:
# Rewrite your pay program using 'try' and 'except' so that your program handles non-numeric input gracefully by printing a message and exiting the program.

input_hours = input('Enter Hours: ')

try:
    hours = float(input_hours)
    input_rate = input('Enter Rate: ')
    rate = float(input_rate)
except:
	print('Error, please enter a numeric input.')
	quit()

if hours <= 40:
    pay = hours * rate
else:
    pay = 40 * rate + (hours - 40) * rate * 1.5

print('Pay:', pay)