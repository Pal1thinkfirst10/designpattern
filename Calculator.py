# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:26:03 2020

@author: dell
"""

##An average calculator:average of a series of numbers provided by some sort of sequential data source
from abc import ABC,abstractmethod

class AverageCalculator(ABC):
    def average(self):
        try:
            num_items  = 0
            total_sum = 0
            while self.has_next():
                total_sum += sum.next_item()
                num_items += 1
            if num_items == 0:
                raise RuntimeError("Can't compute the average of zero items.")
                
            return total_sum/num_items
        finally:
            self.dispose()
    @abstractmethod ##any class that inherits from abstract class needs to implement these methods
    def has_next(self):
        pass
    
    @abstractmethod
    def next_item(self):
        pass
    
    def dispose(self):
        pass
    
class FileAverageCalculator(AverageCalculator):
    
    def __init__(self,file):
        self.file = file
        self.last_line = self.file.readline()
        
    def has_next(self):
        return self.last_line != ""
    
    def next_item(self):
        result = float(self.last_line)
        self.last_line =self.file.readline()
        return result
    
    def dispose(self):
        self.file.close()
        
fac = FileAverageCalculator(open('data.txt'))  
print(fac.average()) # Call the template method


      
    
    
    
    
        
        
    
    
            