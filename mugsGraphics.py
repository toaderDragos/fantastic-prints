## python3 - Double font message for Christmas
## Font files are not always in the same place
## Works with names 5 - 9 letters long 

from PIL import Image, ImageDraw, ImageFont
import os

fontsFolder = r'C:\Users\ASUS ROG\AppData\Local\Microsoft\Windows\Fonts'  # windows fonts e alt folder!!
fontName = 'ChristmasWish-monoline.otf'

x = 2.8  # size multiplier coefficient of all text, sizes and fonts
y = -100  # pixel offset from upper border

# Getting the names out of a random list from the internet
names = open(r'C:\Users\ASUS ROG\AppData\Local\Programs\Python\Python37\tshirtIrina\peopleX200.txt')
nameList = []
for i in range(0, 100):
    twoNames = names.readline()
    twoNames = twoNames.split('\t')  # lista din fisier este formatul: 83 \t Baiat \t Fata
    text4 = twoNames[1]  # Boy Name
    text5 = twoNames[2].strip('\n')  # Girl Name               # Making a single list
    nameList.append(text5)

# For loop to iterate through a list of keywords
for nameTest in nameList:
    letter = nameTest[0]
    text2 = 'is for'

    backgroundIm = Image.new('RGBA', (1800, 1800), (255, 0, 0, 0))  # png transparent
    draw = ImageDraw.Draw(backgroundIm)

    font1 = ImageFont.truetype(os.path.join(fontsFolder, fontName), int(270 * x))
    font2 = ImageFont.truetype(os.path.join(fontsFolder, fontName), int(120 * x))

    backgroundImSize = list(backgroundIm.size)
    letterSize = list(draw.textsize(letter, font1))
    text2Size = list(draw.textsize(text2, font2))  # marime txt intermediar
    nameTestSize = list(draw.textsize(nameTest, font1))

    letterOffset = backgroundImSize[0] / 2 - letterSize[0] / 2
    text2Offset = backgroundImSize[0] / 2 - text2Size[0] / 2
    nameOffset = backgroundImSize[0] / 2 - nameTestSize[0] / 2

    draw.text((letterOffset, y), letter, fill='black', font=font1)  # font mic
    draw.text((text2Offset, 270 * x + y), text2, fill='black', font=font2)  # font Santa
    draw.text((nameOffset, 370 * x + y), nameTest, fill='black', font=font1)  # Numele din lista

    backgroundIm.save((r'C:\Users\ASUS ROG\AppData\Local\Programs\Python\Python37\caniIrina\ ' + nameTest + '.png'),
                      dpi=(150, 150))

## im = Image.new('RGBA', (3600,3600), 'white') # 3600 la 72 dpi = 1800 x 1800 la 150 dpi
