1. Crawl_Scrapy
Consists of two spiders that create the database with sites and categories of sites.
The first spider collects the lower branches.
The second spider collects on lower branches all base.
Data_Base1.txt is the example file.

How to use?
Run first then the second spider.
scrapy crawl "name_of_spider"

Requirements

Python 2.7 or up
Works on Linux
Scrapy http://scrapy.org/

2.Loading_Sites
Download sites.
'way_to_base' is the way where to download.

You need urllib2 http://docs.python.org/2/library/urllib2.html

You will get an '1html.txt ... 455html.txt'

3. Extract_text
Consist of two programm.
The first uses html2text http://code.activestate.com/pypm/html2text/
'way_to_base' is the way where you have your data base.
 
The second uses boilerpipe http://code.google.com/p/boilerpipe/
For boilerpipe you need jpipe http://jpype.sourceforge.net/.
Boilerpipe work without something data base. He load sites and save text.

4. Naive Bayes classifier
Overview
A naive Bayes classifier is a simple probabilistic classifier based on applying Bayes theorem with strong (naive) independence assumptions. A more descriptive term for the underlying probability model would be "independent feature model". Read more on http://en.wikipedia.org/wiki/Naive_Bayes_classifier.

Requirements
Python 2.7 or up
Works on Linux
Stemmer ntlk 
http://nltk.org/
http://snowball.tartarus.org/algorithms/russian/stemmer.html

How to use?
For train:
You need to have a database that will contain the files with the text for teaching. For example:
Database/Computers/1forclass.txt ... 2forclass.txt ...
Database/Space/1forclass.txt ...
Insert way to databse in the functions train("file_list", "way_to_the_dbase")
"file_list" is the text file 
For example: "MainBase.txt"
In "MainBase.txt"
1 Computers http://www.i.ua/
2 Computers http://plus.google.com/
3 Computers http://www.yahoo.com/
4 Computers http://www.intel.ru/
5 Computers http://megagroup.ru/
...
...
...

text_for_classif="something text" is your text for classification.

When the classification will be over you will see value c (see about Bayes theorem) and name of 
category when c is smallest.
