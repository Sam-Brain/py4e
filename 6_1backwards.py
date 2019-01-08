# Chapter 6, Exercise 1:
# Write a 'while' loop that starts at the last character in the sring and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

fruit = 'pineapple'
index = len(fruit) - 1

while index >= 0 :
    letter = fruit[index]
    print(letter)
    index = index -1