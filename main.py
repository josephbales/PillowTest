from PIL import Image, ImageDraw, ImageFont, ImageOps


def process_message(drawing, message_text, font):
    message_text = message_text.replace('\r\n', ' ')
    message_text = message_text.replace('\n', ' ')
    message_text = message_text.replace('  ', ' ')
    number_of_lines = 1
    w, h = drawing.textsize(message_text, font=font)
    if w < 600:
        return message_text, number_of_lines, w, h

    number_of_lines = 2
    spaces = find_occurrences(message_text, ' ')
    for i in range(len(spaces) - 1, 0, -1):
        message_text = message_text.replace('\n', ' ')
        msg_list = list(message_text)
        msg_list[spaces[i]] = '\n'
        message_text = ''.join(msg_list)
        w, h = drawing.textsize(message_text, font=font)
        if w < 600:
            return message_text, number_of_lines, w, h

    return None


def find_occurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


# create an image
img = Image.new(mode='L', size=(630, 374), color=255)

png = Image.open('/mnt/c/Users/josep/Downloads/weather-icons-master/weather-icons-master/svg/png/wi-day-thunderstorm.png')

img.paste(png, (20, 15), png)

# get a font
temp_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 80)
cond_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 28)
cc_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 18)

# get a drawing context
d = ImageDraw.Draw(img)

# draw multiline text
temperature = '108°'
w, h = d.textsize(temperature, font=temp_fnt)
x_coord = (240 - w) / 2
d.multiline_text((x_coord, 190), temperature, font=temp_fnt)
d.multiline_text((260, 12), 'Current Conditions:', font=cc_fnt)
d.multiline_text((260, 32), 'Severe Thunderstorms', font=cond_fnt)
d.multiline_text((260, 80), 'Feels Like: 108°', font=cc_fnt)
d.multiline_text((260, 102), 'Relative Humidity: 80%', font=cc_fnt)
d.multiline_text((260, 124), 'Barometric Pressure: 30.92 inches', font=cc_fnt)
d.multiline_text((260, 146), 'Wind Speed: 28 mph', font=cc_fnt)
d.multiline_text((260, 168), 'Wind Direction: NNW', font=cc_fnt)
d.multiline_text((260, 204), 'Sunrise: 07:26:59 CST', font=cc_fnt)
d.multiline_text((260, 226), 'Sunset: 19:26:59 CST', font=cc_fnt)
d.multiline_text((260, 262), 'Updated at: 2020-11-17 19:26:59 CST', font=cc_fnt)

# Probably need a 100 char limit here to make sure it all fits in the box
message = "You can just push a little tree out of your brush like that. We can do a happy little picture today."
#message = "You can just push a little tree out of your brush like that."
msg, lines, width, height = process_message(d, message, cc_fnt)
print(msg)
print(lines)
print(width)
print(height)
y_coord = 312
if lines == 1:
    y_coord = 322
x_coord = (630 - width) / 2
d.multiline_text((x_coord, y_coord), msg, font=cc_fnt)

# draw lines
d.line([(240, 0), (240, 300)], fill=0, width=5)
d.line([(0, 300), (640, 300)], fill=0, width=5)

with_border = ImageOps.expand(img, border=5, fill='black')

with_border.save('text.bmp')
