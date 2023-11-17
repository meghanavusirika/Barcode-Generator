import pyqrcode
from pyqrcode import QRCode

print("Welcome To Barcode Generator!")
print()
link = input('Enter the link: ')
name = input('Enter the name of the file: ')
url = pyqrcode.create(link)

url.svg(name+'.svg', scale = 8)

print()
print('Barcode Generated!')
