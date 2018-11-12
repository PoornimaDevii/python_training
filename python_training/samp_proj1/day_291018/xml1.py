from xml.sax.handler import ContentHandler
from xml.sax import make_parser

class FoodHandler(ContentHandler):

    def startElement(self, name, attrs):
        if (name == "food"):
            self.name = attrs.get("id")

    def endElement(self, name):
        if (name == "food"):
            print("%-8s" % (self.name))

food1 = FoodHandler()
saxparser = make_parser()
saxparser.setContentHandler(food1)
datasource = open("samp_xml.xml",'r')
saxparser.parse(datasource)
datasource.close()
