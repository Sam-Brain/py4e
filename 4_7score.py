# Chapter 4, Exercise 7:
# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

# Score    Grade
# >= 0.9   A
# >= 0.8   B
# >= 0.7   C
# >= 0.6   D
#  < 0.6   F

input_score = input('Enter score: ')

def computegrade(score):
    if score >= 0.9: return('A')
    elif score >= 0.8: return('B')
    elif score >= 0.7: return('C')
    elif score >= 0.6: return('D')
    else: return('F')

try:
    score = float(input_score)

    if score >= 0.0 and score <= 1.0:
        print(computegrade(score))
    else:
        print('Bad score')

except:
    print('Bad score')
