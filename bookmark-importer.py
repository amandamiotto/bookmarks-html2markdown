#!/usr/bin/python
#coding=utf-8

from bs4 import BeautifulSoup as BS
from os.path import exists
import xml.etree.ElementTree as ET
import lxml.html
import sys
import re


# PHASE 1
# Fault Tolerant
# Blindly parse a Chrome Bookmarks export file looking for H3 to indicate folders
# and A tags with HREF attributes for URLs to add to bookmarks.
    #inFileName = sys.argv[1]
findStr = open('infile.html', 'r', encoding="utf8").read()

with open('out.txt', 'w', encoding="utf8") as f:    
    bs = BS(findStr, 'xml')
    print(findStr)
    for child in bs.descendants:
    	if child.name == "Doctype":
    		# Ignore
    		continue
    	if child.name == "H3":
    		# Create new Header3 in Markdown: using ###
    		# Also create Table Header Row
    		print("	",file=f)
    		print("	",file=f)
    		print("### ", child.string,file=f)
    		print("	",file=f)
    		print("| RESOURCE NAME 	|	URL	|",file=f)
    		print("|----------------|-------|",file=f)
    	if child.name == "A":
    		print("| ", child.string.replace("|", ":"), "	| ", child['HREF'], " |",file=f)	
            
