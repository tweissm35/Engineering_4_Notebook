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
	if len(request.form.items())==2:
                print("both ok")
                msg="bothchecked"
                GPIO.output(17,GPIO.HIGH)
                GPIO.output(18,GPIO.HIGH)
	elif request.form.get('led1'):
		msg="checked1"
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(18,GPIO.LOW)
	elif request.form.get('led2'):
                msg="checked2"
                GPIO.output(18,GPIO.HIGH)
		GPIO.output(17,GPIO.LOW)
	else:
		msg="nocheck"
		GPIO.output(17,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)
	return render_template("index.html", msg=msg)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80)
