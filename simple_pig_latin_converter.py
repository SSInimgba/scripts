"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

import re 


def pig_it(text):
    text = text.split()
    new_word_list = []
    
    
    for i in text:
        f_c = i[0] if i[0] not in ('?', '!') else ''
        r_o_w = i[1:]
        exclamation = re.search("\!|\?", i)[0] if re.search("\!|\?", i) else ''
        new_word = (r_o_w + f_c + 'ay') if f_c else ''
        new_word_list.append(new_word)
    return ' '.join(new_word_list)+exclamation
        
