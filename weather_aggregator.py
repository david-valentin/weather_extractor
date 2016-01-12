# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 23:03:24 2015

@author: dvalentin
"""

from weather_reader import get_temperature
import datetime
import random


x = "10016"

weather_url = "http://api.openweathermap.org/data/2.5/weather?zip=05753,us&appid=2de143494c0b295cca9337e1e96b00e0&units=imperial"

def passit(zip_code):


    weather_url = "http://api.openweathermap.org/data/2.5/weather?zip= %s ,us&appid=2de143494c0b295cca9337e1e96b00e0&units=imperial" % (str(zip_code))
    print(weather_url)



def get_hour():
    now = datetime.datetime.now()
    return str(now.hour)
    
def get_minute():

    now = datetime.datetime.now()
    return str(now.minute)

def get_date():
    now = datetime.datetime.now()
    return str(now.month) + "-" + str(now.day) + "-" + str(now.year)

def storage(file_name, zip_code):
    
    storage_file = open(file_name, "w")
    
    storage_file.write("Date: " + "\t  " + "   Hour: " + "\t" + "Temperature: " + "\n")    
    storage_file.write(str(get_date()) + "\t" + str(get_hour()) + "\t" + str(get_temperature(zip_code)) + "\n")

    storage_file.close()            

def make_list(filename):
    file = open(filename, 'r')
    file_list = []
    for line in file:
        file_list.append((line.split()[0], line.split()[1]))
    return file_list

def is_entry(filename, date, time):
    file_list = make_list(filename)
    return (date,time) in file_list

def is_current_date_hour_entry(filename):
    return is_entry(filename, get_date(), get_hour())
    


if __name__ == "__main__":
    # check to see if the user called the program with the right number
    # of command-line arguments
    if len(sys.argv) != 3:
        print()
        print("  usage: python3 weather_aggregator.py <file> <zip_code>")
        print()
    
    else:
    
        print('Hello')


storage("weather_storage_data.txt", 10016)


