import pytesseract
from PIL import Image

img_file=r"C:\Users\Khushi\Pictures\image1.jpg"
img=Image.open(img_file)
text=pytesseract.image_to_string(img)
print(text)
