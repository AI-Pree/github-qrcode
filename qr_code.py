def generate_qr_code():
    import pillow
    import qrcode

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr.add_data('https://ai-pree.github.io/Portfolio/')
    qr.make(fit=True)

    image = qr.make_image(fill_color="blue", back_color="white")
    image.save('portfolio.png')


def main():
    pass

if __name__ == "__main__":
    main()
