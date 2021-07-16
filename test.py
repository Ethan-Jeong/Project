import pytesseract # 설치 방법 : https://ansan-survivor.tistory.com/313
import cv2 # 설치 방법 : https://beausty23.tistory.com/72
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

image = cv2.imread('20201106.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename), lang='kor')
os.remove(filename)

print(type(text))
print(text)
