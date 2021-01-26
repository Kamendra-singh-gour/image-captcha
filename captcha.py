from  PIL import Image
height=100
width=100
img=Image.open("bus/b8.jpg")
img=img.resize((height,width))
img.show()
img.save("b8.png")
