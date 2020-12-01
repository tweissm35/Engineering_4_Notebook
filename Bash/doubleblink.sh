gpio mode 0 out#set the pins to output mode
gpio mode 1 out#I only need to do this once

for n in {1..10}#for loop that repeats 10 times
do
	gpio write 0 1#on
	gpio write 1 1
	sleep 0.5#wait half a second
	gpio write 0 0#off
	gpio write 1 0
	sleep 0.5
done#end for loop
