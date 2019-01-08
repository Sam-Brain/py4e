# Chapter 6, Exercise 5:
# Take the following Python code that stres a string:
str = 'X-DSPAM-Confidence:0.8475'
# Use 'find' and slicing to extract the portion of the string after the colon character and then use the 'float' function to convert the extracted string into a floating point number.

pos = str.find(':')
print(pos)

strconfi = str[pos+1:]
print(strconfi)

confi = float(strconfi)
print(confi + 1)