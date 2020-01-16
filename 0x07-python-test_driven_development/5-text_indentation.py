#!/usr/bin/python3
"""

prints a text with terminations

"""


def text_indentation(text):
    """ function to prints a text a new line every '.', '?' and ':'
    Args:
        text: string to print
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for i in range(len(text)):
        if i > 0 and text[i - 1] == '.' or text[i - 1] == '?'\
                      or text[i - 1] == ':' and text[i] == ' ':
            continue
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print('{}'.format(text[i]), end='')
            print('\n')
        else:
            print('{}'.format(text[i]), end='')
