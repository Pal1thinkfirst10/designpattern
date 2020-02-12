# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:12:52 2020

@author: dell
"""

from Tigger import Tigger

a = Tigger()
b = Tigger()

print(f"ID(a) = {id(a)}")
print(f"ID(a) = {id(b)}")
print(f"Are they the same object? {a is b}")




