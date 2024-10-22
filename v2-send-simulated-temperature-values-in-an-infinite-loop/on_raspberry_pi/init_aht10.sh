sudo modprobe aht10

lsmod | grep aht* || (echo "couldn't load aht10 module" ; exit)

# cas où on a le capteur
#echo aht10 0x38 > /sys/bus/i2c-1/new_device

python3 ./pub.py
