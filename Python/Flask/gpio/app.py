from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.output(17,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():
	msg="no click yet"
	if request.form.get('submitBtn1'):
		msg="You clicked the red button"
		GPIO.output(17,GPIO.HIGH)
	elif request.form.get('submitBtn2'):
		msg="You clicked the blue button"
		GPIO.output(18,GPIO.HIGH)

	print(request.form.get)

	return render_template("index.html", msg=msg)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80)
