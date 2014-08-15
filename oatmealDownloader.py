#------
# Borrowed from https://github.com/manojmj92/theoatmeal.com-downloader/blob/master/theoatmeal.py
#-----


from bs4 import BeautifulSoup
import urllib
import os
import sys
import logging


dir = os.path.dirname(os.path.abspath(__file__))
oatmealdir = dir + "//OatmealComics"
print oatmealdir

if not os.path.exists(oatmealdir):
        os.makedirs(oatmealdir)
