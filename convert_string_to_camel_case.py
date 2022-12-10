"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"""
import re

def to_camel_case(text):
    return "".join([word.capitalize() if text.index(word) != 0 else word for word in re.split('_|-', text) ])

if __name__ == '__main__':
        print(to_camel_case(""))                        #""
        print(to_camel_case("the_stealth_warrior"))     #theStealthWarrior
        print(to_camel_case("The-Stealth-Warrior"))     #TheStealthWarrior
        print(to_camel_case("A-B-C"))                   #ABC