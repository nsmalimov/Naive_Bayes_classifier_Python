<p>1. Crawl_Scrapy</p>
<p>Consists of two spiders that create the database with sites and categories of sites.</p>
<p>The first spider collects the lower branches.</p>
<p>The second spider collects on lower branches all base.</p>
<p>Data_Base1.txt is the example file.</p>

<p>How to use?</p>
<p>Run first then the second spider.</p>
<p>scrapy crawl "name_of_spider"</p>

<p>Requirements</p>

<p>Python 2.7 or up</p>
<p>Works on Linux</p>
<p>Scrapy http://scrapy.org/</p>

<p>2.Loading_Sites</p>
<p>Download sites.</p>
<p>'way_to_base' is the way where to download.</p>

<p>You need urllib2 http://docs.python.org/2/library/urllib2.html</p>

<p>You will get an '1html.txt ... 455html.txt'</p>

<p>3. Extract_text</p>
<p>Consist of two programm.</p>
<p>The first uses html2text http://code.activestate.com/pypm/html2text/</p>
<p>'way_to_base' is the way where you have your data base.</p>
 
<p>The second uses boilerpipe http://code.google.com/p/boilerpipe/</p>
<p>For boilerpipe you need jpipe http://jpype.sourceforge.net/.</p>
<p>Boilerpipe work without something data base. He load sites and save text.</p>

<p>4. Naive Bayes classifier</p>
<p>Overview</p>
<p>A naive Bayes classifier is a simple probabilistic classifier based on applying Bayes theorem with strong (naive) independence assumptions. A more descriptive term for the underlying probability model would be "independent feature model". Read more on http://en.wikipedia.org/wiki/Naive_Bayes_classifier.</p>

<p>Requirements</p>
<p>Python 2.7 or up</p>
<p>Works on Linux</p>
<p>Stemmer ntlk</p>
<p>http://nltk.org/</p>
<p>http://snowball.tartarus.org/algorithms/russian/stemmer.html</p>

<p>How to use?</p>
<p>For train:</p>
<p>You need to have a database that will contain the files with the text for teaching. For example:</p>
<p>Database/Computers/1forclass.txt ... 2forclass.txt ...</p>
<p>Database/Space/1forclass.txt ...</p>
<p>Insert way to databse in the functions train("file_list", "way_to_the_dbase")</p>
<p>"file_list" is the text file</p>
<p>For example: "MainBase.txt"</p>
<p>In "MainBase.txt"</p>
<p>1 Computers http://www.i.ua/</p>
<p>2 Computers http://plus.google.com/</p>
<p>3 Computers http://www.yahoo.com/</p>
<p>4 Computers http://www.intel.ru/</p>
<p>5 Computers http://megagroup.ru/</p>
<p>...</p>
<p>...</p>
<p>...</p>

<p>text_for_classif="something text" is your text for classification.</p>

<p>When the classification will be over you will see value c (see about Bayes theorem) and name of 
category when c is smallest.</p>
