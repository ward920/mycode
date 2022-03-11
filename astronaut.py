#!/usr/bin/python3

import requests
  
URL= "http://api.open-notify.org/astros.json"
def main():
    # requests.get() sends GET request to the URL
    # .json() strips JSON off the response and translates into Python!
    resp= requests.get(URL).json()
    print(resp)

main()

# people [craft name]
