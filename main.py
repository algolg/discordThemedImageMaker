from PIL import Image, ImageDraw, ImageFont
 

base = Image.open('./base.png').convert("RGBA")


print("Light theme text:")
dtext = input()
print("Dark theme text:")
ltext = input()

def line_splitter(text, width):
    wordsremaining = text.count(" ") + 1
    textList = [".", text]
    lines = []
    while wordsremaining > 0:
        appLine1count = ((textList[1])[:width]).count(" ") + 1
        lineText = ' '.join(textList[1].split()[:appLine1count])
        exactLine1Count = lineText.count(" ") + 1
        textList = textList[1].split(lineText)
        lines += [lineText]
        wordsremaining -= exactLine1Count
    return(lines)
    

def multi_text_line(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = line_splitter(text=text, width=31)
    for line in lines:
        line_width, line_height = font.getsize(line)
        for i in range(0, 30):
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

out.save("output.png", "PNG")
