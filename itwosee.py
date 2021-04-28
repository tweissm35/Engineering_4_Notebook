
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#set up accelerometer
lsm303 = Adafruit_LSM303.LSM303()

#Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Load default font.
font = ImageFont.load_default()

while  True:
	#clear display
	disp.clear()
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	#read data from accelerometer
	accel, mag = lsm303.read()

	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag

	# Write the accelerometer values
	draw.text((0, 0), 'x accel: '+str(accel_x),  font=font, fill=255)
	draw.text((0, 10), 'y accel: '+str(accel_y), font=font, fill=255)
	draw.text((0, 20), 'z accel: '+str(accel_z), font=font, fill=255)

	draw.text((0, 33), 'x mag: '+str(mag_x),  font=font, fill=255)
	draw.text((0, 43), 'y mag: '+str(mag_y), font=font, fill=255)
	draw.text((0, 53), 'z mag: '+str(mag_z), font=font, fill=255)

	# Display image.
	disp.image(image)
	disp.display()
