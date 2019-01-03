# Chapter 4, Exercise 6:
# Rewrite your pay computation with time-and-a-half overtime and create a funcion called computepay which takes two parameters (hours and rate)

input_hours = input('Enter Hours: ')

try:
    hours = float(input_hours)
    input_rate = input('Enter Rate: ')
    rate = float(input_rate)
except:
    print('Error, please enter a numeric input.')
    quit()

def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    return pay

print('Pay:', computepay(hours, rate))