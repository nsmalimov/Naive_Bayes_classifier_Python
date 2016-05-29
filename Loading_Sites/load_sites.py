# -*- coding: utf-8
import os
import string
import urllib2


def unpack_line(line):
    line = string.replace(line, "'", "")
    els = string.split(line, " ")
    categories = els[0]
    sitename = els[1]
    return sitename, categories


file_categories = open("list_categories.txt", "r")
Lines = file_categories.readlines()

for line in Lines:
    line = line.strip("\n")
    os.makedirs(line)

file_sites = open("list_sites.txt", "r")
file_load = open("what_load.txt", "w")
Lines = file_sites.readlines()
categories1 = ""
number1 = 0

for line in Lines:
    try:
        sitename1, categories1 = unpack_line(line)
        sitename = sitename1.strip("\n")
        categories = categories1.strip("\n")
        u = urllib2.urlopen(sitename, timeout=35)
        if categories != categories1:
            categories1 = categories
            number1 = 1
        else:
            number1 = number1 + 1
            categories1 = categories
        file_for_save = open('way_to_dbase' + categories + '/'
                             + str(number1) + 'html.txt', "w")
        file_for_save.write(u.read())
        file_for_save.close()
        file_load.write(str(number1) + ' ' + line)
    except:
        print(line)

file_categories.close()
file_sites.close()
file_load.close()
