from boilerpipe.extract import Extractor
import string
# -*- coding: utf-8

def unpack_line(line):
     line = string.replace(line, " ", " ")
     els = string.split(line, " ")
     url = els[2]
     categories = els[1]
     number = els[0]
     return number, categories, url 

file_base = open('Main_base.txt', 'r')
Line=file_base.readlines()
file_extract = open('what_exctract.txt', 'w')
for line in Line:
    try:
     number1, adress1, sites1 = unpack_line(line)
     number = number1.strip("\n")
     adress = adress1.strip("\n")
     sites = sites1.strip("\n")
     extractor = Extractor(extractor = 'ArticleExtractor', url=sites)
     file_ex = open('way_to_base' + adress + '/' + number + 'forclass.txt', 'w')
     file_ex.write(extractor.getText().encode("UTF-8"))
     file_ex.close()
     file_extract.write(line)
    except:
      print line
file_base.close()
file_extract.close()


