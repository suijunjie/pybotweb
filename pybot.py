# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 05:57:35 2019

@author: evl005
"""
from pybot_random import choice_command, dice_command
from pybot_datetime import today_command, now_command, weekday_command
from pybot_weather import weather_command
from pybot_wikipedia import wikipedia_command
def length_command(command):
    cmd, text = command.split()
    length = len(text)
    response = '文字列の長さは{}文字です。'.format(length)
    return response

def heisei_command(command):
    heisei, year_str = command.split()
    if year_str.isdigit():
        year = int(year_str)
        if year >= 1989:
            heisei_year = year - 1988
            response = '西暦{}年は平成{}年です'.format(year, heisei_year)
        else:
            response = '西暦{}年は、平成ではありません。'.format(year)
    else:
        response = '数値を指定してください。'                    
    return response        

command_file = open('pybot.txt', encoding = 'utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()
bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response
    
"""
bot_dict = {
        'こんにちは': 'こんにちは',
        'ありがとう': 'どういたしまして',
        'さようなら': 'さようなら'
        }
"""
def pybot(command):
    #command = input('pybot> ')
    reponse = ''
    try:
        """
        #print(command)
        if 'こんにちは' in command:
            print('コンニチハ')
        elif 'ありがとう' in command:
            print('どういたしまして')
        elif 'さようなら' in command:
            print('サヨウナラ')
            break
        else:
            print('何を言っているか、わかりません')
        """
        for key in bot_dict:
            if key in command:
                reponse = bot_dict[key]
                break
       
        if '平成' in command:
            reponse = heisei_command(command)
            """
            heisei, year_str = command.split()
            year = int(year_str)
            if year >= 1989:
                heisei_year = year - 1988
                reponse = '西暦{}年は平成{}年です'.format(year, heisei_year)
            else:
                reponse = '西暦{}年は、平成ではありません。'.format(year)
            """ 
        if '長さ' in command:
            reponse = length_command(command)
        if '選ぶ' in command:
            reponse = choice_command(command)
        if 'さいころ' in command:
            reponse = dice_command()
        if '今日' in command:
            reponse = today_command()
        if '現在' in command:
            reponse = now_command()
        if '曜日' in command:
            reponse = weekday_command(command)
        if '天気' in command:
            reponse = weather_command() 
        if '辞典' in command:
            reponse = wikipedia_command(command) 
        if not reponse:
            reponse = '何をいっているか、わからない'
            
        return reponse
        """    
        if 'さようなら' in command:
            break;
        """
    except Exception as e:
        print('予期せぬエラーが発生しました。')
        print('*種類：', type(e))
        print('内容：', e)
        
            