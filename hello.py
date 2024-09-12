from rembg import remove
import easygui
from PIL import Image

inputFile = easygui.fileopenbox("select a file...")
outputFile = easygui.filesavebox("save file")

input = Image.open(inputFile)
output = remove(input)

output.save(outputFile)