from PIL import Image, ImageDraw, ImageFont, ImageOps
from os import path
 

base = Image.open('./base.png').convert("RGBA")


print("Light theme text:")
dtext = input()
print("Dark theme text:")
ltext = input()
            


def line_splitter(text, width):
    wordsRemaining = text.count(" ") + 1
    lineTextList = ["", text]
    lines = []
    while wordsRemaining > 0:
        appCharCount = ((lineTextList[1])[:width]).count(" ") + 1
        lineText = ' '.join(lineTextList[1].split()[:appCharCount])
        exactCharCount = lineText.count(" ") + 1
        lineTextList = lineTextList[1].split(lineText)
        lines += [lineText]
        wordsRemaining -= exactCharCount
    return(lines)
    

def multi_text_line(image, text, font, text_color, text_start_height):
     # pylint: disable=unused-variable
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = line_splitter(text=text, width=31)
    for line in lines:
        line_width, line_height = font.getsize(line)
        for i in range(0, 120):
            draw.text(((image_width - line_width) / 2, y_text), line, font=fnt, fill=text_color)
        y_text += line_height

Light = Image.new('RGBA', base.size, (255,255,255,0))
fnt = ImageFont.truetype('./comic.ttf', 20)
l = ImageDraw.Draw(Light)
multi_text_line(Light, ltext, fnt, (255,255,255,255), 0)
ly = 1
while ly < 500:
    l.line((0, ly, 500, ly) + base.size, fill=0)
    ly += 2

Dark = Image.new('RGBA', base.size, (255,255,255,0))
fnt = ImageFont.truetype('./comic.ttf', 20)
d = ImageDraw.Draw(Dark)
multi_text_line(Dark, dtext, fnt, (54,57,63,255), 0)
dy = 2
while dy < 501:
    d.line((0, dy, 500, dy) + base.size, fill=0)
    dy += 2

two = Image.alpha_composite(base, Light)
out = Image.alpha_composite(two, Dark)



fname = "output.png"
n = 0
while path.exists(fname) is True:
    n += 1
    fname = "output (" + str(n) + ").png"

out.save(fname, "PNG")
