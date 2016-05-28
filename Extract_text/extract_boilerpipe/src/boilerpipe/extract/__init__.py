import socket
import threading
import urllib2

import chardet
import jpype

socket.setdefaulttimeout(15)
lock = threading.Lock()

InputSource = jpype.JClass('org.xml.sax.InputSource')
StringReader = jpype.JClass('java.io.StringReader')
HTMLHighlighter = jpype.JClass('de.l3s.boilerpipe.sax.HTMLHighlighter')
BoilerpipeSAXInput = jpype.JClass('de.l3s.boilerpipe.sax.BoilerpipeSAXInput')


class Extractor(object):
    extractor = None
    source = None
    data = None

    def __init__(self, extractor='DefaultExtractor', **kwargs):
        if kwargs.get('url'):
            request = urllib2.urlopen(kwargs['url'])
            self.data = request.read()
            encoding = request.headers['content-type'].lower().split('charset=')[-1]
            if encoding.lower() == 'text/html':
                encoding = chardet.detect(self.data)['encoding']
            self.data = unicode(self.data, encoding)
        elif kwargs.get('html'):
            self.data = kwargs['html']
            if not isinstance(self.data, unicode):
                self.data = unicode(self.data, chardet.detect(self.data)['encoding'])
        else:
            raise Exception('No text or url provided')

        try:
            if threading.activeCount() > 1:
                if jpype.isThreadAttachedToJVM() == False:
                    jpype.attachThreadToJVM()
            lock.acquire()

            self.extractor = jpype.JClass(
                "de.l3s.boilerpipe.extractors." + extractor).INSTANCE
        finally:
            lock.release()

        reader = StringReader(self.data)
        self.source = BoilerpipeSAXInput(InputSource(reader)).getTextDocument()
        self.extractor.process(self.source)

    def getText(self):
        return self.source.getContent()
