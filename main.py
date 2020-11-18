from PIL import Image, ImageDraw, ImageFont, ImageOps

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
d.multiline_text((260, 13), 'Current Conditions:', font=cc_fnt)
d.multiline_text((260, 37), 'Severe Thunderstorms', font=cond_fnt)
d.multiline_text((260, 80), 'Feels Like: 108°', font=cc_fnt)
d.multiline_text((260, 102), 'Relative Humidity: 80%', font=cc_fnt)
d.multiline_text((260, 124), 'Barometric Pressure: 30.92 inches', font=cc_fnt)
d.multiline_text((260, 146), 'Wind Speed: 28 mph', font=cc_fnt)
d.multiline_text((260, 168), 'Wind Direction: NNW', font=cc_fnt)
d.multiline_text((260, 204), 'Sunrise: 07:26:59 CST', font=cc_fnt)
d.multiline_text((260, 226), 'Sunset: 19:26:59 CST', font=cc_fnt)
d.multiline_text((260, 265), 'Updated at: 2020-11-17 19:26:59 CST', font=cc_fnt)

# Probably need a 100 char limit here to make sure it all fits in the box
d.multiline_text((15, 300), "You can just push a little tree out of your brush like that. I\nthought today we would do a happy little picture. Everybody's\ndifferent. Trees are different. Let them all be individuals.", font=cc_fnt)

# draw lines
d.line([(240, 0), (240, 300)], fill=0, width=5)
d.line([(0, 300), (640, 300)], fill=0, width=5)

with_border = ImageOps.expand(img, border=5, fill='black')

with_border.save('text.bmp')
