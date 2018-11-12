# automating connection using http

import httplib2


c = httplib2.HTTPSConnectionWithTimeout('docs.python.org',443)

c.putrequest("GET","/3/tutorial/index.html")
c.putheader('Someheader','Somevalue')
c.endheaders()

r = c.getresponse()
data = r.read()
print(data)
c.close()