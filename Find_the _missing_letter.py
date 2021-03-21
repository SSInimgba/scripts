"""
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
"""

# Solution 1
def find_missing_letter(chars):
    ords = [ord(char) for char in chars]
    first_el, last_el = ords[0], ords[-1]
    return next(chr(i) for i in range(first_el, last_el) if i not in ords)
  
  
# Solution 2
def find_missing_letter(chars):
    ords = [ord(char) for char in chars]
    x = ((ords[-1]) * (ords[-1]+1))//2
    y =  ((ords[0] - 1) * ords[0])//2
    z =  x - y
    sum_ords = sum(ords)
    missing_char = chr(z - sum_ords)
    return(missing_char)
   
 
