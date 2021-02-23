from http.server import BaseHTTPRequestHandler
from urllib import parse
import qrcode
import PIL
from cowpy import cow
import io

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        user_path = self.path
        parse_path = dict(parse.parse_qsl(parse.urlsplit(user_path).query))
        self.send_response(200)
        self.send_header('Content-type','image/png')
        self.end_headers()

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('Some data')
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        #converting image to byte array
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format="PNG")
        img_byte_array = img_byte_array.getvalue()

        self.wfile.write(img_byte_array)
        return
