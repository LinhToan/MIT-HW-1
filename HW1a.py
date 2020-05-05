# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:49:54 2020

@author: Hiro
"""

r = 0.04

annual_salary = input('Enter your annual salary: ')
portion_saved = input('Enter the percent of your salary to save (decimal): ')
total_cost = input('Enter the cost of your dream home: ')

annual_salary = float(annual_salary)
portion_saved = float(portion_saved)
total_cost = float(total_cost)

time = 1.0

current_savings = (annual_salary / 12.0) * portion_saved
portion_down_savings = total_cost * 0.25

while current_savings < portion_down_savings:
    time += 1
    current_savings += (annual_salary * portion_saved / 12.0) + (current_savings*r/12.0)
    
time = int(time)
time = str(time)
print('Number of months: ' + time)