import qrcode
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)
qr.add_data("https://www.youtube.com/watch?v=xvFZjo5PgG0") # INSIRA AQUI SEU LINK OU INFORMAÇÃO
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("test.jpeg")