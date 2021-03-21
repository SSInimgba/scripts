"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"
"""

# Solution 1
def DNA_strand(dna):
    # code here
    pairs = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    
    return ''.join([pairs[e] for e in dna])
  
  
# Solution 2 // Brute Force

def DNA_strand(dna):
    # code here
    s = ''
    for e in dna:
        if e == 'A':
            s += 'T'
        elif e == 'T':
            s += 'A'
        elif e == 'G':
            s += 'C'
        elif e == 'C':
            s += 'G'
            
    return s 
