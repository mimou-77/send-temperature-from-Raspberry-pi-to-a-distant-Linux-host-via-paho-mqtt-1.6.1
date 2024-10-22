# v2-send-simulated-temperature-values-in-an-infinite-loop

## on the raspberry pi:
this version simulates temperature values and sends them in an infinite loop
rand.py generates a random temperature value and writes it in the file "temp_input"
pub.py : in an infinite loop : calls rand.py, reads the temperature value stored in "temp_input", publishes it to the broker

## on the distant linux host:
sub.py receives messages from the broker in an infinite loop