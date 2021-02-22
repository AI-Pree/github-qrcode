from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

    #generate a qr code based on the value provided in url path
    def qr_code_generator(self, data, fill="black", back="white"):
        import qrcode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        image = qr.make_image(fill_color=fill, back_color=back)
        return image

    def do_GET(self):
        user_path = self.path
        parse_path = dict(parse.parse_qsl(parse.urlsplit(user_path).query))
        self.send_response(200)
        self.send_header('Content-type','image/png')
        self.end_headers()
    
        # if "data" in parse_path:
        #     message = data
        # else:
        #     message = "Hello, stranger!"        
        image = qr_code_generator(parse_path["data"], parse_path["fill"], parse_path["background"])

        self.wfile.write(image)
        return
