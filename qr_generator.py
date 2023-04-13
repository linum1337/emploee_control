import qrcode

def generateQr():
    id = '3'
    name = 'Василий'
    data = f"{id}/{name}"
    img = qrcode.make(data)
    img.save("test1.png")

generateQr()