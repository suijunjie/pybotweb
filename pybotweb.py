# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:19:09 2019

@author: evl005
"""

from bottle import route, run, template, request
#from datetime import datetime
from pybot import pybot

@route('/hello')

def hello():
    #now = datetime.now()
    
    #return template('hello world!{{now}}', now = now)
    #return template('pybot_template', now = now)
    return template('pybot_template', input_text = '', output_text = '')

#run(host = 'localhost', port = 8080, debug= True)

@route('/hello', method = 'POST')
def do_hello():
    input_text = request.forms.input_text
    output_text = pybot(input_text)
    return template('pybot_template', input_text = input_text, output_text = output_text)

run(host = 'localhost', port = 8080, debug = True)
