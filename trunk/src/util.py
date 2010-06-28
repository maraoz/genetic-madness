#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Jun 3, 2010

@author: maraoz
'''

from random import choice
import string

def random_string(length=16):
    characters = string.letters + string.digits
    return choice(string.letters) + ''.join([choice(characters) \
                     for _ in xrange(length - 1)])
