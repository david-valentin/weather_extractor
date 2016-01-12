#David Valentin and Eamon Woods
#CS150-A
#Lab 8
#11/13/15

import urllib.request
import sys


webpage = urllib.request.urlopen('http://www.cs.middlebury.edu/~schar/courses/cs150-f15/hw/hw8-data/weather-05753.txt')
for line in webpage:
    web_dict = (eval(line))



def get_temperature(zip_code):
    return (web_dict['main']['temp'])

if __name__ == "__main__":
    
    # check to see if the user called the program with the right number
    # of command-line arguments
    if len(sys.argv) != 2:
        print()
        print("  usage: python3 url_basics.py <url>")
        print()

    else:
        print(get_temperature(sys.argv[1]))
