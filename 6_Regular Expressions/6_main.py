import re

'''
Identifiers:
\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter
\W = anything but a letter
. = any character, except for a new line
\b = space around whole words
\. = period. must use backslash, because . normally means any character.

Modifiers:
{1,3} = for digits, u expect 1-3 counts of digits, or "places"
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions
$ = matches at the end of string
^ = matches start of a string (a moje she - not)
| = matches either/or. Example x|y = will match either x or y
[] = range, or "variance" [A-Z]
{x} = expect to see this amount of the preceding code.
{x,y} = expect to see this x-y amounts of the precedng code

White Space Charts:
\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = carriage return

Characters to REMEMBER TO ESCAPE IF USED!
. + * ? [ ] $ ^ ( ) { } | \

Brackets:
[] = quant[ia]tative = will find either quantitative, or quantatative.
[a-z] = return any lowercase letter a-z
[1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z

EXAMPLES:
quantitative
quantatative
quant[ia]tative

[a-zA-Z] [1-9]

'''

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d+', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

print(ages)
print(names)


'''
EXAMPLE

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"


matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
'''






