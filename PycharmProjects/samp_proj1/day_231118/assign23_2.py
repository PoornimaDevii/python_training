# find how many times a specific tag occurs, in an xml file
from xml.dom import minidom

doc = minidom.parse('samp_xml.xml')
print(doc)

name = doc.getElementsByTagName('food')
print("The number of tags named food:",len(name))

name = doc.getElementsByTagName('breakfast_menu')
print("The number of tags named breakfast_menu:",len(name))


name = doc.getElementsByTagName('name')
print("The number of tags named name:",len(name))