import qrcode
text = input("Enter text to convert into QR Code: ")
img = qrcode.make(text)
img.save("qrcode.png")
print("QR Code saved as qrcode.png")