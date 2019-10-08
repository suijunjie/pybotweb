# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:24:09 2019

@author: evl005
"""

from bottle import template
response = template('こんにちは{{name}}さん', name = 'たかのり')
print(response)
response = template('こんにちは{{name}}さん', name = 'みつき')
print(response)
