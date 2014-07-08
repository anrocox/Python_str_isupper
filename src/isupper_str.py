#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 8, 2014

@author: anroco

In a python str how to know if characters are uppercase?

En un str python ¿como saber si todos los caracteres son mayusculas?
'''

#create a str
s = 'TEXTUAL DATA IN PYTHON'
print(s)

#the isupper() method verify if all characters in the string are uppercase.
#return True or False
print(s.isupper())

#create a str
s = 'Textual data in Python'
print(s)

#return False because not all characters are uppercase.
print(s.isupper())
