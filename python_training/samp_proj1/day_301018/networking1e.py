# import urllib
#
# print(dir(urllib))
# urllib.request()

# Creating own HTTP server

from BasicHttpServer import HTTPServer, CGIHTTPRequestHandler

class HelloHandler(CGIHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200,"OK")
            self.send_header('Content-type','text/plain')
            self.end_headers()
            self.wfile.write(b'''<HTML>
            <HEAD><TITLE>Hello</TITLE></HEAD>
            <BODY>Hello World:</BODY></HTML>''')

serv = HTTPServer(('',8080),HelloHandler)
serv.serve_forever()

