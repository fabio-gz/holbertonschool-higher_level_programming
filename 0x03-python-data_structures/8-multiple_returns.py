#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        sen = (len(sentence), sentence[0])
        return sen
    else:
        sen = (0, None)
        return sen
