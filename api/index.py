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


        #generting qr code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        image = qr.make_image(fill_color=fill, back_color=back)

        message ="it does work"    

        self.wfile.write(message.encode())
        return
