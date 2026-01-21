#!/usr/bin/python3
# 10-divisible_by_2.py

def divisble_by_2(my_list=[]):
        """finds all multiples of 2 in a list"""
        
        multiples = []
        
        for i in range(len(my_list)):
            
            if my_list[i] % 2 == 0:
                
                multiples.append(true)
        
            else:
            
                multiples.append(false)

        
        return (multiples)
