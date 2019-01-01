# Chapter 3, Exercise 1:
# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

input_hours = input('Enter Hours: ')
hours = float(input_hours)

input_rate = input('Enter Rate: ')
rate = float(input_rate)

if hours <= 40:
    pay = hours * rate
else:
    pay = 40 * rate + (hours - 40) * rate * 1.5

print('Pay:', pay)