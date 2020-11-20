from PIL import Image, ImageDraw, ImageFont, ImageOps


def process_message(drawing, message_text, font, max_width):
    message_text = message_text.replace('\r\n', ' ')
    message_text = message_text.replace('\n', ' ')
    message_text = message_text.replace('  ', ' ')
    number_of_lines = 1
    lw, lh = drawing.textsize(message_text, font=font)

    if lw > max_width:
        message_words = message_text.split()
        message_text = ''
        has_more_text = True
        while has_more_text:
            for i in range(0 , len(message_words) - 1):
                line = ' '.join(message_words[:i])
                lw, lh = drawing.textsize(line, font=font)
                if lw > max_width:
                    # If i is zero then this will fail
                    line = ' '.join(message_words[:i - 1])
                    message_text += f'{line}\n'
                    number_of_lines += 1
                    message_words = message_words[i - 1:]
                    line = ' '.join(message_words)
                    lw, lh = drawing.textsize(line, font=font)
                    if lw <= max_width:
                        has_more_text = False
                        message_text += f'{line}'
                        break

    lw, lh = drawing.textsize(message_text, font=font)
    return message_text, number_of_lines, lw, lh


# create an image
img = Image.new(mode='L', size=(630, 374), color=255)

png = Image.open('/mnt/c/Users/josep/Downloads/weather-icons-master/weather-icons-master/svg/png/wi-day-thunderstorm.png')

img.paste(png, (20, 15), png)

# get a font
temp_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 80)
cond_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 28)
cc_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 18)
alert_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 70)

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

# # Probably need a 100 char limit here to make sure it all fits in the box
# message = "You can just push a little tree out of your brush like that. We can do a happy little picture today."
# #message = "You can just push a little tree out of your brush like that."
# msg, lines, width, height = process_message(d, message, cc_fnt, 600)
# print(msg)
# print(lines)
# print(width)
# print(height)
# y_coord = 312
# if lines == 1:
#     y_coord = 322
# x_coord = (630 - width) / 2
# d.multiline_text((x_coord, y_coord), msg, font=cc_fnt)

d.rectangle([(4, 306), (232, 370)], fill='black')
d.multiline_text((9, 288), 'ALERT', font=alert_fnt, fill='white')


# draw lines
d.line([(240, 0), (240, 300)], fill=0, width=5)
d.line([(0, 300), (640, 300)], fill=0, width=5)

with_border = ImageOps.expand(img, border=5, fill='black')

with_border.save('text.bmp')
