# send-temperature-from-Raspberry-pi-to-a-distant-Linux-host-via-paho-mqtt
3 scripts:
* a shell script that initializes the kernel module for AHT10 temperature sensor
* a python script (publisher) on the raspberry pi that publishes temperature values
* a python script (subscriber) on the linux host that recieves the temperature values and prints them
## getting-started:

on the distant linux host:
```bash
git clone https://github.com/mimou-77/send-temperature-from-Raspberry-pi-to-a-distant-Linux-host-via-paho-mqtt.git
```
work only with the directory "on_distant_Linux_host" containing the files that need to be on the distant linux host (the python script: subscriber)
```bash
git sparse-checkout set on_distant_Linux_host
git checkout
```
on the distant Linux host AND on the raspberry pi:
```bash
sudo apt install python3
```
```bash
pip install paho-mqtt
```


