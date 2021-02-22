from http.server import BaseHTTPRequestHandler
from urllib import parse
import qrcode

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        user_path = self.path
        parse_path = dict(parse.parse_qsl(parse.urlsplit(user_path).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        

        message =qr_code.__VERSION__  

        self.wfile.write(message.encode())
        return
