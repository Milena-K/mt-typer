# open up chrome
# type https://monkey-type.com/
# make a screenshot of the text
# save it as '1.jpg' to the image path below

# read text from screen (tesseract ocr)
from tesserocr import PyTessBaseAPI

image = 'C:\\Users\\Milena\\Documents\\Programming\\Python\\mt-typer\\pictures\\1.jpg'
DATA_PATH = 'C:\\Users\\Milena\\Documents\\Programming\\Python\\mt-typer\\tesserocr-master\\tessdata'

with PyTessBaseAPI(DATA_PATH) as api:
	api.SetImageFile(image)
	text = api.GetUTF8Text()
	print(text)

# write text in the field  
import keyboard

keyboard.wait('right arrow')
for word in text.split():
	keyboard.write(word + " ")
