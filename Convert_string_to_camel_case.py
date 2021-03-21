"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""


def to_camel_case(text):
    
    if text == '':
        return ''
    
    list_text = list(text)
    for i in range(len(list_text)):
        if list_text[i] in ('-', '_'):
            list_text[i+1] = list_text[i+1].upper() 
            list_text[i] = ''

    return ''.join(list_text)
