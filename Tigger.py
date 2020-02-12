# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:15:42 2020

@author: dell
"""

##Tigger character from A.A. Milne's "Winnie The Pooh" books
##Creating a class Tigger

class _Tigger:##Making the tigger class a singleton
    def ___str__(  self):
        return "I am the only one!"
    
    def roar(self):
        return "Grrr"
    
_instance = None ##Private multiscoped variable 

def Tigger():
    global  _instance
    if _instance is None:
        _instance = _Tigger()##creating an instance object
    return _instance     

   