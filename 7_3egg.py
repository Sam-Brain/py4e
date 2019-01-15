# Chapter 7, Exercise 3:
# Modify the program that prompts the use for the file name so that it prints a funny message when the user types in the exact file name "na na boo boo".
# The program should behave normally for all other files which exsist and don't exist.

fname = input('Enter the file name: ')

if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd")
    exit()

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0

for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1

print('There were', count, 'subject lines in', fname)