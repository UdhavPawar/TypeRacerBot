from pynput.keyboard import Controller, Listener, Key # to simluate keyboard typing
from pynput import mouse # to get co-ordinates of text
from time import sleep # to delay bot else it will type too fast
from pyscreenshot import grab # to grab an in-place screenshot
from pytesseract import image_to_string # to convert image to text

# get mouse co-ordinates when clicked on image containing text
def mousePixels(x, y, button, pressed):
    if pressed: # get top pixels
        mousePixels.topLeft = x
        mousePixels.topRight = y
    else: # get bottom pixels
        mousePixels.bottomLeft = x
        mousePixels.bottomRight = y
    if not pressed: # if not pressed stop listener
        return False

# Collect mouse events until released
with mouse.Listener(on_click = mousePixels) as listener:
    listener.join()

# grab a screeshot of mouse pixels
textImage = grab(bbox=(mousePixels.topLeft, mousePixels.topRight, mousePixels.bottomLeft, mousePixels.bottomRight))
# note above is an in-place screen capture, to save to a file use below
# textImage.save("text.png")
text = str(image_to_string(textImage, lang = "eng")).replace("|", "I") # convert text inside image to text. note: replace condition was added as sometimes image_to_string function reads "I" as "|"
text = " ".join(text.splitlines()) # if image has multiple lines of text so will the string from image_to_string. Hence, we join the lines on space which will result into one single line string
print(text)

def keyboardTyper(key):
    if key == Key.backspace: # press space to initiate typing at current cursor's position. note: don't use a character within the text to be converted else pynput.keyboard will press it during first run thus re-trigerring a second run, then third ... ending in infite loop
        for char in text: # we don't to type all text at once, so similate real typing by iterating over and typing one character at a time
            keyboard.press(char)
            keyboard.release(char)
            sleep(0.05)

# Collect keyboard events until released
keyboard = Controller()
with Listener(on_press = keyboardTyper) as listener:
    listener.join()
