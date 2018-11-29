from img2html.converter import Img2HTMLConverter

converter = Img2HTMLConverter(char='爱')
html = converter.convert("mnls.jpg")

with open("mnls.html", mode='w', encoding="utf-8") as f:
    f.write(html)
