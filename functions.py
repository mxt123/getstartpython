#!/usr/bin/env python2

def modify_string(original):
    original += " that has been modified"
    # only local copy modified    

def modify_string_return(original):
    original += " that has been modified"
    return original
    # return modified

test_string="This is a test string"
modify_string(test_string)
print(test_string)
print(modify_string("hello"))

test_string=modify_string_return(test_string)
print(test_string)
print(modify_string_return(test_string))
