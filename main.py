from PIL import Image, ImageDraw, ImageFont, ImageOps


# get a font
temp_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 80)
cond_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 28)
cc_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 18)
alert_fnt = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf', 70)

def process_message(
        drawing: ImageDraw,
        message_text: str,
        font: ImageFont,
        line_spacing: int,
        max_width: int,
        max_lines: int):
    message_text = message_text.replace('\r\n', ' ')
    message_text = message_text.replace('\n', ' ')
    message_text = message_text.replace('  ', ' ')
    number_of_lines = 1
    lw, lh = drawing.multiline_textsize(text=message_text, font=font, spacing=line_spacing)

    if lw > max_width:
        message_words = message_text.split()
        message_text = ''
        has_more_text = True
        while has_more_text:
            for i in range(0 , len(message_words)):
                line = ' '.join(message_words[0:i + 1])
                lw, lh = drawing.multiline_textsize(text=line, font=font, spacing=line_spacing)
                if lw > max_width:
                    line = ' '.join(message_words[:i - 1])
                    message_text += f'{line}\n'
                    number_of_lines += 1
                    if number_of_lines > max_lines:
                        has_more_text = False
                        message_text = f'{message_text[:len(message_text) - 3]}...'
                        break
                    message_words = message_words[i - 1:]
                    line = ' '.join(message_words)
                    lw, lh = drawing.multiline_textsize(text=line, font=font, spacing=line_spacing)
                    if lw <= max_width:
                        has_more_text = False
                        message_text += f'{line}'
                        break
                    break

    lw, lh = drawing.multiline_textsize(text=message_text, font=font, spacing=line_spacing)
    number_of_lines = message_text.count('\n') + 1
    return message_text, number_of_lines, lw, lh

def generate_black_image(**kwargs):
    # create an image
    img = Image.new(mode='L', size=(630, 374), color=255)

    png = Image.open(
        '/mnt/c/Users/josep/Downloads/weather-icons-master/weather-icons-master/svg/png/wi-day-thunderstorm.png')

    img.paste(png, (20, 15), png)

    # get a drawing context
    d = ImageDraw.Draw(img)

    # draw lines
    d.line(xy=[(240, 0), (240, 300)], fill=0, width=5)
    d.line(xy=[(0, 300), (640, 300)], fill=0, width=5)

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
    message = "X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O X O."
    #message = "Severe Thunderstorm Warning, Tornado Watch, Flash Flood Watch, Winter Weather Advisory"
    #message = "You can just push a little tree out of your brush like that. We can do a happy little picture today."
    #message = "You can just push a little tree out of your brush like that. Wecandoahappylittlepicturetoday.Youcanjustpushalittletreeoutofyourbrushlikethat. We can do a happy little picture today. You can just push a little tree out of your brush like that. We can do a happy little picture today. You can just push a little tree out of your brush like that. We can do a happy little picture today."
    #message = "You can just push a little tree out of your brush like that."
    msg, lines, width, height = process_message(drawing=d, message_text=message, font=cc_fnt, line_spacing=3, max_width=616, max_lines=3)
    x_coord = (630 - width) / 2
    y_coord = (74 - height) / 2 + 298
    d.multiline_text(xy=(x_coord, y_coord), text=msg, font=cc_fnt, spacing=3)

    with_border = ImageOps.expand(image=img, border=5, fill='black')

    with_border.save(fp='img_black.bmp')


def generate_red_image():
    # create an image
    img = Image.new(mode='L', size=(640, 384), color=255)

    # get a drawing context
    d = ImageDraw.Draw(img)

    alert_message = "Severe Thunderstorm Warning, Tornado Watch, Flash Flood Watch, Winter Weather Advisory"
    # alert_message = "Some message, that's completely different than that other one, with a comma or two, but"
    # alert_message = "A very very simple message xoxoxo xoxoxo xoxoxo"
    msg, lines, width, height = process_message(drawing=d, message_text=alert_message, font=cc_fnt, line_spacing=3,
                                                max_width=390, max_lines=3)
    d.rectangle(xy=[(8, 306), (232, 370)], fill='black')
    d.multiline_text(xy=(13, 288), text='ALERT', font=alert_fnt, fill='white')
    x_coord = (390 - width) / 2 + 242
    y_coord = (74 - height) / 2 + 298
    d.multiline_text(xy=(x_coord, y_coord), text=msg, font=cc_fnt, spacing=3, fill='black')

    img.save(fp='img_red.bmp')

generate_black_image()
generate_red_image()
