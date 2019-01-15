# Chapter 7, Exercise 1:
# Write a program to read through a file and print the contents of the file (line by line) all in upper case.

fname = input('Enter a file name: ')

try:
    fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0

for line in fhandle:
    strip = line.rstrip()
    print(strip.upper())