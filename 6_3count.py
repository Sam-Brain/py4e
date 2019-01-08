# Chapter 6, Exercise 3:
# Encapsulate this code in a function named 'count', and generalize it so that it accepts the string and the letter as arguments.

def count(word, letter) :
    counter = 0
    for char in word :
        if char == letter :
            counter = counter + 1
    return(counter)

x = count('banana', 'a')
print(x)