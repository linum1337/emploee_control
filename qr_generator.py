import qrcode

def generateQr(id, name):
    data = f"{id}/{name}"
    img = qrcode.make(data)
    print(1)
    img.save("test1.png")

