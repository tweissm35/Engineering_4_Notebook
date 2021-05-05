
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

import Adafruit_LSM303

from PIL import Image, ImageDraw, ImageFont

def mapp(x,in_min,in_max,out_min,out_max):#this function maps a value in one range to the equivalent value in another
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

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
#font = ImageFont.load_default()
font = ImageFont.truetype(font="/home/pi/Documents/Engineering_4_Notebook/Pixeled.ttf")

while  True:
	#clear display
	disp.clear()
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	draw.ellipse((32, 0, height+32, height-1), outline=255, fill=0)

	#read data from accelerometer
	accel, mag = lsm303.read()

	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag

	y_pos=mapp(accel_x,-1200,1200,0,height)
	x_pos=mapp(accel_y,-1200,1200,32,96)


	# Write the accelerometer values
	#draw.text((0, 0), 'x accel: '+str(accel_x),  font=font, fill=255)

	draw.text((0,0), 'edges represent 12ms^2',font=font, fill=255)

	draw.line([(64,0),(64,64)],width=1, fill=255)
	draw.line([(32,32),(96,32)],width=1, fill=255)

	draw.ellipse((x_pos-2, y_pos-2, x_pos+2, y_pos+2), fill=255)

	# Display image.
	disp.image(image)
	disp.display()
