import pyqrcode

url = input("enter your url to get QR code: ")

Qr = pyqrcode.create(url)

Qr.png("webqr.png",scale=8)