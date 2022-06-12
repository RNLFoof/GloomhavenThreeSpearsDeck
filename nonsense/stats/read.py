import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('bandit-archer-0.png')

text = pytesseract.image_to_string(img)
print(text)