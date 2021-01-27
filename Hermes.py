import urllib.request, urllib.error, urllib.parse
import requests
from pywebcopy import save_website
import os



def create_Folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def cho_website(query, j):
    try:
        from googlesearch import search
    except ImportError:
        print("No module name ' google' found")

    query = input('what do you want to search?')

    for j in search(query, tld="co.in", num=20, stop= 10, pause=2):
        print(j)

#Choose the file from the download html, save as local file
