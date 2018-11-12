from xml.dom import minidom

doc = minidom.parse('samp_xml.xml')

name = doc.getElementsByTagName('name')[0]
print(name.firstChild.data)

foods = doc.getElementsByTagName("food")
for food in foods:
    fid = food.getAttribute('id')
    price = food.getElementsByTagName('price')[0]
    desc = food.getElementsByTagName('description')[0]
    cal = food.getElementsByTagName('calories')[0]
    print("fid: %s, price: %s, desc: %s, calories: %s" %(fid,price.firstChild.data, desc.firstChild.data, cal.firstChild.data))