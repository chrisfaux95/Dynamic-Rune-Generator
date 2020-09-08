# Compact string of 0-9, a-z, A-Z
from string import ascii_letters, digits
ALPHA = digits + ascii_letters

""" function to print ASCII values of string """
def print_vals(s):
    val_tuple = lambda c: (c, ord(c))
    val_list = [val_tuple(c) for c in s]
    print(val_list)
    return val_list

""" function to return a list of values based upon
the position of each character in a string's position in ALPHA """
def alpha_to_num(s):
    return [ALPHA.index(c) for c in s]

print_vals(ALPHA)